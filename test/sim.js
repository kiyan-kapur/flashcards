// Simulate the spacing logic outside the page: coverage, stem gaps and week runs over many random passes.
const fs = require('fs'), path = require('path');
const src = fs.readFileSync(path.join(__dirname, '..', 'build', 'v2.js'), 'utf8');
const fn = src.slice(src.indexOf('function v2Order'), src.indexOf('function v2Mastered'));
const v2Order = eval('(' + fn.replace(/^function v2Order/, 'function') + ')');
const bank = ['hard', 'medium', 'easy', 'jic'].flatMap(t => { try { return JSON.parse(fs.readFileSync(path.join(__dirname, '..', 'build', t + '.json'))); } catch (e) { return []; } });
function stats(pool, opts, runs = 2000) {
  let full = 0, minGap = 99, gapViol = 0, weekRun = 0;
  for (let r = 0; r < runs; r++) {
    const ids = v2Order(pool, opts), by = Object.fromEntries(pool.map(q => [q.id, q]));
    if (new Set(ids).size === Math.min(ids.length, pool.length)) full++;
    const last = {};
    ids.forEach((id, i) => { const s = by[id].stem; if (s && last[s] !== undefined) { const g = i - last[s]; minGap = Math.min(minGap, g); if (g < (opts.gap ?? 8)) gapViol++; } if (s) last[s] = i; });
    let run = 1; for (let i = 1; i < ids.length; i++) { run = by[ids[i]].week === by[ids[i - 1]].week ? run + 1 : 1; if (run > 3) { weekRun++; break; } }
  }
  return {runs, fullCoverage: full, minStemGapSeen: minGap, gapViolationsPerRun: +(gapViol / runs).toFixed(2), runsWith4SameWeek: weekRun};
}
const hard = bank.filter(q => q.level === 'hard');
const hardGap = Math.max(2, Math.ceil(new Set(hard.map(q => q.stem)).size * 0.6));
console.log('HARD bank, gap', hardGap, stats(hard, {gap: hardGap}));
if (process.argv[2] === 'show') {
  let seed = 7; const rand = () => (seed = (seed * 16807) % 2147483647) / 2147483647;
  const pool = process.argv[3] === 'mixed' ? bank : hard;
  const ids = v2Order(pool, process.argv[3] === 'mixed' ? {len: 60, jicEvery: 6, rand} : {gap: hardGap, rand});
  const by = Object.fromEntries(pool.map(q => [q.id, q]));
  console.log(ids.map((id, i) => `${String(i + 1).padStart(2)} ${by[id].level.toUpperCase().padEnd(6)} Q${by[id].stem ?? '-'} v${by[id].vi} W${by[id].week}`).join('\n'));
}
