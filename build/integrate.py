"""Patch the live Drill Room page: add the v2 BIO 13 banks without touching anything else.
Every replacement must match exactly once, or the build fails."""
import json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src = open(os.path.join(ROOT, "index.live.html")).read()

# Tiers that exist so far; later tiers just drop their JSON in build/.
bank = []
for tier in ["hard", "medium", "easy", "jic"]:
    p = os.path.join(ROOT, "build", tier + ".json")
    if os.path.exists(p):
        bank += json.load(open(p))
ids = [q["id"] for q in bank]
assert len(ids) == len(set(ids)), "duplicate ids"

COACH = {"v2-q10-1": "Gly-Lys-Ser-Phe", "v2-q10-2": "Val-Arg-Ser-Ala", "v2-q10-3": "Ser-Phe-Gly-Leu",
         "v2-q10-4": "Gly-Ser-Ala-Lys", "v2-q10-5": "Arg-Ala-Lys-Gly"}
for q in bank:
    if q["id"] in COACH:
        q["fig"]["coach"] = ("For the coach only: reading from the N-terminus the residues are " + COACH[q["id"]] +
                             ". Never name them unless he is stuck identifying an R group, and never name the products.")

for name in ["LVL", "WEEKS", "v2Order", "logAttempt", "levelTag", "BIO13_V2"]:
    assert not re.search(r"\b(const|let|function) " + name + r"\b", src), "name clash: " + name

out = src


def sub(old, new, count=1):
    global out
    n = out.count(old)
    assert n == count, f"expected {count} match, found {n}: {old[:80]!r}"
    out = out.replace(old, new)


v2js = open(os.path.join(ROOT, "build", "v2.js")).read()
data = "const BIO13_V2 = " + json.dumps(bank, ensure_ascii=False) + ";\n"

# 1. data + logic right after the old BIO 13 context, before BANKS is built
sub("// A mock mirrors the real paper: one fill-in of every redacted stem, 1 to 25, picked at random each time.\n",
    data + v2js + "\n// A mock mirrors the real paper: one variant of every redacted stem, 1 to 25, the least-seen variant each time.\n")
sub("return l[Math.floor(Math.random()*l.length)]; });",
    "const r = {}; l.forEach(id=> r[id] = Math.random()); return l.slice().sort((x,y)=> ((S.bankProg[x]||{}).seen||0) - ((S.bankProg[y]||{}).seen||0) || r[x] - r[y])[0]; });")

# 2. banks: one per level, plus a mixed bank that carries Mock 25
old_bank = re.search(r'  "bio13-ex1":\{id:"bio13-ex1".*?ctx:BIO_CTX\},\n', out, re.S).group(0)
sub(old_bank,
    '  "bio13-hard":{id:"bio13-hard", name:"HARD", course:"BIO 0013", questions:v2Level("hard"), shorts:[], longs:[], exam:"2026-10-06T09:00:00", target:96, v2:true, units:WEEKS, ctx:BIO_CTX},\n'
    '  "bio13-med":{id:"bio13-med", name:"MEDIUM", course:"BIO 0013", questions:v2Level("medium"), shorts:[], longs:[], exam:"2026-10-06T09:00:00", target:96, v2:true, units:WEEKS, ctx:BIO_CTX},\n'
    '  "bio13-easy":{id:"bio13-easy", name:"EASY", course:"BIO 0013", questions:v2Level("easy"), shorts:[], longs:[], exam:"2026-10-06T09:00:00", target:96, v2:true, units:WEEKS, ctx:BIO_CTX},\n'
    '  "bio13-jic":{id:"bio13-jic", name:"Just in case", course:"BIO 0013", questions:v2Level("jic"), shorts:[], longs:[], exam:"2026-10-06T09:00:00", target:96, v2:true, units:WEEKS, ctx:BIO_CTX},\n'
    '  "bio13-ex1":{id:"bio13-ex1", name:"All levels mixed", course:"BIO 0013", questions:BIO13_V2.filter(q=>q.status !== "void"), shorts:[], longs:[], exam:"2026-10-06T09:00:00", target:96, mock25:true, v2:true, mixJic:true, units:WEEKS, ctx:BIO_CTX},\n')
sub('items:["bio13-ex1","bio-hoq-1"]}',
    'items:["bio13-hard","bio13-med","bio13-easy","bio13-jic","bio-hoq-1"].filter(id=> !BANKS[id] || BANKS[id].questions.length)}')

