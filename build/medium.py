"""Tier 2: the 9 MEDIUM stems, 21 questions (Q1 x2, Q2 x2, Q6 x2, Q7 x3, Q9 x3, Q14 x3, Q19 x2, Q21 x2, Q24 x2)."""
import figs

Q = []


def add(stem, vi, vn, week, lo, topic, q, o, a, why, om, fig=None, alt=""):
    assert len(o) == len(om) and 4 <= len(o) <= 5 and 0 <= a < len(o)
    d = dict(id=f"v2-q{stem}-{vi}", stem=stem, level="medium", vi=vi, vn=vn, week=week, lo=lo, topic=topic,
             q=q, o=o, a=a, why=why, om=om)
    if fig:
        d["fig"] = {"src": "fig/v2/" + fig.split("/fig/v2/")[1], "alt": alt}
    Q.append(d)


# =============================== Q1 DEFINITIONS OF LIFE ===============================
LO1 = "W1: two definitions of life and judging an entity by each"
DEF = ("The textbook defines life by five characteristics: made of cells, reproduces, carries out metabolism, stores genetic "
       "information, and is a product of evolution. NASA's 1994 definition: life is a self-sustaining chemical system capable of "
       "Darwinian evolution.\n\n")
add(1, 1, 2, 1, LO1, "Definitions of life",
    DEF + "A virus is a protein coat around a genome of DNA or RNA. It has no cell membrane and no ribosomes, and it carries out no "
    "chemical reactions until it enters a host cell, which then copies it. Which is the best evaluation of the virus by the "
    "textbook definition?",
    ["Alive: it reproduces and its genome evolves, which covers the five characteristics",
     "Not alive: it is not made of cells and carries out no metabolism of its own",
     "Not alive: it stores no genetic information",
     "Alive: it is made of more than one cell"],
    1,
    "The textbook needs all five characteristics. A virus has genetic information and its lineage evolves, but it is not made of a cell "
    "and runs no metabolism of its own, so it fails the textbook definition. Whether a virus meets NASA's definition is debated, which "
    "is why this card asks about the textbook definition only.",
    ["Two of five is not enough. It still fails 'made of cells' and 'metabolism'.",
     "Correct. Not cellular and no metabolism of its own.",
     "Wrong reason: a virus does store genetic information, in DNA or RNA.",
     "Course trap: 'made of more than one cell' is not one of the five characteristics, and a virus is not made of cells anyway."])

add(1, 2, 2, 1, LO1, "Definitions of life",
    DEF + "A forest fire grows by taking in fuel and oxygen, releases energy as heat and light, and spreads by starting new fires "
    "nearby. Which is the best evaluation?",
    ["Alive by both definitions: it takes in materials, releases energy and makes copies of itself",
     "Alive by the NASA 1994 definition only: it is a self-sustaining chemical system",
     "Alive by the textbook definition only: it has metabolism and reproduces",
     "Alive by neither definition: it is not made of cells, stores no genetic information, and cannot undergo Darwinian evolution"],
    3,
    "Fire looks like metabolism and reproduction, but it has no cells and no genetic information, so it fails the textbook definition. "
    "It also cannot evolve by natural selection: a new fire inherits nothing from the old one, so there are no heritable variations to "
    "select. That fails NASA's definition too. The course ruling: a burning fire is alive by neither.",
    ["Surface resemblance: burning fuel is not cellular metabolism, and spreading is not reproduction with inheritance.",
     "Self-sustaining is not enough. NASA also needs Darwinian evolution, which needs heritable variation, and fire has none.",
     "The textbook also needs cells and genetic information. Fire has neither.",
     "Correct. Course ruling: fire is alive by neither definition."])

