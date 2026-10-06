"""Figure generators for the BIO 13 Exam 1 bank rebuild.

Molecules: RDKit. Peptides and amino acids come from RDKit's own residue
library (Chem.MolFromSequence), so no SMILES are hand-typed for them.
Sugars are built from SMILES and checked: molecular formula, ring size,
carbon count and whether the anomeric carbon carries an H.
Gels and energy diagrams: SVG drawn from the question's own data object.
Every SVG is also rendered to PNG in preview/ so it can be looked at.
"""
import math, os, re
import cairosvg
from rdkit import Chem
from rdkit.Chem import AllChem, Draw, rdDepictor
from rdkit.Chem.Draw import rdMolDraw2D
from rdkit.Chem.rdMolDescriptors import CalcMolFormula

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIG = os.path.join(ROOT, "fig", "v2")
PREV = os.path.join(ROOT, "preview")
os.makedirs(FIG, exist_ok=True); os.makedirs(PREV, exist_ok=True)
rdDepictor.SetPreferCoordGen(True)

# Free amino acid formulas (neutral form). Used to cross-check RDKit's residue library.
AA_FORMULA = {
    "G": "C2H5NO2", "A": "C3H7NO2", "S": "C3H7NO3", "C": "C3H7NO2S", "V": "C5H11NO2",
    "L": "C6H13NO2", "F": "C9H11NO2", "K": "C6H14N2O2", "R": "C6H14N4O2",
    "D": "C4H7NO4", "E": "C5H9NO4", "Q": "C5H10N2O3", "T": "C4H9NO3", "N": "C4H8N2O3",
}
AA_NAME = {"G": "Glycine", "A": "Alanine", "S": "Serine", "C": "Cysteine", "V": "Valine",
           "L": "Leucine", "F": "Phenylalanine", "K": "Lysine", "R": "Arginine",
           "D": "Aspartate", "E": "Glutamate", "Q": "Glutamine", "T": "Threonine", "N": "Asparagine"}


def _parse(f):
    return {el: int(n or 1) for el, n in re.findall(r"([A-Z][a-z]?)(\d*)", f)}


def _fmt(c):
    order = ["C", "H"] + sorted(k for k in c if k not in ("C", "H"))
    return "".join(k + (str(c[k]) if c[k] != 1 else "") for k in order if c.get(k))


def expected_peptide_formula(seq):
    tot = {}
    for r in seq:
        for el, n in _parse(AA_FORMULA[r]).items():
            tot[el] = tot.get(el, 0) + n
    tot["H"] -= 2 * (len(seq) - 1); tot["O"] -= (len(seq) - 1)  # one water lost per peptide bond
    return _fmt(tot)


def png_of(svg_path):
    out = os.path.join(PREV, os.path.basename(svg_path).replace(".svg", ".png"))
    cairosvg.svg2png(url=svg_path, write_to=out, output_width=900, background_color="white")
    return out


def _mol_svg(mol, w, h, labels=None, legend="", bond=None):
    d = rdMolDraw2D.MolDraw2DSVG(w, h)
    o = d.drawOptions()
    if bond:
        o.fixedBondLength = bond
        o.fixedFontSize = 20
    o.clearBackground = True
    o.bondLineWidth = 2
    o.minFontSize = 15
    o.addStereoAnnotation = False
    if labels:
        for idx, lab in labels.items():
            o.atomLabels[idx] = lab
    rdMolDraw2D.PrepareAndDrawMolecule(d, mol, legend=legend)
    d.FinishDrawing()
    return d.GetDrawingText()


def peptide(name, seq):
    mol = Chem.MolFromSequence(seq)
    got, want = CalcMolFormula(mol), expected_peptide_formula(seq)
    assert got == want, f"{name}: formula {got} != expected {want}"
    # Bond-line, neutral form, free amino and carboxyl ends drawn by RDKit as NH2 / OH.
    rdDepictor.Compute2DCoords(mol)
    svg = _mol_svg(mol, 620, 300)
    path = os.path.join(FIG, name + ".svg")
    open(path, "w").write(svg)
    return path, got


def amino_panel(name, letters):
    """Named amino acids, alphabetical, neutral form, no class labels."""
    letters = sorted(set(letters), key=lambda x: AA_NAME[x])
    mols, legends = [], []
    for L in letters:
        m = Chem.MolFromSequence(L)
        assert CalcMolFormula(m) == AA_FORMULA[L], (L, CalcMolFormula(m))
        rdDepictor.Compute2DCoords(m)
        mols.append(m); legends.append(AA_NAME[L])
    per = min(len(mols), 4)
    d = rdMolDraw2D.MolDraw2DSVG(280 * per, 260 * math.ceil(len(mols) / per), 280, 260)
    o = d.drawOptions(); o.clearBackground = True; o.bondLineWidth = 2; o.legendFontSize = 20; o.minFontSize = 15
    d.DrawMolecules(mols, legends=legends)
    d.FinishDrawing()
    path = os.path.join(FIG, name + ".svg")
    open(path, "w").write(d.GetDrawingText())
    return path, [AA_NAME[L] for L in letters]