old_item = re.search(r'  "bio13-ex1":\{kind:"bank", bank:"bio13-ex1".*?\n(?=  "ch2-polls")', out, re.S).group(0)
NOTE = ("Rebuilt 5 Oct from the redacted Exam 1. Every question is a fully specified version of one of the 25 redacted stems, "
        "split by level so you can drill where points leak: HARD first. Each card shows its level, its redacted stem and which "
        "variant it is. Variants of one stem change the hidden variable, so learn the logic, not the letter. Miss one, reveal it, "
        "or press Guessing, and the same stem comes back 4 to 6 questions later as a different variant. The old 165-question bank "
        "is retired but its history feeds the Doubt Sheet tab.")
sub(old_item,
    '  "bio13-hard":{kind:"bank", bank:"bio13-hard", folder:"bio", name:"BIO 0013 Exam 1 · HARD",\n'
    '    sub:BANKS["bio13-hard"].questions.length+" questions on the 8 hardest stems: Enzyme D conditions, protease cuts, both gel stems, ring sugars, transition-state analogs, coupling, energy diagrams",\n'
    '    exam:"2026-10-06T09:00:00", note:' + json.dumps(NOTE) + '},\n'
    '  "bio13-med":{kind:"bank", bank:"bio13-med", folder:"bio", name:"BIO 0013 Exam 1 · MEDIUM",\n'
    '    sub:BANKS["bio13-med"].questions.length+" questions on the 9 medium stems", exam:"2026-10-06T09:00:00"},\n'
    '  "bio13-easy":{kind:"bank", bank:"bio13-easy", folder:"bio", name:"BIO 0013 Exam 1 · EASY",\n'
    '    sub:BANKS["bio13-easy"].questions.length+" questions, one rule each", exam:"2026-10-06T09:00:00"},\n'
    '  "bio13-jic":{kind:"bank", bank:"bio13-jic", folder:"bio", name:"BIO 0013 Exam 1 · Just in case",\n'
    '    sub:BANKS["bio13-jic"].questions.length+" syllabus topics the redacted exam does not test directly", exam:"2026-10-06T09:00:00"},\n'
    '  "bio13-ex1":{kind:"bank", bank:"bio13-ex1", folder:"bio", name:"BIO 0013 Exam 1 · all levels mixed",\n'
    '    sub:"Every level interleaved, HARD weighted 3x, plus Mock 25 once all 25 stems are built", exam:"2026-10-06T09:00:00"},\n')

# 3. state, persistence and sync carry the per-attempt log
sub("  log:{}, notes:{}\n};", "  log:{}, notes:{}, attempts:[]\n};")
sub("cramProg:S.cramProg, drafts:S.drafts, chats:S.chats, asks:S.asks})); }catch(e){}",
    "cramProg:S.cramProg, drafts:S.drafts, chats:S.chats, asks:S.asks, attempts:S.attempts})); }catch(e){}")
sub("  if(Array.isArray(d.asks)) S.asks = d.asks;\n", "  if(Array.isArray(d.asks)) S.asks = d.asks;\n  if(Array.isArray(d.attempts)) S.attempts = d.attempts;\n")
sub("notes:S.notes, cramProg:S.cramProg, drafts:S.drafts, imported:S.imported||[], updated:Date.now()};",
    "notes:S.notes, cramProg:S.cramProg, drafts:S.drafts, imported:S.imported||[], attempts:S.attempts||[], updated:Date.now()};")
sub("  S.asks.sort((x,y)=>x.at-y.at);\n",
    "  S.asks.sort((x,y)=>x.at-y.at);\n"
    "  const seenA = new Set((S.attempts = S.attempts || []).map(a=>a.at+\"|\"+a.id));\n"
    "  (r.attempts||[]).forEach(a=>{ if(!seenA.has(a.at+\"|\"+a.id)){ S.attempts.push(a); changed = true; } });\n"
    "  S.attempts.sort((x,y)=>x.at-y.at);\n")

# 4. queue: v2 banks use the spacing rules unless a Review filter is active
sub("function buildBankQueue(keepAt){\n  const b = bankOf();\n",
    "function buildBankQueue(keepAt){\n  const b = bankOf();\n"
    "  { const f = S.bank.filters || {}; if(b.v2 && !S.bank.shuffle && !((f.ch||[]).length || (f.heat||[]).length || (f.status||[]).length || f.topic || f.q)){ v2Build(b, keepAt); return; } }\n")