# =============================== Q2 VALENCE ===============================
LO2 = "W1: Lewis, bond-line and molecular formulas"
add(2, 1, 2, 1, LO2, "Valence and molecular formulas",
    "Silicon has 4 valence electrons, the same number as carbon. What is the most likely molecular formula of a stable molecule made "
    "only of silicon and hydrogen, with one silicon atom?",
    ["SiH2", "SiH3", "SiH4", "SiH8"],
    2,
    "Same valence electrons means the same bonding pattern. Carbon makes four bonds (CH4), so silicon also needs four more electrons "
    "to fill its octet and makes four single bonds to hydrogen: SiH4.",
    ["Treated silicon like oxygen, which makes two bonds.",
     "Treated silicon like nitrogen, which makes three bonds.",
     "Correct. Four valence electrons, four bonds, like CH4.",
     "Confused the octet (8 electrons) with the number of bonds. Each bond shares one of silicon's electrons."])

add(2, 2, 2, 1, LO2, "Valence and molecular formulas",
    "Sulfur has 6 valence electrons, the same number as oxygen. What is the most likely molecular formula of a stable molecule made "
    "only of sulfur and hydrogen, with one sulfur atom?",
    ["H2S", "SH4", "SH6", "SH"],
    0,
    "Sulfur behaves like oxygen. With 6 valence electrons it needs 2 more to fill its octet, so it forms 2 bonds and keeps two lone "
    "pairs, just as oxygen does in H2O. The answer is H2S. The number of bonds is the valence number (2), not the number of valence "
    "electrons (6).",
    ["Correct. Like H2O: two bonds, two lone pairs.",
     "Four bonds is carbon's pattern, not oxygen's.",
     "Six-bond trap: 6 valence electrons does not mean 6 bonds. Sulfur needs only 2 more electrons.",
     "One bond would leave sulfur one electron short of an octet."])

# =============================== Q6 / Q7 ENZYME D ===============================
LO6 = "W2: chemical interactions shape proteins; four levels of structure and what stabilises each"
ENZ = ("Enzyme D, from a gut bacterium, is a homodimer. Each subunit is a single polypeptide chain of 310 amino acids. Where the two "
       "subunits contact each other, the R group of {r88} 88 on one subunit forms {bond} with the R group of {r142} 142 on the other "
       "subunit. Each subunit's fold is held by a hydrophobic core and hydrogen bonds. ")
HELIX = "The substitution disrupts the alpha helix that contains residue 88, which unfolds the subunit"

p, _ = figs.amino_panel("q6-1", "AKD")
add(6, 1, 2, 2, LO6, "Quaternary vs tertiary structure",
    ENZ.format(r88="lysine", bond="an ionic bond", r142="aspartate") +
    "A mutant form of the enzyme has alanine instead of lysine at position 88. The mutant subunits fold normally but fail to form "
    "dimers, and the enzyme is inactive. The structures of the named amino acids are shown below.\n\nWhich statement best explains "
    "why the mutant subunits fold normally but fail to form dimers?",
    [HELIX,
     "Alanine forms a disulfide bond with aspartate 142 instead of an ionic bond",
     "Alanine's R group is a nonpolar methyl group, so position 88 can no longer form the ionic bond with aspartate 142 that holds the "
     "subunits together; the fold of each subunit does not depend on residue 88",
     "The substitution breaks a peptide bond in the backbone, so the subunit is shorter",
     "Alanine's R group is too large to fit at the interface"],
    2,
    "The stem tells you the fold is fine, so tertiary structure is intact. Residue 88's only job is the ionic bond across the interface, "
    "which is quaternary structure. Alanine's R group is an uncharged methyl, so that ionic bond is gone and the subunits do not stick.",
    ["Trap: secondary structure is held by backbone hydrogen bonds, not R groups, and the stem says the subunit folds normally.",
     "Disulfide bonds form only between two cysteine R groups (S-S).",
     "Correct. Interface bond lost, fold untouched.",
     "A substitution swaps one amino acid for another; the backbone and chain length are unchanged.",
     "Alanine's R group is smaller than lysine's, not larger."],
    p, "Skeletal structures, neutral form, alphabetical: alanine, aspartate, lysine.")