def sugar(name, smiles, formula, ring_size, n_carbons, anomeric_has_h):
    mol = Chem.MolFromSmiles(smiles)
    assert CalcMolFormula(mol) == formula, (name, CalcMolFormula(mol), formula)
    ri = mol.GetRingInfo()
    assert ri.NumRings() == 1 and len(ri.AtomRings()[0]) == ring_size, (name, "ring size")
    assert sum(1 for a in mol.GetAtoms() if a.GetSymbol() == "C") == n_carbons, (name, "carbon count")
    ring = ri.AtomRings()[0]
    ring_o = [i for i in ring if mol.GetAtomWithIdx(i).GetSymbol() == "O"][0]
    # anomeric carbon: ring carbon bonded to the ring O and to an exocyclic OH
    anom = None
    for nb in mol.GetAtomWithIdx(ring_o).GetNeighbors():
        if any(x.GetSymbol() == "O" and x.GetIdx() not in ring for x in nb.GetNeighbors()):
            anom = nb
    assert anom is not None, (name, "no anomeric carbon")
    assert (anom.GetTotalNumHs() == 1) == anomeric_has_h, (name, "anomeric H")
    # Label every carbon with its hydrogens so the anomeric H (or its absence) is visible.
    labels = {}
    for a in mol.GetAtoms():
        if a.GetSymbol() == "C":
            h = a.GetTotalNumHs()
            labels[a.GetIdx()] = "C" if h == 0 else ("CH" if h == 1 else "CH<sub>2</sub>")
    rdDepictor.Compute2DCoords(mol)
    svg = _mol_svg(mol, 560, 460, labels=labels, bond=62)
    path = os.path.join(FIG, name + ".svg")
    open(path, "w").write(svg)
    return path


# ---------------- SDS-PAGE gel ----------------
LADDER = [50, 40, 30, 25, 20, 15, 10, 5]


def gel(name, lanes):
    """lanes: dict letter -> list of kDa sizes. One band per distinct size."""
    W, H = 560, 420
    top, bot = 50, 380
    lo, hi = math.log10(4), math.log10(60)

    def y(k):
        return top + (hi - math.log10(k)) / (hi - lo) * (bot - top)
    cols = ["Ladder"] + list(lanes.keys())
    lw, x0 = 70, 90
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" font-family="Helvetica, Arial, sans-serif">',
         f'<rect width="{W}" height="{H}" fill="#ffffff"/>',
         f'<rect x="{x0-12}" y="{top-14}" width="{len(cols)*lw+4}" height="{bot-top+30}" fill="#eef1f3" stroke="#9aa7ad"/>']
    for i, c in enumerate(cols):
        cx = x0 + i * lw + lw / 2 - 10
        s.append(f'<text x="{cx}" y="{top-22}" font-size="16" text-anchor="middle" fill="#222">{c if c != "Ladder" else "MW"}</text>')
        s.append(f'<rect x="{cx-24}" y="{top-12}" width="48" height="8" fill="#c9d1d5"/>')  # well
    for k in LADDER:
        cx = x0 + lw / 2 - 10
        s.append(f'<rect x="{cx-22}" y="{y(k)-2.5:.1f}" width="44" height="5" rx="1.5" fill="#6b7b83"/>')
        s.append(f'<text x="{x0-18}" y="{y(k)+5:.1f}" font-size="14" text-anchor="end" fill="#333">{k}</text>')
    s.append(f'<text x="18" y="{(top+bot)/2}" font-size="13" fill="#333" transform="rotate(-90 18 {(top+bot)/2})" text-anchor="middle">kDa</text>')
    for i, (lane, sizes) in enumerate(lanes.items(), start=1):
        cx = x0 + i * lw + lw / 2 - 10
        assert len(set(sizes)) == len(sizes), (name, lane, "duplicate band")
        for k in sizes:
            assert 5 <= k <= 50, (name, k)
            s.append(f'<rect x="{cx-22}" y="{y(k)-3.5:.1f}" width="44" height="7" rx="2" fill="#1d2b33"/>')
    s.append("</svg>")
    path = os.path.join(FIG, name + ".svg")
    open(path, "w").write("\n".join(s))
    return path


