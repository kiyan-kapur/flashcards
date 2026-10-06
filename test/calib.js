// HARD calibration behaviour: only variant 1s at start, hints step through, a miss shows the method and brings variant 1 back,
// a clean right answer on variant 1 unlocks that stem's trap variants.
const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright');
const http = require('http'), fs = require('fs'), path = require('path');
const root = path.join(__dirname, '..', 'app');
const srv = http.createServer((req, res) => { const u = decodeURIComponent(req.url.split('?')[0]); const p = path.join(root, u === '/' ? 'index.html' : u);
  fs.readFile(p, (e, d) => { if (e) { res.writeHead(404); return res.end(); } res.writeHead(200, {'Content-Type': p.endsWith('.svg') ? 'image/svg+xml' : 'text/html'}); res.end(d); }); }).listen(8767);
(async () => {
  const b = await chromium.launch(); const pg = await b.newPage({viewport: {width: 1280, height: 1300}});
  const errs = []; pg.on('pageerror', e => errs.push(String(e)));
  await pg.goto('http://localhost:8767/'); await pg.waitForTimeout(600);
  await pg.evaluate(() => { localStorage.clear(); S.attempts = []; S.bankProg = {}; openItem('bio13-hard'); });
  const q0 = await pg.evaluate(() => S.bank.queue.map(id => bankOf().questions.find(q => q.id === id)).map(q => q.id + ' v' + q.vi));
  console.log('START QUEUE', q0.length, q0.join(', '));
  // put the trypsin card first for the preview
  await pg.evaluate(() => { const Q = S.bank.queue; Q.splice(Q.indexOf('v2-q10-c1'), 1); Q.unshift('v2-q10-c1'); S.bank.qi = 0; render(); });
  await pg.click('#bk-hint'); await pg.click('#bk-hint'); await pg.waitForTimeout(150);
  console.log('HINT BUTTON NOW', await pg.$eval('#bk-hint', e => e.textContent), '| steps shown', await pg.$$eval('.why-block ol li', l => l.length));
  await pg.screenshot({path: path.join(__dirname, 'shot-v1-hint.png'), fullPage: true});
  // wrong answer
  await pg.click('[data-pick="0"]'); await pg.click('#bk-check'); await pg.waitForTimeout(150);
  const meth = await pg.$$eval('.why-block .row b', l => l.map(x => x.textContent));
  console.log('AFTER MISS rows', meth.join(' | '));
  await pg.screenshot({path: path.join(__dirname, 'shot-v1-miss.png'), fullPage: true});
  const next = await pg.evaluate(() => S.bank.queue.slice(S.bank.qi + 1, S.bank.qi + 8));
  console.log('NEXT 7 after miss', next.join(', '), '| v1 back at +' + (next.indexOf('v2-q10-c1') + 1));
  // later, answer the trypsin v1 right with Sure
  await pg.evaluate(() => { const i = S.bank.queue.indexOf('v2-q10-c1', S.bank.qi + 1); S.bank.qi = i - 1; });
  await pg.click('#bk-next'); await pg.waitForTimeout(100);
  console.log('NOW ON', await pg.evaluate(() => S.bank.queue[S.bank.qi]), '| hint reset label', await pg.$eval('#bk-hint', e => e.textContent));
  await pg.click('[data-conf="sure"]'); await pg.click('[data-pick="1"]'); await pg.click('#bk-check'); await pg.waitForTimeout(100);
  const after = await pg.evaluate(() => S.bank.queue.slice(S.bank.qi + 1).filter(id => /q10-/.test(id)).map(id => id + '@+' + (S.bank.queue.indexOf(id, S.bank.qi + 1) - S.bank.qi)));
  console.log('Q10 TRAPS UNLOCKED', after.join(', '));
  console.log('ATTEMPT ROWS', JSON.stringify(await pg.evaluate(() => S.attempts.map(a => [a.id, a.ok, a.conf, a.hints]))));
  console.log('ERRORS', errs); await b.close(); srv.close();
})();