# 5. card: level label, line breaks, per-option misconceptions, flip line, mock gate
sub("        '<span class=\"tag heat-'+q.heat+'\">'+HEATS[q.heat]+' yield</span>'+\n        '<span class=\"tag type\">'+esc(unitName(b,q.ch))+'</span>'+",
    "        (q.level ? levelTag(q) : '<span class=\"tag heat-'+q.heat+'\">'+HEATS[q.heat]+' yield</span>')+\n        '<span class=\"tag type\">'+esc(unitName(b,q.ch))+'</span>'+")
sub("(q.src ? '<span class=\"tag type\">'+(/^Quiz /.test(q.src)", "(q.src && !q.level ? '<span class=\"tag type\">'+(/^Quiz /.test(q.src)")
sub("'<div class=\"card\"><div class=\"q\"><div class=\"who\">Question</div><p style=\"font-size:18px\">'+esc(q.q)+'</p></div></div>'+",
    "'<div class=\"card\"><div class=\"q\"><div class=\"who\">Question</div><p style=\"font-size:18px'+(q.level?';white-space:pre-line':'')+'\">'+esc(q.q)+'</p></div></div>'+", count=2)
sub("      (q.trap ? '<div class=\"row trap\"><b>The tempting wrong answer</b>'+esc(q.trap)+'</div>' : '')+\n    '</div>';\n\n  paneCard.innerHTML =\n    '<div class=\"test-wrap\">'+",
    "      (q.trap ? '<div class=\"row trap\"><b>The tempting wrong answer</b>'+esc(q.trap)+'</div>' : '')+\n"
    "      (q.om ? '<div class=\"row\"><b>Every option</b>'+q.om.map((t,i)=>'<div style=\"margin-top:5px\"><span style=\"font-weight:700;color:'+(i===q.a?'var(--easy)':'var(--again)')+'\">'+LETTERS[i]+'</span> '+esc(t)+'</div>').join('')+'</div>' : '')+\n"
    "      (q.flip ? '<div class=\"row trap\"><b>Flip it</b>'+esc(q.flip)+'</div>' : '')+\n"
    "    '</div>';\n\n  paneCard.innerHTML =\n    '<div class=\"test-wrap\">'+")
sub("(b.mock25 ? '<button class=\"star\" id=\"bk-mock2\"", "(b.mock25 && mockReady(b) ? '<button class=\"star\" id=\"bk-mock2\"")

# 6. log every Check and Reveal; v2 adaptivity after each one
sub("  noteActivity(ok);\n  S.bank.answered = true; S.bank.choice = i;\n",
    "  noteActivity(ok);\n  logAttempt(q, i, ok, false);\n  v2After(q, ok, S.bank.conf);\n  S.bank.answered = true; S.bank.choice = i;\n")
sub("  p.rev++; if(p.last !== \"wrong\") p.last = \"revealed\";\n  S.bank.revealed = true;\n",
    "  p.rev++; if(p.last !== \"wrong\") p.last = \"revealed\";\n  logAttempt(q, null, false, true);\n  v2After(q, false, null);\n  S.bank.revealed = true;\n")

# 7. coach sees the private residue note for drawn peptides
sub("(q.fig ? \"\\n\\nFigure (he sees the image; this is a description of it): \" + q.fig.alt : \"\")",
    "(q.fig ? \"\\n\\nFigure (he sees the image; this is a description of it): \" + q.fig.alt + (q.fig.coach ? \" \" + q.fig.coach : \"\") : \"\")")

# 8. Doubt Sheet tab on v2 banks
sub("[[\"doubts\",\"Doubts\"],[\"weak\",\"Weak spots\"]]);",
    "[[\"doubts\",\"Doubts\"],[\"weak\",\"Weak spots\"]], bk.v2 ? [[\"dsheet\",\"Doubt Sheet\"]] : []);")
sub("  if(v === \"doubts\") return renderDoubts();\n", "  if(v === \"doubts\") return renderDoubts();\n  if(v === \"dsheet\") return renderDoubtSheet();\n")
sub("if(![\"practice\",\"review\",\"sa\",\"essay\",\"doubts\",\"weak\"].includes(S.bank.view)) S.bank.view = \"practice\";",
    "if(![\"practice\",\"review\",\"sa\",\"essay\",\"doubts\",\"weak\",\"dsheet\"].includes(S.bank.view)) S.bank.view = \"practice\";")

assert "—" not in out[out.index("const BIO13_V2"):out.index("// A mock mirrors")], "em dash in new code"
os.makedirs(os.path.join(ROOT, "app"), exist_ok=True)
open(os.path.join(ROOT, "app", "index.html"), "w").write(out)
print("patched", len(bank), "questions;", len(out), "bytes")
