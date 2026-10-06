"""Tier 3: the 8 EASY stems, 9 questions (Q3, Q4, Q5 x2, Q13, Q16, Q17, Q18, Q20)."""
import os
import figs
from rdkit import Chem
from rdkit.Chem import rdDepictor
from rdkit.Chem.Draw import rdMolDraw2D
from rdkit.Chem.rdMolDescriptors import CalcMolFormula

Q = []


def add(stem, vi, vn, week, lo, topic, q, o, a, why, om, fig=None, alt=""):
    assert len(o) == len(om) and 4 <= len(o) <= 5 and 0 <= a < len(o)
    d = dict(id=f"v2-q{stem}-{vi}", stem=stem, level="easy", vi=vi, vn=vn, week=week, lo=lo, topic=topic,
             q=q, o=o, a=a, why=why, om=om)
    if fig:
        d["fig"] = {"src": "fig/v2/" + fig.split("/fig/v2/")[1], "alt": alt}
    Q.append(d)


add(3, 1, 1, 1, "W1: electronegativity, polarity, hydrophilic/hydrophobic", "Water and ions",
    "When table salt dissolves, water molecules cluster around each sodium ion (Na+) with their oxygen atoms pointing toward it. "
    "Which feature of a water molecule allows it to form this attraction with ions?",
    ["Water forms ionic bonds with Na+",
     "Water carries a net negative charge",
     "Oxygen is more electronegative than hydrogen, so water's oxygen carries a partial negative charge that is attracted to the positive ion",
     "Water is a linear molecule, so its charges point outward",
     "Water's hydrogen atoms carry partial negative charges"],
    2,
    "Water is polar: oxygen pulls the shared electrons toward itself, so the O end is partly negative and the H ends are partly positive. "
    "The partly negative oxygen is attracted to Na+ (and the partly positive hydrogens to Cl-). Water is bent and has no net charge.",
    ["Trap: water has no full charge, so it cannot form an ionic bond. This is an attraction between a partial charge and an ion.",
     "Net-charge trap: water is neutral overall. The charges are partial and uneven.",
     "Correct. Polarity from electronegativity.",
     "Water is bent, not linear. A linear molecule with this bond pattern would cancel its polarity.",
     "Backwards: the hydrogens are partly positive."])

ALK = [("X", "CCCCC"), ("Y", "CCC(C)C"), ("Z", "CC(C)(C)C")]
mols = []
for n, smi in ALK:
    m = Chem.MolFromSmiles(smi)
    assert CalcMolFormula(m) == "C5H12", n
    rdDepictor.Compute2DCoords(m)
    mols.append(m)
d = rdMolDraw2D.MolDraw2DSVG(780, 240, 260, 240)
o = d.drawOptions(); o.clearBackground = True; o.bondLineWidth = 2; o.legendFontSize = 20
d.DrawMolecules(mols, legends=["Hydrocarbon X", "Hydrocarbon Y", "Hydrocarbon Z"])
d.FinishDrawing()
p4 = os.path.join(figs.FIG, "q4-1.svg"); open(p4, "w").write(d.GetDrawingText())
add(4, 1, 1, 1, "W1: covalent vs ionic vs hydrogen bonds vs London dispersion forces", "Boiling point and dispersion forces",
    "Hydrocarbons X, Y and Z (drawn below) all have the formula C5H12 and are nonpolar. Their boiling points fall from X (36 °C) to "
    "Y (28 °C) to Z (10 °C). Which best explains this trend?",
    ["The more branched molecules form fewer hydrogen bonds with each other",
     "Boiling breaks C-H bonds, and branching weakens them",
     "The straighter the molecule, the more surface it shares with its neighbours, so more London dispersion forces must be overcome to boil it",
     "The more branched molecules are lighter",
     "The more branched molecules are more polar"],
    2,
    "All three are nonpolar, so the only attractions between molecules are London dispersion forces. A straight chain lies alongside its "
    "neighbours over a long surface; a compact, branched molecule touches less. Less contact, weaker dispersion forces, lower boiling point.",
    ["Hydrocarbons have no O-H or N-H, so they form no hydrogen bonds at all.",
     "Boiling separates molecules from each other. It breaks no covalent bonds.",
     "Correct. Shape changes surface contact, which changes dispersion forces.",
     "Same formula, same mass.",
     "C-H bonds are nonpolar; branching does not make the molecule polar."],
    p4, "Three skeletal structures, all C5H12: X is a straight five-carbon chain; Y has one branch; Z is a central carbon with four methyl groups.")

