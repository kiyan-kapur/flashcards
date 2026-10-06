"""Tier 1: the 8 HARD stems, 33 questions (Q8 x4, Q10 x5, Q11 x3, Q12 x5, Q15 x5, Q22 x3, Q23 x4, Q25 x4)."""
import figs

Q = []


def add(stem, vi, vn, week, lo, topic, q, o, a, why, om, flip, fig=None, alt=""):
    assert len(o) == len(om) and 4 <= len(o) <= 5 and 0 <= a < len(o)
    d = dict(id=f"v2-q{stem}-{vi}", stem=stem, level="hard", vi=vi, vn=vn, week=week, lo=lo, topic=topic,
             q=q, o=o, a=a, why=why, om=om, flip=flip)
    if fig:
        d["fig"] = {"src": "fig/v2/" + fig.split("/fig/v2/")[1], "alt": alt}
    Q.append(d)


# =============================== Q8 ENZYME D ===============================
LO_Q = "W2: chemical interactions shape proteins; four levels of structure and what stabilises each"
ENZ = ("Enzyme D, from a gut bacterium, is a homodimer. Each subunit is a single polypeptide chain of 310 amino acids. "
       "Where the two subunits contact each other, the R group of {r88} 88 on one subunit forms {bond} with the R group of "
       "{r142} 142 on the other subunit. {extra} The structures of the named amino acids are shown below.\n\n")
SAME = "The wild-type Enzyme D is incubated under each of the following conditions. Which is most likely to cause the dimers to separate into monomers, while the monomers remain folded?"

p, _ = figs.amino_panel("q8-1", "KD")
add(8, 1, 4, 2, LO_Q, "Quaternary structure: what breaks an interface",
    ENZ.format(r88="lysine", bond="an ionic bond", r142="aspartate",
               extra="Each subunit's fold is held by a hydrophobic core and hydrogen bonds, and Enzyme D has no disulfide bonds.") + SAME,
    ["Boiling in SDS",
     "Adding trypsin, which hydrolyzes peptide bonds",
     "Adding a high concentration of NaCl",
     "Heating to 95 °C without SDS"],
    2,
    "The interface is one ionic bond between a positive R group (lysine's amine) and a negative R group (aspartate's carboxyl). "
    "Lots of dissolved ions crowd around those charges and shield them from each other, so the subunits let go, while the "
    "hydrophobic core and hydrogen bonds inside each subunit stay intact. Note: high salt is the standard chemistry answer; it was "
    "not in the course handouts.",
    ["Separates AND unfolds: SDS plus heat disrupts the noncovalent interactions inside each subunit too.",
     "Confuses separating subunits with cutting the backbone. Peptide bonds are inside each chain, not between the subunits.",
     "Correct. Salt shields the opposite charges and weakens the ionic bond at the interface without touching the fold.",
     "Heat is not selective. It disrupts the weak interactions that hold each subunit's tertiary structure, so the monomers unfold."],
    "If the interface had been a disulfide bond, salt would do nothing and the answer would be a reducing agent.",
    p, "Skeletal structures, neutral form, alphabetical: aspartate (side chain CH2-COOH) and lysine (side chain four CH2 groups ending in NH2).")

p, _ = figs.amino_panel("q8-2", "C")
add(8, 2, 4, 2, LO_Q, "Quaternary structure: what breaks an interface",
    ENZ.format(r88="cysteine", bond="a disulfide bond", r142="cysteine",
               extra="These cross-subunit disulfides are the only disulfide bonds in the enzyme. Each subunit's fold is held by a hydrophobic core and hydrogen bonds.") + SAME,
    ["Adding a high concentration of NaCl",
     "Boiling in SDS",
     "Lowering the pH to 3",
     "Adding a reducing agent (such as DTT) at room temperature, without SDS",
     "Adding trypsin, which hydrolyzes peptide bonds"],
    3,
    "Two cysteine R groups joined across the interface form a disulfide, which is a covalent bond. Only a reducing agent breaks it. "
    "Because each subunit's fold relies on noncovalent interactions alone, breaking the disulfide releases monomers that are still folded.",
    ["Salt shields charges, so it weakens ionic bonds. A disulfide is covalent, and salt does not break it.",
     "Course trap: SDS plus heat unfolds each subunit but does NOT break disulfide bonds. The chains stay linked AND unfold.",
     "pH changes the charge on acidic and basic R groups, which matters for ionic bonds, not covalent disulfides.",
     "Correct. The reducing agent breaks the S-S bond, and nothing else holds the subunits together.",
     "Cutting peptide bonds chops the chains apart; it does not release intact folded monomers."],
    "If the question had said 'boiled in SDS with a reducing agent', the dimers would separate but the monomers would also unfold.",
    p, "Skeletal structure, neutral form: cysteine (side chain CH2-SH).")

p, _ = figs.amino_panel("q8-3", "DR")
add(8, 3, 4, 2, LO_Q, "Quaternary structure: what breaks an interface",
    ENZ.format(r88="aspartate", bond="an ionic bond", r142="arginine",
               extra="Each subunit's fold is held by a hydrophobic core and hydrogen bonds.") +
    "A lab member says: \"Add DTT, a reducing agent. It breaks the bond between the subunits.\" Which condition is actually most likely "
    "to separate the dimers into monomers, while the monomers remain folded?",
    ["Adding DTT, as suggested",
     "Adding a high concentration of KCl",
     "Boiling in SDS with DTT",
     "Adding an enzyme that hydrolyzes glycosidic linkages"],
    1,
    "Aspartate's R group is a carboxyl (negative) and arginine's ends in a nitrogen-rich group (positive), so the interface is an ionic "
    "bond. A reducing agent only breaks disulfide (S-S) bonds. High salt shields opposite charges from each other, so it weakens ionic "
    "bonds specifically and leaves the fold alone. High salt is the standard chemistry answer; it was not in the course handouts.",
    ["Reducing agents break disulfides only. The interface here is ionic, so DTT does nothing to it.",
     "Correct. Dissolved K+ and Cl- shield the charged R groups and weaken the ionic bond at the interface.",
     "This separates the subunits, but SDS plus heat also unfolds every monomer.",
     "Wrong macromolecule: glycosidic linkages join sugars, not amino acids."],
    "If positions 88 and 142 had both been cysteine, DTT would have been the right call.",
    p, "Skeletal structures, neutral form, alphabetical: arginine and aspartate.")