p, _ = figs.amino_panel("q6-2", "CS")
add(6, 2, 2, 2, LO6, "Quaternary vs tertiary structure",
    ENZ.format(r88="cysteine", bond="a disulfide bond", r142="cysteine") +
    "A mutant form of the enzyme has serine instead of cysteine at position 88. The mutant subunits fold normally but fail to form "
    "dimers, and the enzyme is inactive. The structures of the named amino acids are shown below.\n\nWhich statement best explains "
    "why the mutant subunits fold normally but fail to form dimers?",
    ["Changing any amino acid changes every level of structure, so the mutant subunit must be misfolded",
     HELIX,
     "Serine's R group is nonpolar, so it buries itself in the hydrophobic core",
     "Serine's R group ends in -OH instead of -SH, so it cannot form the covalent disulfide bond with cysteine 142 that links the "
     "subunits; residue 88 is at the interface, not in the core"],
    3,
    "Disulfide bonds form only between two -SH groups. Serine is cysteine with O in place of S, so the S-S link across the interface "
    "is lost. The stem says the subunit still folds, so residue 88 matters only for quaternary structure.",
    ["Contradicts the stem, which says the mutant folds normally.",
     "Trap: secondary structure is backbone hydrogen bonds, and the fold is intact.",
     "Serine's -OH makes it polar, not nonpolar.",
     "Correct. No -SH, no disulfide, no dimer."],
    p, "Skeletal structures, neutral form, alphabetical: cysteine (side chain CH2-SH) and serine (side chain CH2-OH).")

LO7 = "W2: chemical interactions shape proteins"
Q7Q = ("A mutant at position 88 fails to form dimers. Which substitution at position 88 would be least likely to prevent dimer "
       "formation? The five options are drawn below, alphabetically.")


def q7(vi, r88, bond, r142, letters, a, why, om, stem_letters):
    names = sorted(figs.AA_NAME[L] for L in letters)
    p, drawn = figs.amino_panel(f"q7-{vi}", letters + stem_letters)   # options plus the residues named in the stem
    add(7, vi, 3, 2, LO7, "Which substitution keeps the interface",
        ENZ.format(r88=r88, bond=bond, r142=r142) + Q7Q.replace("The five options are drawn below, alphabetically.",
        "Every amino acid named here is drawn below, alphabetically."), names, a, why, om,
        p, "Skeletal structures, neutral form, alphabetical, names only: " + ", ".join(n.lower() for n in drawn) + ".")
    assert len(names) == 5


q7(1, "lysine", "an ionic bond", "aspartate", "ARDLS", 1,
   "Aspartate 142 is negative, so position 88 needs a positive R group to keep the ionic bond. Arginine's R group ends in a "
   "nitrogen-rich group that is positive at pH 7.4, just like lysine's amine.",
   ["Nonpolar methyl: no charge, no ionic bond.",
    "Correct. Positive R group, so the ionic bond with aspartate survives.",
    "Negative next to negative: it would repel aspartate 142.",
    "Nonpolar: no charge to pair with aspartate.",
    "Polar but uncharged. An -OH cannot replace a full ionic bond."], "K")
q7(2, "aspartate", "an ionic bond", "lysine", "NEGKT", 1,
   "Lysine 142 is positive, so position 88 needs a negative R group. Glutamate has a carboxyl on its R group, like aspartate, and is "
   "negative at pH 7.4.",
   ["Look-alike trap: asparagine ends in an amide, which is uncharged. It looks like aspartate but carries no negative charge.",
    "Correct. Carboxyl R group, negative, pairs with lysine.",
    "Glycine's R group is just H: no charge.",
    "Positive next to positive: it would repel lysine 142.",
    "Polar but uncharged. An -OH cannot replace a full ionic bond."], "D")
q7(3, "serine", "a hydrogen bond", "glutamine", "ACLFT", 4,
   "Serine's -OH hydrogen bonds with glutamine's amide. Threonine also has an -OH on a small R group, so it can make the same "
   "hydrogen bond.",
   ["Nonpolar methyl: no hydrogen bond.",
    "Course ruling: S-H is treated as nonpolar (electronegativity difference 0.38), so cysteine's -SH does not hydrogen bond here.",
    "Nonpolar: no hydrogen bond.",
    "Nonpolar ring: no hydrogen bond, and much bulkier than serine.",
    "Correct. Another small R group with an -OH."], "SQ")

