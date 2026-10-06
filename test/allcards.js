// Render every v2 card in every level bank, unanswered and answered, and fail on any page error.
const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright');
const http = require('http'), fs = require('fs'), path = require('path');
const root = path.join(__dirname, '..', 'app');
const srv = http.createServer((req, res) => { const u = decodeURIComponent(req.url.split('?')[0]); const p = path.join(root, u === '/' ? 'index.html' : u);
  fs.readFile(p, (e, d) => { if (e) { res.writeHead(404); return res.end(); } res.writeHead(200, {'Content-Type': p.endsWith('.svg') ? 'image/svg+xml' : 'text/html'}); res.end(d); }); }).listen(8766);
(async () => {
  const b = await chromium.launch(); const pg = await b.newPage({viewport: {width: 1280, height: 1100}});
  const errs = [], missing = []; pg.on('pageerror', e => errs.push(String(e)));
  pg.on('response', r => { if (r.status() === 404 && r.url().includes('/fig/v2/')) missing.push(r.url()); });
  await pg.goto('http://localhost:8766/'); await pg.waitForTimeout(600);
  for (const bank of ['bio13-hard', 'bio13-med', 'bio13-easy']) {
    const n = await pg.evaluate(async bk => { openItem(bk); const ids = bankOf().questions.map(q => q.id); let ok = 0;
      for (const id of ids) { S.bank.queue = [id]; S.bank.qi = 0; S.bank.answered = false; S.bank.revealed = false; S.bank.sel = null; render();
        const q = bankOf().questions[0] && bankOf().questions.find(x => x.id === id);
        if (!document.querySelector('.tagrow .tag').textContent.startsWith(q.level.toUpperCase())) throw new Error('tag ' + id);
        S.bank.answered = true; S.bank.choice = q.a; render();
        if (document.querySelectorAll('.why-block .row').length < 2) throw new Error('why ' + id); ok++; }
      return ok; }, bank);
    console.log(bank, 'rendered', n);
  }
  for (const [bank, file] of [['bio13-med', 'shot-medium.png'], ['bio13-easy', 'shot-easy.png']]) {
    await pg.evaluate(bk => { openItem(bk); S.bank.qi = 0; render(); }, bank); await pg.waitForTimeout(400);
    await pg.screenshot({path: path.join(__dirname, file), fullPage: true});
  }
  await pg.waitForTimeout(300);
  console.log('missing figs', missing, 'ERRORS', errs);
  await b.close(); srv.close();
})();