p, _ = figs.amino_panel("q8-4", "EK")
add(8, 4, 4, 2, LO_Q, "Quaternary structure: what breaks an interface",
    ENZ.format(r88="glutamate", bond="an ionic bond", r142="lysine",
               extra="Enzyme D contains no disulfide bonds. Each subunit's fold is held by a hydrophobic core and hydrogen bonds.") +
    "The wild-type Enzyme D is incubated under each of the following conditions. Which is most likely to separate the dimers into "
    "monomers AND unfold the monomers?",
    ["Adding a high concentration of NaCl",
     "Adding a reducing agent at room temperature",
     "Adding trypsin, which hydrolyzes peptide bonds",
     "Boiling in SDS"],
    3,
    "This one reverses the usual logic: you want everything noncovalent gone. SDS plus heat disrupts the ionic bond at the interface "
    "and the hydrophobic core and hydrogen bonds inside each subunit. Enzyme D has no disulfides, so nothing covalent holds the chains "
    "together or in shape.",
    ["Reverses the logic: salt separates the dimers but leaves each monomer folded. This question wants both.",
     "There are no disulfides in Enzyme D, so a reducing agent has nothing to break.",
     "Cutting peptide bonds destroys the chains rather than giving intact, unfolded monomers.",
     "Correct. SDS plus heat breaks the interface and unfolds each subunit."],
    "If the interface had been a disulfide, boiling in SDS would unfold the subunits but leave them linked; you would need a reducing agent too.",
    p, "Skeletal structures, neutral form, alphabetical: glutamate and lysine.")

# =============================== Q10 SNIPASE ===============================
LO_P = "W2: orient an amino acid and polypeptide; condensation vs hydrolysis"
SNIP = ("A newly discovered protease, snipase, hydrolyzes peptide bonds on the {side}-terminal side of {cls} amino acids. "
        "If the tetrapeptide shown below is fully digested by snipase, what products form? "
        "(Residues are numbered 1 to 4 starting from the N-terminus.)")
F1 = "Residue 1 as a free amino acid, plus a tripeptide of residues 2-4"
D2 = "Two dipeptides: residues 1-2 and residues 3-4"
T3 = "A tripeptide of residues 1-3, plus residue 4 as a free amino acid"
NC = "No change: the tetrapeptide stays intact"
F4 = "Four free amino acids"

p, f = figs.peptide("q10-1", "GKSF")
add(10, 1, 5, 2, LO_P, "Protease cut sites and peptide orientation",
    SNIP.format(side="C", cls="basic"), [F1, D2, T3, NC, F4], 1,
    "Find the N-terminus (the free amino group) and number from there. Residue 2's R group ends in an extra amine, so it is basic. "
    "Its C-terminal side is the peptide bond between residues 2 and 3. One cut gives two dipeptides.",
    ["Cut on the N-terminal side of the basic residue. The question says C-terminal side.",
     "Correct. One cut, after residue 2.",
     "Cut beside the residue with a ring (aromatic) instead of the one with the extra amine (basic).",
     "Missed the basic residue: the extra amine on residue 2's R group marks it as basic.",
     "Snipase cuts only next to basic residues, not every peptide bond."],
    "If snipase cut on the N-terminal side of basic residues, the cut would fall between residues 1 and 2: a free amino acid plus a tripeptide.",
    p, "Bond-line tetrapeptide, neutral form, free amino group at one end and free carboxyl group at the other. No residue labels.")

p, f = figs.peptide("q10-2", "VRSA")
add(10, 2, 5, 2, LO_P, "Protease cut sites and peptide orientation",
    SNIP.format(side="N", cls="basic"), [D2, T3, F1, NC], 2,
    "The free amino group marks residue 1. Residue 2's R group ends in a nitrogen-rich group, so it is basic. Its N-terminal side is the "
    "bond between residues 1 and 2, so residue 1 is released and residues 2-4 stay together.",
    ["That is the C-terminal side of the basic residue. Snipase here cuts on the N-terminal side.",
     "Numbered from the wrong end. Read from the C-terminus, the same cut looks like this.",
     "Correct. One cut, between residues 1 and 2.",
     "Missed the basic R group on residue 2."],
    "If snipase cut on the C-terminal side instead, the cut would fall between residues 2 and 3, giving two dipeptides.",
    p, "Bond-line tetrapeptide, neutral form, free amino group at one end and free carboxyl group at the other. No residue labels.")

p, f = figs.peptide("q10-3", "SFGL")
add(10, 3, 5, 2, LO_P, "Protease cut sites and peptide orientation",
    SNIP.format(side="C", cls="aromatic"), [F1, T3, NC, D2], 3,
    "Aromatic means a ring in the R group. Only residue 2 has one. Its C-terminal side is the bond between residues 2 and 3, so one cut "
    "gives two dipeptides. Residue 4 is large and nonpolar, but it has no ring, so it is not aromatic.",
    ["That is the N-terminal side of the aromatic residue. The question says C-terminal side.",
     "Treated the large nonpolar residue 4 as aromatic. Aromatic means a ring, not just hydrophobic.",
     "Missed the ring on residue 2.",
     "Correct. One cut, after residue 2."],
    "If the aromatic residue had been residue 4, its C-terminal side would have no peptide bond and nothing would be cut.",
    p, "Bond-line tetrapeptide, neutral form, free amino group at one end and free carboxyl group at the other. No residue labels.")

