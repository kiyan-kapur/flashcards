/* ============== BIO 0013 EXAM 1 REBUILD (v2): one bank per level, per-attempt log, spacing rules ============== */
// The old bank is retired, never deleted: its questions stay so the Doubt Sheet can read their history.
BIO13_Q.forEach(q=>{ q.status = "void"; });
const LVL = {hard:{t:"HARD", tag:"heat-red", heat:"red"}, medium:{t:"MEDIUM", tag:"heat-orange", heat:"orange"},
             easy:{t:"EASY", tag:"heat-green", heat:"green"}, jic:{t:"JUST IN CASE", tag:"heat-yellow", heat:"yellow"}};
BIO13_V2.forEach(q=>{
  q.ch = q.week; q.heat = LVL[q.level].heat; q.trap = q.trap || ""; q.status = q.status || "active";
  q.src = q.level === "jic" ? "Just in case · " + q.topic : "Redacted Q" + q.stem + " · variant " + q.vi + " of " + q.vn;
});
const v2Level = l => BIO13_V2.filter(q=>q.level === l && q.status !== "void");
const WEEKS = {1:"Week 1", 2:"Week 2", 3:"Week 3", 4:"Week 4"};
function levelTag(q){
  const L = LVL[q.level];
  const txt = q.level === "jic" ? L.t + " · " + q.topic : L.t + " · Redacted Q" + q.stem + " · variant " + q.vi + " of " + q.vn;
  return '<span class="tag '+L.tag+'">'+esc(txt)+'</span>';
}
function mockReady(b){ return new Set(b.questions.filter(q=>q.stem).map(q=>q.stem)).size === 25; }

/* ---------- per-attempt log: one row per Check or Reveal ---------- */
function logAttempt(q, chose, ok, revealed){
  const b = bankOf();
  S.attempts.push({id:q.id, bank:b ? b.id : null, stem:q.stem || null, topic:q.topic, chose:chose, key:q.a, ok:!!ok,
                   conf:S.bank.conf || null, rev:!!revealed, hints:S.bank.hintQ === q.id ? (S.bank.hintN || 0) : 0, at:Date.now()});
}

/* ---------- spacing (Step 5) ----------
   Pure function so it can be simulated outside the page. Rules:
   - a stem never repeats inside 8 questions (relaxed only when fewer stems exist than the gap needs);
   - a variant does not repeat until every variant of its stem has been seen;
   - no more than 3 in a row from one week;
   - HARD stems weigh 3, MEDIUM 2, EASY 1; a HARD stem drops to 1 once each of its variants has been right with Sure or Fairly sure;
   - Just-in-Case slots in at 1 per jicEvery questions (mixed bank only). */