LO5 = "W2: condensation vs hydrolysis; four macromolecules"
add(5, 1, 2, 2, LO5, "Digestion: hydrolysis and water",
    "A student writes: \"When we digest proteins, the peptide bonds are broken by hydrolysis, which is why digestion uses up water.\" "
    "Which is the best evaluation of this statement?",
    ["Correct in every part",
     "Incorrect: peptide bonds are broken by condensation, which releases water",
     "Incorrect: amino acids in proteins are joined by glycosidic linkages",
     "Incorrect: hydrolysis releases water, so digestion produces water"],
    0,
    "Proteins are amino acids joined by peptide bonds. Digestion splits them by hydrolysis, which adds a water molecule across each bond, "
    "so water is used up. Condensation is the reverse: it builds the bond and releases water.",
    ["Correct. Every slot is right.",
     "Swapped the reactions: condensation builds polymers and releases water.",
     "Glycosidic linkages join sugars, not amino acids.",
     "Hydrolysis consumes water; condensation releases it."])

add(5, 2, 2, 2, LO5, "Digestion: hydrolysis and water",
    "A student writes: \"When we digest starch, the glycosidic linkages are broken by condensation, which is why digestion uses up "
    "water.\" Which is the best evaluation of this statement?",
    ["Correct in every part",
     "One error: the linkages are broken by hydrolysis, not condensation; the rest is correct",
     "One error: starch is held together by peptide bonds, not glycosidic linkages",
     "One error: digestion releases water rather than using it up"],
    1,
    "Starch is glucose joined by glycosidic linkages, and digestion does use up water. The wrong slot is the reaction: breaking a bond "
    "while adding water is hydrolysis. Condensation is the building reaction, and it releases water.",
    ["The reaction slot is wrong: condensation builds bonds.",
     "Correct. Only the reaction name is wrong.",
     "Starch is a polysaccharide; its linkages are glycosidic.",
     "Digestion by hydrolysis consumes water, so this slot was right."])

p = figs.table("q13-1", ["Virus", "A", "T", "G", "C", "U"],
               [["1", "20", "20", "30", "30", "0"], ["2", "25", "0", "25", "25", "25"], ["3", "30", "15", "22", "33", "0"]],
               note="Base composition, % of all bases")
add(13, 1, 1, 2, "W2: nucleotides and nucleic acids; DNA vs RNA", "Reading base composition",
    "Researchers isolate the genomes of three newly discovered viruses and measure their base composition (%) to determine what kind of "
    "nucleic acid each genome is. The data are in the table below.\n\nWhich conclusion is best supported by these data?",
    ["Virus 1 is double-stranded DNA, virus 2 is double-stranded RNA, and virus 3 is single-stranded DNA",
     "Virus 2 must be single-stranded, because RNA is always single-stranded",
     "Virus 3 has more genes than virus 1, because it has more C",
     "Virus 1 is single-stranded, because its A does not equal its G",
     "Virus 2 is DNA, because its A equals its U"],
    0,
    "T means DNA, U means RNA. In a double strand every base has a partner, so A = T (or A = U) and G = C. Virus 1: DNA, A = T and G = C, "
    "double-stranded. Virus 2: RNA, A = U and G = C, double-stranded RNA. Virus 3: DNA, but A does not equal T, so single-stranded.",
    ["Correct. Use T or U for DNA or RNA, then A = T (or U) and G = C for double strands.",
     "RNA can be double-stranded; A = U and G = C point to dsRNA here.",
     "Over-claim: base percentages say nothing about how many genes a genome has.",
     "The pairing rule is A = T and G = C, not A = G.",
     "DNA has T, not U. A virus with U is RNA."],
    p, "Table of base composition (%): virus 1 A 20, T 20, G 30, C 30, U 0; virus 2 A 25, T 0, G 25, C 25, U 25; virus 3 A 30, T 15, G 22, C 33, U 0.")

add(16, 1, 1, 3, "W3: carbohydrate functions", "Carbohydrate functions",
    "Which of the following is NOT a function of carbohydrates?",
    ["Storing glucose in liver and muscle cells as glycogen",
     "Forming part of the A and B blood-type markers on red blood cells",
     "Catalyzing chemical reactions as enzymes",
     "Providing structural support in plant cell walls as cellulose"],
    2,
    "Carbohydrates store energy (glycogen in animals, starch in plants), build structures (cellulose) and mark cell surfaces (the sugars of "
    "the A and B blood types). Catalysis is a job for proteins (enzymes).",
    ["Decoy: this one is true. Animals store glycogen in liver and muscle; plants store starch.",
     "True: A and B blood types are sugars on the cell surface.",
     "Correct (NOT a function). Enzymes are proteins.",
     "True: cellulose is a structural polysaccharide."])