# =============================== Q9 NET CHARGE ===============================
LO9 = "W2: functional groups"
NC_O = ["−2", "−1", "0", "+1", "+2"]
NC_Q = "The structure of Molecule Q is shown below. What is the most likely net charge of Molecule Q at physiological pH (7.4)?"
p, _ = figs.peptide("q9-1", "E")
add(9, 1, 3, 2, LO9, "Net charge from functional groups", NC_Q, NC_O, 1,
    "Count only groups that ionize. The amine is basic: +1. Two carboxyl groups are acidic: −1 each. Net: +1 − 1 − 1 = −1.",
    ["Counted a third negative group. There are only two carboxyls.",
     "Correct. One amine (+1), two carboxyls (−2).",
     "Counted only the backbone amine and carboxyl and missed the carboxyl on the side chain.",
     "Swapped the signs: carboxyls are acidic and lose H+, so they are negative.",
     "Treated the carboxyls as basic."],
    p, "Skeletal structure, neutral form, no charges drawn: an amino acid whose side chain is CH2-CH2-COOH.")

p, _ = figs.peptide("q9-2", "KN")
add(9, 2, 3, 2, LO9, "Net charge from functional groups", NC_Q, NC_O, 3,
    "In a peptide, count the free amino end (+1), the free carboxyl end (−1) and any charged R groups. One R group ends in an amine "
    "(+1). The other ends in an amide, which is uncharged, and the peptide bond is an amide too, also uncharged. Net: +1 + 1 − 1 = +1.",
    ["Too negative: counted amides as acidic.",
     "Missed the amine at the end of the side chain.",
     "Counted only the two ends and missed the charged side chain.",
     "Correct. Two amines (+2), one carboxyl (−1); amides are 0.",
     "Amide trap: counted an amide as basic. Amides are uncharged polar."],
    p, "Skeletal structure, neutral form, no charges drawn: a dipeptide. One side chain ends in NH2 on a CH2 chain; the other ends in a C(=O)NH2 amide.")

p = figs.molecule("q9-3", "SCCNC(=O)COP(=O)(O)O", "C4H10NO5PS")
add(9, 3, 3, 2, LO9, "Net charge from functional groups", NC_Q, NC_O, 0,
    "The terminal phosphate group loses two H+ at pH 7.4: −2. The thiol (-SH) and the amide are uncharged. Net: −2.",
    ["Correct. Terminal phosphate −2; amide and thiol 0.",
     "Counted the phosphate as −1. A terminal phosphate is −2.",
     "Missed the phosphate's charge.",
     "Amide trap: an amide is uncharged, not basic.",
     "Treated the phosphate as basic."],
    p, "Skeletal structure, neutral form, no charges drawn: HS-CH2-CH2-NH-C(=O)-CH2-O-PO3H2.")

# =============================== Q14 DNA PAIRING ===============================
LO14 = "W2: nucleotides and nucleic acids"
Q14 = ("A researcher synthesizes four short single-stranded DNA molecules. All are written 5' to 3' in the table below.\n\n"
       "She mixes the strands two at a time, and also tests each strand on its own (two copies of the same strand can meet). "
       "Which would form a double helix in which all 8 bases are paired?")


def rc(s):
    return s[::-1].translate(str.maketrans("ATGC", "TACG"))


def q14(vi, strands, answer_pairs, o, a, why, om):
    found = [(i + 1, j + 1) for i in range(4) for j in range(i, 4) if rc(strands[i]) == strands[j]]
    assert found == answer_pairs, (vi, found)
    p = figs.table(f"q14-{vi}", ["Strand", "Sequence"], [[str(i + 1), "5'-" + s + "-3'"] for i, s in enumerate(strands)])
    add(14, vi, 3, 2, LO14, "Antiparallel base pairing", Q14, o, a, why, om,
        p, "Table of four strands, each written 5' to 3': " + "; ".join(f"strand {i+1} 5'-{s}-3'" for i, s in enumerate(strands)))