function v2Order(pool, o){
  const rnd = o.rand || Math.random, seen = o.seen || (()=>0), mastered = o.mastered || (()=>false);
  const W = {hard:3, medium:2, easy:1};
  const main = pool.filter(q=>q.level !== "jic"), jic = pool.filter(q=>q.level === "jic");
  const byStem = {}; main.forEach(q=> (byStem[q.stem] = byStem[q.stem] || []).push(q));
  const stems = Object.keys(byStem), used = {}, lastAt = {}, out = [];
  // Mixed bank: a stem never repeats inside 8. A single-level bank has only 8 or 9 stems, where a gap of 8 forces strict
  // rotation and some variants would never show, so it uses a gap of about 60% of its stems (5 or 6) instead.
  const gap = o.gap != null ? o.gap : Math.min(8, stems.length) - 1;
  const len = o.len || pool.length;
  const pickVariant = list => list.slice().sort((x,y)=>
    ((used[x.id]||0) - (used[y.id]||0)) || ((seen(x.id) + (used[x.id]||0)) - (seen(y.id) + (used[y.id]||0))) || (rnd() - .5))[0];
  const weekOf = id => (pool.find(q=>q.id===id) || {}).week;
  if(o.first){ const f = pool.find(q=>q.id===o.first); if(f){ out.push(f.id); used[f.id] = 1; if(f.stem) lastAt[f.stem] = 0; } }
  while(out.length < len){
    const pos = out.length;
    if(o.jicEvery && jic.length && (pos + 1) % o.jicEvery === 0){
      const j = pickVariant(jic); out.push(j.id); used[j.id] = (used[j.id]||0) + 1; continue;
    }
    if(!stems.length) break;
    const last3 = out.slice(-3).map(weekOf), wk = last3.length === 3 && last3.every(w=>w === last3[0]) ? last3[0] : null;
    const near = (s, g)=> lastAt[s] !== undefined && pos - lastAt[s] <= g;
    const fresh = s=> byStem[s].some(q=>!used[q.id]);
    // Prefer stems that still have an unseen variant this pass. Only if every such stem sits inside the gap does the gap
    // shrink, one step at a time, so a pass shows every variant before repeating any.
    let ok = [];
    for(let g = gap; g >= 1 && !ok.length; g--){
      ok = stems.filter(s=> !near(s, g) && fresh(s) && byStem[s][0].week !== wk);
      if(!ok.length) ok = stems.filter(s=> !near(s, g) && fresh(s));
    }
    if(!ok.length) ok = stems.filter(s=> !near(s, gap) && byStem[s][0].week !== wk);
    if(!ok.length) ok = stems.filter(s=> !near(s, gap));
    if(!ok.length) ok = [stems.slice().sort((a,b)=> (lastAt[a] ?? -1) - (lastAt[b] ?? -1))[0]];
    const wt = s=>{
      const l = byStem[s][0].level;
      let w = (l === "hard" && byStem[s].every(q=>mastered(q.id))) ? 1 : W[l];
      const left = byStem[s].filter(q=>!used[q.id]).length;
      w *= left ? left : 0.15;                                 // stems with more unseen variants go more often, so a pass covers every variant
      return w;
    };
    let tot = ok.reduce((t,s)=>t + wt(s), 0), r = rnd() * tot, s = ok[0];
    for(const k of ok){ r -= wt(k); if(r <= 0){ s = k; break; } }
    const v = pickVariant(byStem[s]);
    out.push(v.id); used[v.id] = (used[v.id]||0) + 1; lastAt[s] = pos;
  }
  return out;
}
// HARD calibration: variant 1 of each stem is problem-set level. The trap variants stay locked until variant 1 has been
// answered right without pressing Guessing.
function v1Of(b, stem){ return b.questions.find(x=>x.stem === stem && x.vi === 1); }
function v1Right(b, stem){
  const v = v1Of(b, stem);
  return !!v && (S.attempts || []).some(a=> a.id === v.id && a.ok && a.conf !== "guess");
}
function lockedOut(b, q){ return q.level === "hard" && q.vi > 1 && !v1Right(b, q.stem); }
function hintHTML(q){
  if(!q.hint || S.bank.hintQ !== q.id || !S.bank.hintN) return "";
  return '<div class="why-block"><div class="row"><b>Hint, step by step</b><ol style="margin:4px 0 0;padding-left:20px">'+
    q.hint.slice(0, S.bank.hintN).map(t=>'<li style="margin:3px 0">'+esc(t)+'</li>').join("")+'</ol></div></div>';
}
function hintLabel(q){
  const n = S.bank.hintQ === q.id ? S.bank.hintN : 0;
  return n === 0 ? "Step-by-step hint" : n < q.hint.length ? "Next step (" + n + " of " + q.hint.length + ")" : "All steps shown";
}
function methodHTML(q){
  return '<div class="row trap"><b>The method, step by step</b><ol style="margin:4px 0 0;padding-left:20px">'+
    q.hint.map(t=>'<li style="margin:3px 0">'+esc(t)+'</li>').join("")+'</ol></div>';
}
function v2Mastered(id){ const c = (S.bankProg[id] || {}).conf || {}; return ((c.sure||{}).ok || 0) + ((c.fair||{}).ok || 0) > 0; }
function v2Build(b, keepAt){
  const nMain = b.questions.filter(q=>q.level !== "jic").length;
  const pool = b.questions.filter(q=> !lockedOut(b, q));
  S.bank.queue = v2Order(pool, {
    len: b.mixJic ? Math.max(60, nMain) : pool.length,
    seen: id=> (S.bankProg[id] || {}).seen || 0, mastered: v2Mastered,
    jicEvery: b.mixJic ? 6 : 0, first: keepAt,
    gap: b.mixJic ? undefined : Math.max(2, Math.ceil(new Set(b.questions.map(q=>q.stem)).size * 0.6))
  });
  S.bank.qi = 0; S.bank.sess = {sureOk:{}};
  S.bank.answered = false; S.bank.revealed = false; S.bank.choice = null; S.bank.sel = null; S.bank.finished = false;
}
// After each answer: a miss, a reveal or a "Guessing" brings the stem back 4 to 6 questions later as a DIFFERENT variant;
// right with "Sure" twice retires that variant for the session.
function v2After(q, ok, conf){
  const b = bankOf();
  if(!b || !b.v2 || !q.stem) return;
  const sess = S.bank.sess || (S.bank.sess = {sureOk:{}});
  const Q = S.bank.queue, here = S.bank.qi;
  if(q.level === "hard"){
    // HARD: a miss, reveal or Guessing brings back variant 1 (never a harder one); a clean right answer on variant 1
    // unlocks the trap variants for that stem and slots them in later in the session.
    const v1 = v1Of(b, q.stem);
    if(!ok || conf === "guess"){
      for(let i = Math.min(Q.length - 1, here + 6); i > here; i--){ const x = b.questions.find(z=>z.id === Q[i]); if(x && x.stem === q.stem) Q.splice(i, 1); }
      Q.splice(Math.min(here + 4 + Math.floor(Math.random()*3), Q.length), 0, v1.id);
      return;
    }
    if(q.vi === 1 && !sess["unlocked" + q.stem]){
      sess["unlocked" + q.stem] = true;
      // one trap variant now, about 6 questions on; the rest join the next pass, where normal spacing applies
      const t = b.questions.filter(x=>x.stem === q.stem && x.vi > 1).sort((x,y)=> x.vi - y.vi)[0];
      if(t && !Q.slice(here + 1).includes(t.id)) Q.splice(Math.min(here + 6, Q.length), 0, t.id);
    }
  }
  if(!ok || conf === "guess"){
    const sibs = b.questions.filter(x=>x.stem === q.stem && x.id !== q.id);
    if(!sibs.length) return;
    const sib = sibs.slice().sort((x,y)=> ((S.bankProg[x.id]||{}).seen||0) - ((S.bankProg[y.id]||{}).seen||0) || Math.random() - .5)[0];
    // drop any copy of this stem already sitting in the next 6 slots so it is not seen twice
    for(let i = Math.min(Q.length - 1, here + 6); i > here; i--){ const x = b.questions.find(z=>z.id === Q[i]); if(x && x.stem === q.stem) Q.splice(i, 1); }
    Q.splice(Math.min(here + 4 + Math.floor(Math.random()*3), Q.length), 0, sib.id);
  } else if(conf === "sure"){
    sess.sureOk[q.id] = (sess.sureOk[q.id] || 0) + 1;
    if(sess.sureOk[q.id] >= 2) for(let i = Q.length - 1; i > here; i--) if(Q[i] === q.id) Q.splice(i, 1);
  }
}