p, f = figs.peptide("q10-4", "GSAK")
add(10, 4, 5, 2, LO_P, "Protease cut sites and peptide orientation",
    SNIP.format(side="C", cls="basic"), [T3, NC, F1, D2, F4], 1,
    "Number from the free amino group. The only basic R group (ending in an extra amine) belongs to residue 4, the C-terminal residue, "
    "whose carboxyl group is free. There is no peptide bond on its C-terminal side, so snipase cannot cut. Same logic as trypsin "
    "leaving the last residue of Lys-Tyr-Asp-Lys alone.",
    ["That is a cut on the N-terminal side of the basic residue.",
     "Correct. The basic residue is the last residue; nothing lies on its C-terminal side.",
     "Numbered from the wrong end: the basic residue sits at the C-terminus, not the N-terminus.",
     "There is no basic residue at position 2.",
     "Snipase cuts only beside basic residues, not every peptide bond."],
    "If snipase cut on the N-terminal side of basic residues, it would cut between residues 3 and 4: a tripeptide plus a free amino acid.",
    p, "Bond-line tetrapeptide, neutral form, free amino group at one end and free carboxyl group at the other. No residue labels.")

p, f = figs.peptide("q10-5", "RAKG")
add(10, 5, 5, 2, LO_P, "Protease cut sites and peptide orientation",
    SNIP.format(side="C", cls="basic"),
    [F1, D2, "Residues 1 and 4 as free amino acids, plus a dipeptide of residues 2-3", T3, F4], 2,
    "Two residues are basic: residue 1 (R group ending in a nitrogen-rich group) and residue 3 (R group ending in an amine). Cutting on "
    "the C-terminal side of each breaks the 1-2 bond and the 3-4 bond. That releases residues 1 and 4 and leaves 2-3 as a dipeptide.",
    ["Found only the first basic residue. Residue 3 is basic too.",
     "That is cutting on the N-terminal side of the basic residues.",
     "Correct. Two cuts: after residue 1 and after residue 3.",
     "Found only residue 3 as basic and missed residue 1.",
     "The bond between residues 2 and 3 is not on the C-terminal side of a basic residue, so it stays."],
    "If snipase cut on the N-terminal side instead, only the bond between residues 2 and 3 would be cut, giving two dipeptides.",
    p, "Bond-line tetrapeptide, neutral form, free amino group at one end and free carboxyl group at the other. No residue labels.")

# =============================== Q11 / Q12 HORMONE H ===============================
LO_G = "W2: SDS-PAGE"
HH = ("Hormone H is made as a single, inactive polypeptide called pro-H ({P} kDa). To activate it, an enzyme hydrolyzes two peptide "
      "bonds, removing a {S} kDa segment from the middle of the chain. The two remaining pieces ({a} kDa and {b} kDa) stay attached to "
      "each other by a single disulfide bond, forming mature H. This is the only disulfide bond present in any form of Hormone H. The "
      "released {S} kDa segment does not associate with mature H but persists in the cell and is not degraded.\n\n"
      "Samples were analyzed by SDS-PAGE and stained so that all H-derived polypeptides are visible. The gel below shows a molecular "
      "weight ladder and five possible band patterns (lanes A to E).\n\n")
LANES = ["Lane A", "Lane B", "Lane C", "Lane D", "Lane E"]


def lanes_dict(*bands):
    return dict(zip("ABCDE", bands))


def hh(stem, vi, vn, P, S, a_, b_, ask, lanes, ans, why, om, flip, topic):
    assert P == S + a_ + b_
    p = figs.gel(f"q{stem}-{vi}", lanes_dict(*lanes))
    alt = "SDS-PAGE gel: ladder 50, 40, 30, 25, 20, 15, 10, 5 kDa. " + "; ".join(
        f"lane {L}: " + ", ".join(str(k) for k in sorted(v, reverse=True)) + " kDa" for L, v in lanes_dict(*lanes).items())
    add(stem, vi, vn, 2, LO_G, topic, HH.format(P=P, S=S, a=a_, b=b_) + ask, LANES, ans, why, om, flip, p, alt)


hh(11, 1, 3, 30, 6, 14, 10, "Purified mature H is boiled in SDS with a reducing agent. Which lane best represents the expected result?",
   [[24], [30], [14, 10, 6], [14, 10], [24, 6]], 3,
   "Mature H is two chains (14 and 10 kDa) held by one disulfide. SDS plus heat unfolds them and the reducing agent breaks the "
   "disulfide, so the two chains run separately: two bands, at 14 and 10 kDa. The segment was removed before purification, so it is absent.",
   ["Forgot that the reducing agent breaks the disulfide holding the two pieces together.",
    "Mature H is not pro-H: the middle segment has been cut out.",
    "The sample is purified mature H; the released segment is not in it.",
    "Correct. Two chains, two sizes, two bands.",
    "Kept the disulfide intact and added a segment that is not in a purified sample."],
   "Without the reducing agent, the disulfide survives SDS and heat, so you would see one band at 24 kDa.",
   "SDS-PAGE: disulfides and reducing agent")

hh(11, 2, 3, 40, 8, 20, 12, "Purified mature H is boiled in SDS without a reducing agent. Which lane best represents the expected result?",
   [[20, 12], [40], [32], [32, 8], [20, 12, 8]], 2,
   "SDS and heat unfold proteins but do not break disulfide bonds; only a reducing agent does. Mature H's two pieces stay linked, so it "
   "runs as one polypeptide of 20 + 12 = 32 kDa.",
   ["Course trap: assumed SDS and heat break the disulfide. They do not.",
    "Mature H is not pro-H: the 8 kDa segment has been removed.",
    "Correct. One linked unit, one band at 32 kDa.",
    "The sample is purified mature H; the segment is not in it.",
    "Two errors: broke the disulfide without a reducing agent and added the segment."],
   "With a reducing agent added, the disulfide breaks and you would see two bands, at 20 and 12 kDa.",
   "SDS-PAGE: disulfides and reducing agent")