S1 = "AGTCCATG"
q14(1, [S1, rc(S1), S1.translate(str.maketrans("ATGC", "TACG")), "GGATTCAC"], [(1, 2)],
    ["Strands 1 and 2 only", "Strands 1 and 3 only", "Strands 1 and 2, and strands 1 and 3", "Strands 2 and 4 only", "None of them"], 0,
    "Strands pair antiparallel: read one strand 5' to 3' and its partner 3' to 5'. Reverse strand 2 and it reads 3'-TCAGGTAC-5', which "
    "pairs base for base with strand 1 (A-T, G-C). Strand 3 is the complement of strand 1 written in the same direction, so it could only "
    "pair if the strands ran parallel, which DNA does not do.",
    ["Correct. The antiparallel partner.",
     "Parallel decoy: strand 3 matches strand 1 only if both run 5' to 3' side by side.",
     "Strand 3 is the parallel decoy, so only 1 and 2 work.",
     "Check every pair against the reversed partner: 2 and 4 mismatch.",
     "Strand 2 is a perfect antiparallel partner for strand 1."])
q14(2, ["ACGTACGT", "TTGACCAG", "GTCAAGTC", "CAGGTTCA"], [(1, 1)],
    ["Strand 1 on its own (two copies pair with each other)", "Strands 1 and 3", "Strands 2 and 4", "None: a strand cannot pair with a copy of itself"], 0,
    "Strand 1 is a palindrome in the DNA sense: its reverse complement is itself (5'-ACGTACGT-3' read backwards and complemented gives "
    "ACGTACGT). Two copies of strand 1 therefore form a fully paired double helix. No other strand or pair matches all 8 bases.",
    ["Correct. Self-complementary strand.",
     "Reverse strand 3 and compare: several bases mismatch.",
     "Strand 4 reversed does not complement strand 2 at every base.",
     "A self-complementary sequence pairs with a second copy of itself."])
q14(3, [S1, "CATGCACT", S1.translate(str.maketrans("ATGC", "TACG")), "GACTTGGA"], [],
    ["Strands 1 and 2", "Strands 1 and 3", "Strands 1 and 4", "None of them"], 3,
    "Strand 2 is almost the antiparallel partner of strand 1, but one base is wrong: position 5 of strand 2 is C, where a perfect "
    "partner would have G, opposite the C in strand 1. Strand 3 only matches in the parallel direction. So no pair gets all 8 bases paired.",
    ["One-mismatch trap: 7 of 8 pair, but the question asks for all 8.",
     "Parallel decoy: strand 3 matches strand 1 only side by side in the same direction.",
     "Strand 4 does not complement strand 1 when reversed.",
     "Correct. Every candidate has at least one mismatch."])

# =============================== Q19 MEMBRANE FLUIDITY ===============================
LO19 = "W3: phospholipid structure to bilayer function"
Q19 = ("Some organisms have adaptations to keep their membranes fluid in the face of temperature changes. Like membrane permeability, "
       "membrane fluidity is influenced by noncovalent interactions between fatty acid tails. Membrane phospholipids were extracted from "
       "two fish species: one lives in Arctic water near 0 °C, the other on tropical reefs near 28 °C. The fatty acid composition is in "
       "the table below.\n\nWhich species most likely lives in the Arctic, and why?")
p = figs.table("q19-1", ["", "Species A", "Species B"],
               [["Saturated tails (%)", "70", "35"], ["Unsaturated tails (%)", "30", "65"], ["Average tail length (carbons)", "18", "18"]])
add(19, 1, 2, 3, LO19, "Membrane fluidity: saturation and tail length", Q19,
    ["Species A, because saturated tails pack tightly and keep the membrane warm",
     "Species B, because the kinks at double bonds in unsaturated tails stop them packing tightly, so the membrane stays fluid in the cold",
     "Species B, because unsaturated tails form more hydrogen bonds with water",
     "Species A, because saturated tails make the membrane more fluid"],
    1,
    "Tail length is equal, so unsaturation decides it. Double bonds put kinks in the tails, the tails cannot pack closely, and there are "
    "fewer London dispersion interactions between them. That keeps the membrane fluid at low temperature. The Arctic fish has more "
    "unsaturated tails: species B.",
    ["Membranes do not generate heat; tight packing makes a membrane stiffer in the cold.",
     "Correct. Kinks, looser packing, fewer dispersion forces.",
     "Fatty acid tails are nonpolar and sit inside the bilayer; they do not hydrogen bond with water.",
     "Backwards: saturated tails pack tightly and make the membrane less fluid."],
    p, "Table: species A 70% saturated, 30% unsaturated, average tail 18 carbons; species B 35% saturated, 65% unsaturated, average tail 18 carbons.")