add(17, 1, 1, 3, "W3: predict whether and how a substance crosses a membrane", "Crossing the membrane",
    "A steroid hormone normally crosses the plasma membrane on its own and binds a receptor inside target cells. Chemists attach a "
    "charged phosphate group to the hormone, hoping to make it dissolve better in blood. What effect would this change most likely have?",
    ["It crosses the membrane faster, because it is more soluble",
     "No change: steroids cross membranes whatever groups are attached",
     "It dissolves better in blood but can no longer cross the membrane on its own, so it cannot reach its receptor and loses its effect",
     "It binds its receptor more tightly, because charged groups attract"],
    2,
    "A steroid crosses the membrane because it is nonpolar and can dissolve through the hydrophobic interior of the bilayer. A charged "
    "group makes it more water-soluble but blocks it from passing through that hydrophobic core, so it cannot reach a receptor inside the cell.",
    ["Soluble in water is the opposite of what crosses the bilayer's hydrophobic core.",
     "A charge changes everything: charged molecules cannot cross the bilayer unaided.",
     "Correct. Better in blood, stuck outside the cell.",
     "It never reaches the receptor, which is inside the cell."])

add(18, 1, 1, 3, "W3: predict whether and how a substance crosses a membrane", "Osmosis",
    "In winter, salt spread on roads washes into the soil beside the road. Plants growing along the road wilt, even though the soil is "
    "wet. Which is the best explanation?",
    ["The soil water is hypertonic to the root cells, so water leaves the cells by osmosis",
     "Salt diffuses into the root cells and makes them burst",
     "The soil water is hypotonic to the root cells, so water rushes in and the cells burst",
     "The salt blocks water from moving in either direction across the membrane",
     "Salt pulls water out of the cells by forming ionic bonds with it"],
    0,
    "Salty soil water has more dissolved solute than the fluid inside the root cells: it is hypertonic. Water moves by osmosis toward the "
    "higher solute concentration, so it leaves the cells, they lose pressure, and the plant wilts despite wet soil.",
    ["Correct. Hypertonic outside, water moves out.",
     "Ions do not cross the membrane freely, and wilting means cells lost water, not burst.",
     "Backwards: salty water is hypertonic, not hypotonic.",
     "Water still moves; it moves out.",
     "Water and ions attract, but they do not form ionic bonds; osmosis explains the water movement."])

add(20, 1, 1, 4, "W4: thermodynamics and spontaneity", "Entropy",
    "Which of the following processes DECREASES the entropy of the system?",
    ["ATP + H2O → ADP + Pi",
     "Sugar dissolving in water",
     "A cell pumping H+ ions across a membrane to build a concentration gradient",
     "Starch being hydrolyzed into glucose",
     "A protein folding in water, counting the protein and the surrounding water together as the system"],
    2,
    "Building a gradient packs ions on one side: more order, lower entropy (course fact). The others spread things out: one molecule "
    "becomes several, a solid disperses, a polymer breaks into monomers. Folding orders the chain but frees much more water, so with water "
    "counted, entropy rises.",
    ["One molecule becomes two (plus water used): entropy increases.",
     "Dissolving spreads molecules out: entropy increases.",
     "Correct. A gradient is order.",
     "One polymer becomes many monomers: entropy increases.",
     "Folding nuance: the chain gets more ordered, but the freed water gains more, so overall entropy increases."])

if __name__ == "__main__":
    import json, collections
    c = collections.Counter(q["stem"] for q in Q)
    print(len(Q), dict(c))
    assert dict(c) == {3: 1, 4: 1, 5: 2, 13: 1, 16: 1, 17: 1, 18: 1, 20: 1}
    for q in Q:
        assert q["vn"] == c[q["stem"]]
        txt = q["q"] + " ".join(q["o"]) + q["why"] + " ".join(q["om"])
        assert "—" not in txt and "–" not in txt, q["id"]
    json.dump(Q, open("build/easy.json", "w"), ensure_ascii=False, indent=1)
    for q in Q:
        if "fig" in q:
            figs.png_of(figs.FIG + "/" + q["fig"]["src"].split("/")[-1])
    print("ok")