hh(11, 3, 3, 30, 8, 11, 11, "Purified mature H is boiled in SDS with a reducing agent. Which lane best represents the expected result?",
   [[22], [11], [11, 8], [22, 8], [30]], 1,
   "The reducing agent breaks the disulfide, so the two pieces run separately. But they are the same size, and SDS-PAGE sorts only by "
   "size, so both land in one band at 11 kDa. Number of bands = number of different sizes, not number of chains.",
   ["Forgot that the reducing agent breaks the disulfide.",
    "Correct. Two chains, one size, one band (holding twice the protein).",
    "The sample is purified mature H; the 8 kDa segment is not in it.",
    "Kept the disulfide intact and added a segment that is not in the sample.",
    "That is pro-H, which has been processed."],
   "If the pieces had been 12 and 10 kDa instead, you would see two bands.",
   "SDS-PAGE: band count = distinct sizes")

hh(12, 1, 5, 30, 6, 14, 10,
   "A sample is taken halfway through the activation reaction, when only some of the pro-H has been processed (assume both peptide bonds in any one pro-H molecule are cut at the same moment). It is boiled in SDS "
   "without a reducing agent. Which lane best represents the expected result?",
   [[24, 6], [30, 24], [30, 14, 10, 6], [30], [30, 24, 6]], 4,
   "Halfway means three kinds of H polypeptide are present: unprocessed pro-H (30), mature H (14 + 10 held by the disulfide, which SDS "
   "and heat do not break, so 24) and the released segment (6), which persists. Three sizes, three bands.",
   ["Forgot the pro-H that has not been processed yet.",
    "Forgot the 6 kDa segment, which persists and is not degraded.",
    "Broke the disulfide without a reducing agent. SDS and heat leave it intact.",
    "That is the start of the reaction, before any processing.",
    "Correct. Pro-H, mature H and the segment."],
   "With a reducing agent, mature H would split into 14 and 10, giving four bands: 30, 14, 10 and 6.",
   "SDS-PAGE: mixtures during processing")

hh(12, 2, 5, 40, 8, 20, 12,
   "A sample is taken halfway through the activation reaction, when only some of the pro-H has been processed (assume both peptide bonds in any one pro-H molecule are cut at the same moment). It is boiled in SDS "
   "with a reducing agent. Which lane best represents the expected result?",
   [[40, 20, 12, 8], [40, 32, 8], [20, 12, 8], [40, 20, 12], [20, 12]], 0,
   "Halfway: pro-H, mature H and the segment are all present. The reducing agent breaks mature H's disulfide, so its pieces run "
   "separately at 20 and 12. Pro-H is one continuous chain; breaking its disulfide does not change its size, so it stays at 40. The "
   "8 kDa segment persists.",
   ["Correct. Pro-H, both pieces and the segment.",
    "Ignored the reducing agent: it does break mature H's disulfide.",
    "Forgot the pro-H that has not been processed yet.",
    "Forgot the segment, which persists.",
    "Forgot both the unprocessed pro-H and the segment."],
   "Without the reducing agent, mature H would stay together at 32 kDa: bands at 40, 32 and 8.",
   "SDS-PAGE: mixtures during processing")

hh(12, 3, 5, 30, 6, 14, 10,
   "A sample is taken at the moment the activating enzyme is added, before any pro-H has been processed. It is boiled in SDS with a "
   "reducing agent. Which lane best represents the expected result?",
   [[14, 10, 6], [24, 6], [30], [30, 24, 6], [30, 14, 10, 6]], 2,
   "No processing has happened yet, so only pro-H exists. The reducing agent breaks disulfides, not peptide bonds, and pro-H is one "
   "continuous chain, so it runs as a single 30 kDa band.",
   ["Treated the reducing agent as if it cut peptide bonds. It only breaks disulfides.",
    "That is a fully processed sample without a reducing agent.",
    "Correct. Only pro-H, one band.",
    "That is a halfway sample without a reducing agent.",
    "That is a halfway sample with a reducing agent."],
   "At the end of the reaction with a reducing agent, you would see 14, 10 and 6 kDa bands and no pro-H.",
   "SDS-PAGE: mixtures during processing")

hh(12, 4, 5, 36, 10, 15, 11,
   "A sample is taken after the activation reaction has finished, when all of the pro-H has been processed. It is boiled in SDS "
   "without a reducing agent. Which lane best represents the expected result?",
   [[36, 26, 10], [26], [15, 11, 10], [26, 10], [15, 11]], 3,
   "All pro-H is processed, so none is left. Mature H stays together without a reducing agent (15 + 11 = 26). The 10 kDa segment is not "
   "degraded and is still in the sample, so it gives its own band.",
   ["That is a halfway sample: no pro-H is left at the end.",
    "Forgot the segment. The stem says it persists and is not degraded.",
    "Broke the disulfide without a reducing agent.",
    "Correct. Mature H plus the persisting segment.",
    "Broke the disulfide and forgot the segment."],
   "With a reducing agent, you would see 15, 11 and 10 kDa bands.",
   "SDS-PAGE: mixtures during processing")