/* ---------- Doubt Sheet: all BIO 13 history, void and new, worst concept first ---------- */
function doubtSheetRows(){
  const byId = {}; BIO13_Q.concat(BIO13_V2).forEach(q=> byId[q.id] = q);
  const G = {}, g = t=> G[t] || (G[t] = {topic:t, n:0, ok:0, sureWrong:0, rev:0, last:null, lastAt:-1, old:0});
  const logged = new Set();
  (S.attempts || []).forEach(a=>{
    const q = byId[a.id]; if(!q) return; logged.add(a.id);
    const r = g(q.topic);
    if(a.rev){ r.rev++; return; }
    r.n++; if(a.ok){ r.ok++; return; }
    if(a.conf === "sure") r.sureWrong++;
    if(a.at > r.lastAt){ r.lastAt = a.at; r.last = {q:q.q, chose:a.chose != null ? q.o[a.chose] : null, key:q.o[q.a]}; }
  });
  // Before this build the app kept per-question totals only, so old questions contribute their totals.
  BIO13_Q.forEach(q=>{
    const p = S.bankProg[q.id]; if(!p || logged.has(q.id) || !(p.seen || p.rev)) return;
    const r = g(q.topic);
    r.n += p.seen || 0; r.ok += p.ok || 0; r.rev += p.rev || 0; r.old += p.seen || 0;
    const c = (p.conf || {}).sure; if(c) r.sureWrong += (c.n - c.ok);
    if(p.last === "wrong" && p.choice != null && r.lastAt < 0 && !r.last) r.last = {q:q.q, chose:q.o[p.choice], key:q.o[q.a]};
  });
  return Object.values(G).filter(r=>r.n || r.rev).map(r=> Object.assign(r, {
    pct: r.n ? Math.round(r.ok / r.n * 100) : 0,
    sw: r.n ? Math.round(r.sureWrong / r.n * 100) : 0,
    score: (r.n - r.ok) + r.sureWrong + r.rev * 0.5      // a Sure-but-wrong counts double
  })).sort((a,b)=> b.score - a.score || a.pct - b.pct);
}
function doubtSheetMd(){
  const rows = doubtSheetRows();
  return "# BIO 0013 Exam 1 Doubt Sheet\n\nGenerated " + new Date().toISOString().slice(0,16).replace("T"," ") +
    " from every attempt, old bank and new. Worst first. A Sure answer that was wrong counts double.\n\n" +
    rows.map((r,i)=> "## " + (i+1) + ". " + r.topic + "\n\n- Seen " + r.n + " times, " + r.pct + "% correct, " + r.sw +
      "% Sure but wrong" + (r.rev ? ", revealed " + r.rev + " times" : "") + (r.old ? " (" + r.old + " from the retired bank, totals only)" : "") +
      (r.last && r.last.chose ? "\n- Last wrong answer: \"" + r.last.chose + "\"\n- Correct: \"" + r.last.key + "\"\n- On: " + r.last.q.replace(/\n+/g," ").slice(0,220) : "")
    ).join("\n\n") + "\n";
}
function renderDoubtSheet(){
  const rows = doubtSheetRows();
  const body = rows.length ? rows.map((r,i)=>{
    const col = r.pct < 50 ? "var(--again)" : r.pct < 80 ? "var(--hard)" : "var(--easy)";
    return '<div class="res-q"><div class="res-top"><span class="mark '+(r.pct<50?"no":r.pct<80?"part":"ok")+'">'+(i+1)+'</span>'+
      '<span class="rq"><em>seen '+r.n+' · <b style="color:'+col+'">'+r.pct+'% right</b> · '+r.sw+'% Sure but wrong'+(r.rev?' · revealed '+r.rev:'')+(r.old?' · '+r.old+' from retired bank':'')+'</em>'+
      '<b>'+esc(r.topic)+'</b></span></div>'+
      (r.last && r.last.chose ? '<div class="res-body"><div class="ab"><b>Last wrong</b><span class="nope">'+esc(r.last.chose)+'</span></div>'+
        '<div class="ab"><b>Correct</b><span class="yes">'+esc(r.last.key)+'</span></div></div>' : '')+
    '</div>';
  }).join("") : '<div class="note">No attempts yet. Answer some questions and this fills in.</div>';
  paneCard.innerHTML = '<div class="test-wrap">'+
    '<div class="scorehead"><b>'+rows.length+'</b><span>concepts, worst first. Every BIO 13 attempt counts, old bank and new. A Sure answer that was wrong counts double.</span></div>'+
    '<div class="navrow"><button class="btn-primary" id="ds-save">Save Doubt Sheet</button></div>'+body+'</div>';
  document.getElementById("ds-save").onclick = async ()=>{
    const md = doubtSheetMd(), name = "BIO 0013 Doubt Sheet - " + new Date().toISOString().slice(0,10) + ".md";
    let dl = null; try{ dl = await window.claude?.use?.("downloads"); }catch(e){}
    if(dl){ try{ await dl.save({filename:name, data:md}); toast("Saved " + name); return; }catch(e){ if(e && e.code === "declined") return; } }
    try{ await navigator.clipboard.writeText(md); toast("Download unavailable here, so the Doubt Sheet is on your clipboard."); }
    catch(e){ openModal("Doubt Sheet", '<textarea style="min-height:320px;width:100%">'+esc(md)+'</textarea>'); }
  };
  lockChat("The Doubt Sheet ranks every BIO 13 concept by how often it costs you points.");
}