p = figs.table("q19-2", ["", "Species A", "Species B"],
               [["Saturated tails (%)", "50", "50"], ["Unsaturated tails (%)", "50", "50"], ["Average tail length (carbons)", "14", "20"]])
add(19, 2, 2, 3, LO19, "Membrane fluidity: saturation and tail length", Q19,
    ["Neither can be identified, because both have the same percentage of unsaturated tails",
     "Species B, because longer tails have more London dispersion interactions, which keeps the membrane fluid",
     "Species A, because shorter tails have fewer London dispersion interactions with each other, so the membrane stays fluid in the cold",
     "Species A, because shorter tails form more hydrogen bonds"],
    2,
    "Saturation is equal here, so tail length decides it. Shorter tails have less surface to touch neighbouring tails, so there are fewer "
    "London dispersion interactions holding them together and the membrane stays fluid when cold. Saturation and tail length are two "
    "separate levers, as with coconut oil.",
    ["Course fact: saturation and tail length are two separate levers. Equal saturation leaves length to decide.",
     "Backwards: more dispersion interactions hold tails together and make the membrane less fluid.",
     "Correct. Short tails, fewer dispersion forces, more fluid.",
     "Fatty acid tails are nonpolar; they do not hydrogen bond."],
    p, "Table: species A 50% saturated, 50% unsaturated, average tail 14 carbons; species B 50% saturated, 50% unsaturated, average tail 20 carbons.")

# =============================== Q21 THERMODYNAMICS OF A PROCESS ===============================
LO21 = "W4: thermodynamics and spontaneity"
add(21, 1, 2, 4, LO21, "Thermodynamics of biological processes",
    "A newly made polypeptide folds on its own, in water, into its native shape, with its hydrophobic R groups buried in the core. "
    "Which statement best describes the thermodynamics of this process?",
    ["ΔG > 0, because the folded protein is more ordered than the unfolded chain",
     "ΔG < 0, because folding forms many new covalent bonds that release heat",
     "ΔG < 0: the chain itself becomes more ordered, but water molecules freed from around the hydrophobic R groups gain much more entropy",
     "ΔG = 0, because folding can be reversed",
     "ΔG < 0, because the polypeptide chain itself gains entropy as it folds"],
    2,
    "It happens on its own, so ΔG is negative. The chain loses entropy as it folds, but before folding, water formed ordered cages around "
    "the exposed hydrophobic R groups. Burying those groups frees the water, and that entropy gain is larger. The interactions in the fold "
    "are noncovalent.",
    ["Looks only at the chain. Count the water too: overall entropy rises, and folding is spontaneous.",
     "Folding is held by noncovalent interactions, not new covalent bonds.",
     "Correct. Chain more ordered, water much less ordered, ΔG negative.",
     "Reversible does not mean ΔG = 0. ΔG = 0 only at equilibrium.",
     "The folded chain is more ordered, so its own entropy falls."])