hh(12, 5, 5, 32, 6, 16, 10,
   "A sample is taken halfway through the activation reaction, when only some of the pro-H has been processed (assume both peptide bonds in any one pro-H molecule are cut at the same moment). It is boiled in SDS "
   "with a reducing agent. Which lane best represents the expected result?",
   [[32, 26, 6], [32, 16, 10, 6], [16, 10, 6], [32, 16, 10], [26, 16, 10, 6]], 1,
   "A reducing agent breaks disulfide bonds, not peptide bonds. Pro-H is a single continuous chain, so even with its disulfide broken "
   "it still runs at 32 kDa. Mature H splits into 16 and 10, and the 6 kDa segment persists.",
   ["Ignored the reducing agent: mature H's disulfide breaks.",
    "Correct. Pro-H at full size, both pieces and the segment.",
    "Forgot the pro-H that has not been processed yet.",
    "Forgot the segment, which persists.",
    "Shrank pro-H: a reducing agent cannot remove the segment from pro-H, because that takes hydrolysis of peptide bonds."],
   "Without a reducing agent: 32, 26 and 6 kDa.",
   "SDS-PAGE: mixtures during processing")

# =============================== Q15 RING SUGARS ===============================
LO_S = "W3: classify monosaccharides"
SUG_O = ["Aldopentose", "Aldohexose", "Ketopentose", "Ketohexose"]
SUG_Q = "{n} is shown below in its ringed form. How would it be classified in its linear form?"
SUG_ALT = "Ring structure with every carbon labelled with its hydrogens, the ring oxygen, every OH and every CH2OH. Stereochemistry not shown."

p = figs.sugar("q15-1", "OCC1OC(O)C(O)C(O)C1O", "C6H12O6", 6, 6, True)
add(15, 1, 5, 3, LO_S, "Ring sugars: aldose or ketose, how many carbons", SUG_Q.format(n="Glucose"), SUG_O, 1,
    "Count every carbon: five in the ring plus the CH2OH outside it = 6, a hexose. The anomeric carbon (bonded to both the ring O and "
    "an OH) also carries an H, so in the linear form it was the aldehyde carbon (C1). Aldohexose.",
    ["Counted only the ring carbons and missed the CH2OH carbon outside the ring.",
     "Correct. 6 carbons, aldehyde at the anomeric carbon.",
     "Two errors: the anomeric carbon has an H, and there are 6 carbons.",
     "The anomeric carbon carries an H, so it came from an aldehyde, not a ketone."],
    "If the anomeric carbon had carried a CH2OH instead of an H, it would have been a ketose.", p, SUG_ALT)

p = figs.sugar("q15-2", "OCC1OC(O)(CO)C(O)C1O", "C6H12O6", 5, 6, False)
add(15, 2, 5, 3, LO_S, "Ring sugars: aldose or ketose, how many carbons", SUG_Q.format(n="Fructose"), SUG_O, 3,
    "The five-membered ring holds four carbons and the ring O. Two CH2OH groups sit outside it, giving 6 carbons. The anomeric carbon "
    "carries an OH and a CH2OH but no H, so it was a ketone carbon (C2). Ketohexose.",
    ["Ring-size trap, plus the anomeric carbon has no H. A five-membered ring is not five carbons.",
     "The anomeric carbon has no H, so it was a ketone, not an aldehyde.",
     "Ring-size trap: the ring has 4 carbons and two CH2OH carbons sit outside it, so 6 in total.",
     "Correct. 6 carbons, ketone at the anomeric carbon."],
    "If one of the carbons outside the ring were missing, it would have been a ketopentose.", p, SUG_ALT)

p = figs.sugar("q15-3", "OCC1OC(O)C(O)C1O", "C5H10O5", 5, 5, True)
add(15, 3, 5, 3, LO_S, "Ring sugars: aldose or ketose, how many carbons", SUG_Q.format(n="Ribose"), SUG_O, 0,
    "Four ring carbons plus one CH2OH outside = 5 carbons. The anomeric carbon has an H, so it was an aldehyde. Aldopentose.",
    ["Correct. 5 carbons, aldehyde at the anomeric carbon.",
     "Counted the ring O as a carbon. The ring has 4 carbons.",
     "The anomeric carbon has an H, so it was an aldehyde.",
     "Two errors: the anomeric carbon has an H, and there are only 5 carbons."],
    "If the anomeric carbon carried a CH2OH and no H, it would be a ketose, and you would count that extra carbon.", p, SUG_ALT)

p = figs.sugar("q15-4", "OCC1(O)OCC(O)C1O", "C5H10O5", 5, 5, False)
add(15, 4, 5, 3, LO_S, "Ring sugars: aldose or ketose, how many carbons", SUG_Q.format(n="Sugar R"), SUG_O, 2,
    "The ring holds four carbons and the ring O. Only one CH2OH sits outside, on the anomeric carbon, which has no H, so it was a ketone "
    "carbon. The CH2 on the other side of the ring O is a ring carbon, not a CH2OH. 4 + 1 = 5 carbons. Ketopentose.",
    ["The anomeric carbon has no H, so it was a ketone.",
     "Two errors: no H on the anomeric carbon, and only 5 carbons.",
     "Correct. 5 carbons, ketone at the anomeric carbon.",
     "Assumed a fructose-like ring always means 6 carbons. Only one carbon sits outside this ring."],
    "If there had been a second CH2OH outside the ring, it would have been a ketohexose like fructose.", p, SUG_ALT)

p = figs.sugar("q15-5", "OCC(O)C1OC(O)C(O)C1O", "C6H12O6", 5, 6, True)
add(15, 5, 5, 3, LO_S, "Ring sugars: aldose or ketose, how many carbons",
    SUG_Q.format(n="Tuftsose, a sugar made by a deep-sea bacterium,"), SUG_O, 1,
    "The ring is five-membered, but that does not make it a pentose. Count every carbon: four in the ring plus a two-carbon side chain "
    "(a CH with an OH, then a CH2OH) outside = 6. The anomeric carbon has an H, so it was an aldehyde. Aldohexose.",
    ["Ring-size trap: a five-membered ring is not five carbons. Count the side chain.",
     "Correct. 6 carbons, aldehyde at the anomeric carbon.",
     "Two errors: the anomeric carbon has an H, and the side chain adds two carbons.",
     "The anomeric carbon has an H, so it was an aldehyde."],
    "If the side chain had been a single CH2OH, it would have been an aldopentose like ribose.", p, SUG_ALT)