# ---------------- reaction coordinate diagrams ----------------
def energy(name, diagrams, ymax=160):
    """diagrams: list of dicts {r, ts, p}, all on one shared free-energy axis."""
    pw, ph = 230, 260
    W, H = 70 + pw * len(diagrams) + 20, ph + 110
    top, bot = 30, 30 + ph

    def y(g):
        return bot - g / ymax * ph
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" font-family="Helvetica, Arial, sans-serif">',
         f'<rect width="{W}" height="{H}" fill="#ffffff"/>']
    for g in range(0, ymax + 1, 20):
        s.append(f'<line x1="60" x2="{W-20}" y1="{y(g):.1f}" y2="{y(g):.1f}" stroke="#e3e8ea"/>')
        s.append(f'<text x="54" y="{y(g)+5:.1f}" font-size="13" text-anchor="end" fill="#333">{g}</text>')
    s.append(f'<line x1="60" x2="60" y1="{top}" y2="{bot}" stroke="#333" stroke-width="1.5"/>')
    s.append(f'<text x="16" y="{(top+bot)/2}" font-size="14" fill="#333" transform="rotate(-90 16 {(top+bot)/2})" text-anchor="middle">Free energy (G)</text>')
    for i, d in enumerate(diagrams):
        x0 = 70 + i * pw
        xs, xe, xm = x0 + 18, x0 + pw - 28, x0 + pw / 2 - 5
        r, ts, p = y(d["r"]), y(d["ts"]), y(d["p"])
        assert d["ts"] > max(d["r"], d["p"]), (name, i, "peak must be above both ends")
        s.append(f'<line x1="{x0+4}" x2="{x0+4}" y1="{top}" y2="{bot}" stroke="#cfd8dc" stroke-dasharray="3 4"/>' if i else "")
        path = (f'M{xs},{r:.1f} L{xs+28},{r:.1f} C{xs+58},{r:.1f} {xm-30},{ts:.1f} {xm},{ts:.1f} '
                f'C{xm+30},{ts:.1f} {xe-58},{p:.1f} {xe-28},{p:.1f} L{xe},{p:.1f}')
        s.append(f'<path d="{path}" fill="none" stroke="#0e5f68" stroke-width="3"/>')
        s.append(f'<text x="{xs+2}" y="{r-8:.1f}" font-size="13" fill="#222">R {d["r"]}</text>')
        s.append(f'<text x="{xe-2}" y="{p-8:.1f}" font-size="13" text-anchor="end" fill="#222">P {d["p"]}</text>')
        s.append(f'<text x="{xm}" y="{ts-8:.1f}" font-size="13" text-anchor="middle" fill="#222">peak {d["ts"]}</text>')
        s.append(f'<text x="{xm}" y="{bot+30}" font-size="17" font-weight="bold" text-anchor="middle" fill="#111">{i+1}</text>')
        s.append(f'<text x="{xm}" y="{bot+50}" font-size="12" text-anchor="middle" fill="#666">reaction progress</text>')
    s.append(f'<text x="70" y="{H-8}" font-size="12" fill="#666">R = reactants, P = products. All four share one y axis.</text>')
    s.append("</svg>")
    path = os.path.join(FIG, name + ".svg")
    open(path, "w").write("\n".join(x for x in s if x))
    return path


def molecule(name, smiles, formula):
    """Unnamed (invented) molecule from SMILES, neutral form, with a formula assert."""
    mol = Chem.MolFromSmiles(smiles)
    assert CalcMolFormula(mol) == formula, (name, CalcMolFormula(mol), formula)
    rdDepictor.Compute2DCoords(mol)
    path = os.path.join(FIG, name + ".svg")
    open(path, "w").write(_mol_svg(mol, 560, 300))
    return path


def table(name, head, rows, note=""):
    """Plain data table as SVG, so the numbers in the picture come from the question's own data."""
    cw = [max(len(str(r[i])) for r in [head] + rows) * 11 + 34 for i in range(len(head))]
    W, rh = sum(cw) + 20, 40
    H = rh * (len(rows) + 1) + 20 + (26 if note else 0)
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" font-family="Helvetica, Arial, sans-serif">',
         f'<rect width="{W}" height="{H}" fill="#ffffff"/>']
    y = 10
    for ri, r in enumerate([head] + rows):
        x = 10
        if ri == 0:
            s.append(f'<rect x="10" y="{y}" width="{W-20}" height="{rh}" fill="#e9eef0"/>')
        for i, c in enumerate(r):
            fam = "Courier New, monospace" if "5'" in str(c) else "Helvetica, Arial, sans-serif"
            wt = "bold" if ri == 0 else "normal"
            txt = str(c).replace("&", "&amp;")
            s.append(f'<text x="{x+12}" y="{y+26}" font-size="17" font-weight="{wt}" fill="#111" font-family="{fam}">{txt}</text>')
            x += cw[i]
        s.append(f'<line x1="10" x2="{W-10}" y1="{y+rh}" y2="{y+rh}" stroke="#c5cfd3"/>')
        y += rh
    if note:
        s.append(f'<text x="12" y="{y+20}" font-size="13" fill="#555">{note}</text>')
    s.append("</svg>")
    path = os.path.join(FIG, name + ".svg")
    open(path, "w").write("\n".join(s))
    return path