add(21, 2, 2, 4, LO21, "Thermodynamics of biological processes",
    "Cells make ATP from ADP and inorganic phosphate (ADP + Pi → ATP + H2O). Which statement best describes the thermodynamics of "
    "this process?",
    ["ΔG < 0: it happens on its own because cells need ATP",
     "ΔG > 0: it does not happen on its own and must be coupled to an exergonic process, such as H+ flowing down its gradient",
     "ΔG > 0, so it can never happen in a cell",
     "ΔG < 0, because forming a new bond always releases energy",
     "Whether ΔG is positive or negative depends on whether the enzyme ATP synthase is present"],
    1,
    "ATP hydrolysis is exergonic, so the reverse, ATP synthesis, is endergonic (ΔG > 0). It still happens in cells because it is coupled "
    "to a favourable process. In mitochondria and chloroplasts, H+ flowing down its gradient through ATP synthase pays for it.",
    ["Need does not set ΔG. ATP synthesis is the reverse of an exergonic reaction.",
     "Correct. Endergonic, made possible by coupling.",
     "Endergonic reactions do happen in cells when coupled to exergonic ones.",
     "Overall ΔG counts the bonds broken and the order created, not just one bond formed.",
     "Enzymes change rate, never ΔG."])

# =============================== Q24 ENZYME CLAIMS ===============================
LO24 = "W4: how enzymes speed reactions"
add(24, 1, 2, 4, LO24, "What an enzyme can and cannot do",
    "The reaction M → N has a ΔG of about +25 kJ/mol under conditions in the cell. A biotech startup claims it has engineered an enzyme "
    "so efficient that cells using it convert M into N with nothing else needed. Which is the best evaluation of this claim?",
    ["Plausible: a fast enough enzyme can overcome a positive ΔG",
     "Plausible: enzymes supply the energy that drives a reaction forward",
     "Not possible: an enzyme lowers activation energy but does not change ΔG, so a reaction with positive ΔG still will not go forward "
     "unless it is coupled to an exergonic reaction",
     "Not possible: enzymes only work on reactions whose ΔG is zero"],
    2,
    "Enzymes change how fast a reaction reaches equilibrium, never which direction is favoured. With ΔG positive, M → N will not go "
    "forward on its own however good the enzyme. It would need coupling to something exergonic, such as ATP hydrolysis.",
    ["Speed and direction are separate. No enzyme turns a positive ΔG negative.",
     "Enzymes are not an energy source; they are unchanged after the reaction.",
     "Correct. Enzymes do not change ΔG.",
     "Enzymes speed up reactions with any ΔG; a negative ΔG is what makes the forward direction favourable."])

add(24, 2, 2, 4, LO24, "What an enzyme can and cannot do",
    "Hydrolysis of the peptide bond in a dipeptide has a ΔG of about −10 kJ/mol, but without a catalyst it takes years. A biotech startup "
    "claims it has engineered an enzyme that makes this hydrolysis a million times faster. Which is the best evaluation of this claim?",
    ["Not possible: if the reaction were favourable, it would already be fast",
     "Not possible: enzymes decide whether a reaction happens, not how fast",
     "Plausible, but only because the enzyme makes ΔG more negative",
     "Plausible: the reaction is exergonic but has a high activation energy, and enzymes speed reactions by lowering activation energy"],
    3,
    "Peptide bond hydrolysis is exergonic but very slow, because its activation energy is high. That is exactly the case an enzyme helps: "
    "by stabilizing the transition state it lowers the activation energy, and million-fold speed-ups are normal for enzymes. ΔG is unchanged.",
    ["ΔG says which direction is favoured, not how fast. Activation energy sets the rate.",
     "Backwards: enzymes change rate, not whether a reaction is favourable.",
     "Enzymes never change ΔG.",
     "Correct. Exergonic, slow, so an enzyme can speed it up."])

if __name__ == "__main__":
    import json, collections
    c = collections.Counter(q["stem"] for q in Q)
    print(len(Q), dict(c))
    assert dict(c) == {1: 2, 2: 2, 6: 2, 7: 3, 9: 3, 14: 3, 19: 2, 21: 2, 24: 2}
    for q in Q:
        assert q["vn"] == c[q["stem"]]
        txt = q["q"] + " ".join(q["o"]) + q["why"] + " ".join(q["om"])
        assert "—" not in txt and "–" not in txt, q["id"]
    json.dump(Q, open("build/medium.json", "w"), ensure_ascii=False, indent=1)
    for q in Q:
        if "fig" in q:
            figs.png_of(figs.FIG + "/" + q["fig"]["src"].split("/")[-1])
    print("ok")