# =============================== Q22 TRANSITION-STATE ANALOG ===============================
LO_E = "W4: how enzymes speed reactions"
TS = "Enzymes speed up reactions by binding and stabilizing the transition state. "
add(22, 1, 3, 4, LO_E, "Transition-state analogs",
    TS + "Researchers design a stable molecule that has the same shape and charge distribution as the transition state of the reaction "
    "catalyzed by enzyme E, but it cannot be converted to product. What effect would this molecule most likely have when added to "
    "enzyme E and its substrate?",
    ["It binds the active site weakly, because the active site is shaped to fit the substrate",
     "It binds the active site more tightly than the substrate does and acts as a competitive inhibitor, slowing the reaction",
     "It speeds up the reaction by giving the enzyme a ready-made transition state",
     "It makes ΔG of the reaction less negative, so less product forms at equilibrium",
     "It binds a separate allosteric site and activates the enzyme"],
    1,
    "The active site binds the transition state more tightly than the substrate; that tight binding is what stabilizes it and lowers "
    "the activation energy. A stable look-alike gets that tight binding but cannot react, so it sits in the active site and blocks "
    "substrate: a strong competitive inhibitor. ΔG is unchanged.",
    ["The active site fits the transition state best, not the substrate. That is how enzymes stabilize it.",
     "Correct. Tight binding in the active site, competitive inhibition, lower rate.",
     "The analog never turns into product. It occupies the active site, so less substrate is converted.",
     "Enzymes and inhibitors change rate, never ΔG.",
     "It mimics something that binds in the active site, so it competes there."],
    "If the molecule had resembled the substrate instead, it would still be a competitive inhibitor, but a weaker one, because the "
    "active site binds the substrate less tightly than the transition state.")

add(22, 2, 3, 4, LO_E, "Transition-state analogs",
    "HIV protease hydrolyzes peptide bonds in viral proteins. " + TS + "A drug company designs a stable molecule that mimics the "
    "transition state of peptide bond hydrolysis by HIV protease but contains no bond the enzyme can break. What is the most likely "
    "effect on the rate at which HIV protease cuts viral proteins?",
    ["The rate increases, because the enzyme no longer has to bend the substrate into the transition state",
     "The rate increases, because stabilizing the transition state lowers the activation energy",
     "The rate decreases, because the mimic binds the active site tightly and keeps viral proteins out",
     "The rate is unchanged, because the mimic cannot be cut"],
    2,
    "Peptide bond hydrolysis is exergonic but slow without a catalyst, because its activation energy is high. HIV protease speeds it up "
    "by binding the transition state tightly. A stable mimic takes that tight-binding spot and never leaves as product, so fewer active "
    "sites are free for viral proteins. The rate drops. This is the idea behind several real HIV drugs.",
    ["Speeds-up trap: the mimic is never converted to product, so the enzyme gains nothing from holding it.",
     "True for a real transition state, but this molecule is a dead end that occupies the active site.",
     "Correct. Competitive inhibition by a transition-state mimic.",
     "Not being cut is exactly why it stays bound and blocks the site."],
    "If the question had asked what happens to ΔG of peptide bond hydrolysis, the answer would be no change.")

add(22, 3, 3, 4, LO_E, "Transition-state analogs",
    TS + "Researchers add a stable transition-state analog to a reaction catalyzed by enzyme E, at a concentration that occupies "
    "about half of the enzyme's active sites. Which statement about the reaction is correct?",
    ["ΔG of the reaction becomes less negative, so less product forms",
     "The equilibrium shifts toward the substrate",
     "The analog lowers the activation energy further, so the reaction speeds up",
     "The enzyme is used up as it converts the analog to product",
     "ΔG is unchanged; the reaction runs more slowly because fewer active sites are free to bind substrate"],
    4,
    "Enzymes, and molecules that block them, change only how fast a reaction reaches equilibrium. They never change ΔG or where "
    "equilibrium lies. The analog blocks the active sites it occupies, so the rate drops while ΔG stays the same.",
    ["Changes-ΔG trap: inhibitors change rate, not ΔG.",
     "Equilibrium position is set by ΔG, which no inhibitor changes.",
     "Speeds-up trap: the analog occupies active sites and cannot react.",
     "The analog cannot react, and enzymes are not consumed.",
     "Correct. Same ΔG, lower rate."],
    "If the question had asked about the rate with twice as much analog, the rate would drop further; ΔG would still not change.")

# =============================== Q23 COUPLING ===============================
LO_C = "W4: coupling unfavourable to favourable processes"
CPL = ("Cells make molecule Z with the enzyme Z synthase:\n"
       "Reaction 1: X + Y → Z + H2O   ΔG = {g} kJ/mol\n"
       "Reaction 2: ATP + H2O → ADP + Pi   ΔG = −30 kJ/mol\n"
       "Z synthase binds X, Y and ATP together in its active site. It transfers a phosphate from ATP to X, forming X-P, and Y then "
       "displaces the phosphate to make Z. (ΔG values are for conditions in the cell.)\n\n")
