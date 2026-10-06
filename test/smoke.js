// Smoke test: open the patched page, walk Biology -> HARD, answer, reveal, open the Doubt Sheet, check nothing threw.
const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright');
const http = require('http'), fs = require('fs'), path = require('path');
const root = path.join(__dirname, '..', 'app');
const srv = http.createServer((req, res) => {
  const p = path.join(root, decodeURIComponent(req.url.split('?')[0]) === '/' ? 'index.html' : decodeURIComponent(req.url.split('?')[0]));
  fs.readFile(p, (e, d) => { if (e) { res.writeHead(404); return res.end(); }
    res.writeHead(200, {'Content-Type': p.endsWith('.svg') ? 'image/svg+xml' : 'text/html'}); res.end(d); });
}).listen(8765);
(async () => {
  const b = await chromium.launch(); const pg = await b.newPage({viewport: {width: 1280, height: 1000}});
  const errs = []; pg.on('pageerror', e => errs.push(String(e))); pg.on('console', m => { if (m.type() === 'error' && !/404|Failed to load/.test(m.text())) errs.push(m.text()); });
  await pg.goto('http://localhost:8765/'); await pg.waitForTimeout(800);
  await pg.click('#go-home'); await pg.waitForTimeout(200);
  await pg.click('[data-folder="bio"]'); await pg.waitForTimeout(300);
  const rows = await pg.$$eval('[data-open]', els => els.map(e => e.dataset.open + ': ' + e.querySelector('h4').textContent));
  console.log('FOLDER ROWS', rows);
  await pg.click('[data-open="bio13-hard"]'); await pg.waitForTimeout(300);
  const tag = await pg.$eval('.tagrow .tag', e => e.textContent); console.log('TAG', tag);
  await pg.screenshot({path: path.join(__dirname, 'shot-hard-q.png'), fullPage: true});
  const queue = await pg.evaluate(() => S.bank.queue.slice());
  console.log('QUEUE LEN', queue.length, 'unique', new Set(queue).size);
  // answer wrong on purpose with Guessing
  const q0 = await pg.evaluate(() => { const b = bankOf(); return b.questions.find(x => x.id === S.bank.queue[S.bank.qi]); });
  const wrong = q0.a === 0 ? 1 : 0;
  await pg.click('[data-conf="guess"]'); await pg.click(`[data-pick="${wrong}"]`); await pg.click('#bk-check'); await pg.waitForTimeout(200);
  await pg.screenshot({path: path.join(__dirname, 'shot-hard-after.png'), fullPage: true});
  const st = await pg.evaluate(() => ({att: S.attempts.slice(-1)[0], q: S.bank.queue.slice(S.bank.qi, S.bank.qi + 8)}));
  console.log('ATTEMPT', JSON.stringify(st.att));
  const fam = await pg.evaluate(ids => ids.map(id => (bankOf().questions.find(q => q.id === id) || {}).stem), st.q);
  console.log('NEXT 8 STEMS after miss on stem', q0.stem, fam);
  await pg.click('#bk-next'); await pg.click('#bk-reveal'); await pg.waitForTimeout(150);
  const ls = await pg.evaluate(() => JSON.parse(localStorage.getItem(KEY)).attempts.length);
  console.log('ATTEMPTS IN LOCALSTORAGE', ls);
  await pg.click('[data-bview="dsheet"]'); await pg.waitForTimeout(200);
  await pg.screenshot({path: path.join(__dirname, 'shot-doubt.png'), fullPage: true});
  for (const id of ['bio13-ex1', 'psy-quiz1', 'ch2-bank']) { await pg.evaluate(i => openItem(i), id); await pg.waitForTimeout(150); }
  const mockBtn = await pg.evaluate(() => { openItem('bio13-ex1'); return !!document.getElementById('bk-mock2'); });
  console.log('MOCK BUTTON (should be false until 25 stems)', mockBtn);
  console.log('ERRORS', errs);
  await b.close(); srv.close();
})();