add(23, 1, 4, 4, LO_C, "Energy coupling", CPL.format(g="+20") + "The cell has plenty of ATP, X and Y. Will Z accumulate?",
    ["No. Reaction 1 has a positive ΔG, so it cannot happen in a cell",
     "Yes. The enzyme lowers ΔG of reaction 1 until it is negative",
     "Yes. The reactions are linked through the shared intermediate X-P, so the overall ΔG is +20 + (−30) = −10 kJ/mol",
     "No. The energy from ATP hydrolysis is released as heat and cannot be used"],
    2,
    "Coupling works when one enzyme links the two reactions through a shared intermediate (X-P). Then you add the ΔG values: "
    "+20 + (−30) = −10 kJ/mol. Negative overall, so Z is made and accumulates.",
    ["Ignores coupling: an unfavourable reaction can run when it is linked to a favourable one.",
     "Enzymes lower activation energy, never ΔG.",
     "Correct. Linked reactions, negative sum.",
     "That happens only when ATP is hydrolyzed separately. Here the enzyme links the two reactions."],
    "If reaction 1 had a ΔG of +40 kJ/mol, the sum would be +10 and Z would not accumulate.")

add(23, 2, 4, 4, LO_C, "Energy coupling", CPL.format(g="+42") + "The cell has plenty of ATP, X and Y. Will Z accumulate?",
    ["Yes. ATP hydrolysis is strongly exergonic, so any reaction coupled to it goes forward",
     "No. Even coupled, the overall ΔG is +42 + (−30) = +12 kJ/mol, so the overall reaction is not spontaneous",
     "Yes. Z synthase lowers the activation energy, so Z forms",
     "No. Reaction 1 is endergonic, and endergonic reactions can never be coupled"],
    1,
    "Coupling lets you add the ΔG values, but the sum still has to be negative. One ATP supplies −30 kJ/mol, and reaction 1 needs +42. "
    "The overall ΔG is +12 kJ/mol, so Z does not accumulate.",
    ["One ATP supplies a fixed amount, −30 kJ/mol. It cannot drive a reaction that needs more than that.",
     "Correct. Coupled, but the sum is still positive.",
     "Lowering activation energy speeds up reactions that are already favourable; it cannot make an uphill reaction go.",
     "Endergonic reactions are exactly the ones that get coupled. This one just needs more than one ATP's worth."],
    "If the enzyme hydrolyzed two ATP per Z (−60 kJ/mol in total), the sum would be −18 kJ/mol and Z would accumulate.")

add(23, 3, 4, 4, LO_C, "Energy coupling",
    CPL.format(g="+20") + "Researchers use a mutant Z synthase that still binds X and Y but cannot bind ATP. To supply energy, they add "
    "ATP and a different enzyme, an ATPase, that hydrolyzes ATP to ADP + Pi in the same solution. Will Z accumulate?",
    ["No. ATP is hydrolyzed on its own, so its energy is released as heat, and reaction 1 alone still has ΔG = +20 kJ/mol",
     "Yes. The two ΔG values still add to −10 kJ/mol",
     "Yes. The ATPase lowers the activation energy of reaction 1",
     "No. ATP hydrolysis is endergonic, so it absorbs energy"],
    0,
    "Coupling needs a physical link: the same enzyme must use ATP's phosphate to make the intermediate X-P. Here ATP is hydrolyzed by a "
    "separate enzyme, so its free energy is released as heat. Reaction 1 still stands alone at +20 kJ/mol, so Z does not accumulate.",
    ["Correct. No shared intermediate, no coupling.",
     "Adding ΔG values only works when the reactions are linked through a shared intermediate in one active site.",
     "The ATPase acts on ATP, not on X and Y. And lowering activation energy never changes ΔG.",
     "Wrong sign: ATP hydrolysis is exergonic (ΔG = −30 kJ/mol)."],
    "If the wild-type Z synthase were used, the reactions would be coupled and the overall ΔG would be −10 kJ/mol.")

add(23, 4, 4, 4, LO_C, "Energy coupling and Le Chatelier",
    "Cells make molecule Z with the enzyme Z synthase:\nX + Y ⇌ Z   ΔG = +5 kJ/mol when X, Y and Z are all at equal concentrations\n"
    "Z synthase binds X and Y together in its active site. In the cell, a second enzyme converts Z into W as fast as Z forms, so Z stays "
    "at a very low concentration, while X and Y stay plentiful.\n\nWill Z synthase keep making Z?",
    ["No. ΔG is positive, so the reaction can never run forward",
     "Yes. Z synthase changes ΔG to a negative value",
     "No. The reaction reaches equilibrium and stops, because Z never builds up",
     "Yes. Removing Z as it forms pulls the reaction forward (Le Chatelier), making ΔG negative under these conditions"],
    3,
    "ΔG depends on concentrations. The +5 kJ/mol value only applies when X, Y and Z are equal. With X and Y high and Z constantly "
    "removed, the reaction sits far from equilibrium on the reactant side, so the actual ΔG is negative and Z keeps being made (and "
    "immediately used). This is Le Chatelier: removing product shifts the equilibrium to the right.",
    ["That ΔG is for equal concentrations. Keeping Z low changes it.",
     "Enzymes never change ΔG.",
     "Equilibrium is never reached while Z keeps being removed.",
     "Correct. Product removal pulls the reaction forward."],
    "If Z were not removed and built up instead, the reaction would slow and stop at equilibrium.")

# =============================== Q25 REACTION COORDINATE DIAGRAMS ===============================
LO_R = "W4: thermodynamics and spontaneity; how enzymes speed reactions"
RCD = ("Each of the reaction coordinate diagrams below represents a different reaction. All four diagrams are drawn on the same free "
       "energy scale (y axis). Assume a hump (activation energy) of 20 units or less is crossed quickly without an enzyme; anything "
       "larger needs an enzyme to go at a useful rate.\n\n")
ENZ_ONLY = ("Which diagram(s) represent reactions that could occur in a cell under these conditions only if an enzyme is present? "
            "(Here that means an enzyme alone is enough, and without one the reaction would not occur.)")
CPL_ONLY = ("Which diagram(s) represent reactions that could occur in a cell under these conditions only if coupled to a strongly "
            "exergonic reaction such as ATP hydrolysis? (Here that means coupling is enough, and without coupling the reaction would "
            "not occur. In a cell the coupling is carried out by an enzyme.)")


def rcd(vi, data, ask, o, a, why, om, flip):
    p = figs.energy(f"q25-{vi}", data)
    alt = "Four reaction coordinate diagrams on one free-energy axis (0 to 160). " + "; ".join(
        f"diagram {i+1}: reactants {d['r']}, peak {d['ts']}, products {d['p']}" for i, d in enumerate(data))
    add(25, vi, 4, 4, LO_R, "Reaction coordinate diagrams: enzyme vs coupling", RCD + ask, o, a, why, om, flip, p, alt)


rcd(1, [dict(r=50, ts=65, p=20), dict(r=55, ts=120, p=25), dict(r=20, ts=38, p=32), dict(r=25, ts=100, p=60)], ENZ_ONLY,
    ["1 only", "2 only", "2 and 4", "4 only", "3 and 4"], 1,
    "Ask two things per diagram. Is it downhill (products below reactants, ΔG negative)? Is the hump small or big? Only diagram 2 is "
    "downhill with a big hump: spontaneous, but too slow without a catalyst. Diagram 1 is downhill with a small hump, so it goes on its "
    "own. Diagrams 3 and 4 are uphill; no enzyme alone can make an uphill reaction go.",
    ["Diagram 1 has a small hump (15). It goes on its own.",
     "Correct. Downhill with a big hump (65).",
     "Diagram 4 is uphill. An enzyme alone cannot make it go.",
     "Biggest-hump trap: diagram 4 is uphill, so an enzyme alone is not enough.",
     "Uphill reactions need coupling, not just an enzyme."],
    "If the question had said 'only if coupled to ATP hydrolysis', the answer would be 3 and 4.")

rcd(2, [dict(r=30, ts=48, p=42), dict(r=60, ts=75, p=25), dict(r=15, ts=33, p=28), dict(r=70, ts=130, p=35)], CPL_ONLY,
    ["3 and 4", "4 only", "1 only", "1 and 3", "2 and 4"], 3,
    "Coupling is needed when products sit higher than reactants (ΔG positive). Diagrams 1 and 3 are uphill. No enzyme alone can make "
    "them go; each needs to be coupled to a strongly downhill reaction. Diagrams 2 and 4 are downhill and need no coupling; diagram 4 "
    "has a big hump, so it needs an enzyme, but that is a speed problem, not a direction problem.",
    ["Diagram 4 is downhill. Its big hump needs an enzyme, not coupling.",
     "Biggest-hump trap: diagram 4 is downhill and needs only an enzyme.",
     "Diagram 3 is uphill too (15 to 28), even though its hump is small.",
     "Correct. Both uphill reactions.",
     "Downhill reactions do not need coupling."],
    "If the question had said 'only if an enzyme is present', the answer would be 4 only.")

rcd(3, [dict(r=100, ts=112, p=80), dict(r=10, ts=28, p=24), dict(r=70, ts=135, p=40), dict(r=60, ts=78, p=74)], CPL_ONLY,
    ["1 and 4", "4 only", "1 only", "3 only", "2 and 4"], 4,
    "Direction depends on the change in free energy from reactants to products, not on where the curve sits on the axis. Diagram 1 sits "
    "high but runs downhill (100 to 80). Diagram 2 sits low but runs uphill (10 to 24). Uphill means coupling is needed: diagrams 2 and 4.",
    ["Absolute-height trap: diagram 1 sits high but runs downhill (100 to 80).",
     "Diagram 2 is uphill too, even though it sits low on the axis.",
     "Absolute-height trap: diagram 1 is the highest curve but it runs downhill.",
     "Diagram 3 is downhill with a big hump. It needs an enzyme, not coupling.",
     "Correct. Both uphill reactions, wherever they sit on the axis."],
    "If the question had asked which needs only an enzyme, the answer would be diagram 3.")

rcd(4, [dict(r=40, ts=52, p=15), dict(r=15, ts=120, p=55), dict(r=75, ts=130, p=45), dict(r=25, ts=42, p=38)], ENZ_ONLY,
    ["2 only", "2 and 3", "3 only", "1 and 3", "2 and 4"], 2,
    "Big humps grab the eye, but an enzyme only helps a reaction that is already downhill. Diagram 2 has the biggest hump but is uphill, "
    "so an enzyme alone can never make it go; it needs coupling. Diagram 3 is downhill with a big hump, so it needs just an enzyme. "
    "Diagram 1 is downhill with a small hump and goes on its own.",
    ["Big-hump-uphill trap: diagram 2 is uphill, so an enzyme alone is not enough.",
     "Diagram 2 is uphill. Only diagram 3 needs just an enzyme.",
     "Correct. Downhill with a big hump.",
     "Diagram 1 has a small hump (12). It goes on its own.",
     "Both are uphill. They need coupling."],
    "If diagram 2 were coupled to ATP hydrolysis, it could go, with an enzyme carrying out the coupling.")

if __name__ == "__main__":
    import json, collections
    c = collections.Counter(q["stem"] for q in Q)
    print(len(Q), dict(c))
    assert dict(c) == {8: 4, 10: 5, 11: 3, 12: 5, 15: 5, 22: 3, 23: 4, 25: 4}
    for q in Q:
        assert q["vn"] == c[q["stem"]]
        txt = q["q"] + " ".join(q["o"]) + q["why"] + " ".join(q["om"]) + q["flip"]
        assert "—" not in txt and "–" not in txt, q["id"]
    json.dump(Q, open("build/hard.json", "w"), ensure_ascii=False, indent=1)
    for q in Q:
        if "fig" in q:
            figs.png_of(figs.FIG + "/" + q["fig"]["src"].split("/")[-1])
    print("ok")
