"""Tier 4: Just-in-Case, 17 questions (brief Step 6 items 1, 3, 5, 8, 9, 11, 13, 14, 15, 16, 17, 18, 19, 20, 23, 24, 25)."""
import figs
from rdkit import Chem
from rdkit.Chem.rdMolDescriptors import CalcMolFormula

Q = []


def add(n, week, topic, q, o, a, why, om, fig=None, alt=""):
    assert len(o) == len(om) and 4 <= len(o) <= 5 and 0 <= a < len(o)
    d = dict(id=f"v2-jic-{n}", stem=None, level="jic", jic=n, week=week, lo="Just in case", topic=topic,
             q=q, o=o, a=a, why=why, om=om)
    if fig:
        d["fig"] = {"src": "fig/v2/" + fig.split("/fig/v2/")[1], "alt": alt}
    Q.append(d)


add(1, 1, "Prokaryote vs eukaryote parts",
    "A newly discovered single-celled organism has a plasma membrane, ribosomes and DNA, but no nucleus and no membrane-bound "
    "organelles. Which structure would you expect to find in BOTH this organism and a human liver cell?",
    ["Ribosomes", "A nucleus", "Lysosomes", "Mitochondria", "Endoplasmic reticulum"], 0,
    "This is a prokaryote. Prokaryotes and eukaryotes share a plasma membrane, DNA and ribosomes. The nucleus and membrane-bound "
    "organelles (mitochondria, ER, lysosomes) are eukaryote only, and the course key treats lysosomes as animal cells only.",
    ["Correct. Every cell makes proteins on ribosomes.",
     "The stem says no nucleus: that is what makes it a prokaryote.",
     "Membrane-bound organelle: eukaryote only (animal cells, per the course key).",
     "Membrane-bound organelle: eukaryote only.",
     "Membrane-bound organelle: eukaryote only."])

smi3 = "C=CC(O)CC(=O)N"
f3 = CalcMolFormula(Chem.MolFromSmiles(smi3))
assert f3 == "C5H9NO2"
p = figs.molecule("jic-3", smi3, f3)
add(3, 1, "Molecular formula from a bond-line structure",
    "What is the molecular formula of the molecule drawn below?",
    ["C5H9NO2", "C5H5NO2", "C4H9NO2", "C5H11NO2", "C5H9NO"], 0,
    "In a bond-line drawing every corner and line end is a carbon (5 here), and each carbon carries enough implied H to make four bonds. "
    "Count them: CH2= (2), =CH (1), CH with OH (1), CH2 (2), and the C=O carbon (0) give 6 H on carbon, plus 1 on O and 2 on N: 9 H. "
    "One N, two O.",
    ["Correct. 5 C, 9 H, 1 N, 2 O.",
     "Counted only the H atoms that are drawn and missed the implied ones on carbon.",
     "Missed a carbon at a line end or corner.",
     "Treated the C=C double bond as single, adding two H.",
     "Missed the O in the C=O, or the one in the OH."],
    p, "Bond-line structure, no implied hydrogens drawn: CH2=CH-CH(OH)-CH2-C(=O)-NH2.")

add(5, 1, "Course ruling: which bonds are polar",
    "Using the course's electronegativity values (O 3.44, N 3.04, S 2.58, C 2.55, H 2.20), which of these bonds does the course "
    "classify as POLAR: C-O, O-H, S-H, C-H?",
    ["C-O and O-H only", "C-O, O-H and S-H", "O-H only", "All four", "S-H and C-H only"], 0,
    "A bond is polar when the electronegativity difference is large. O-H differs by 1.24 and C-O by 0.89: polar. S-H differs by only "
    "0.38 and C-H by 0.35, so the course treats both as nonpolar. Ranked most to least polar: O-H, C-O, S-H, C-H.",
    ["Correct. Course ruling: S-H is nonpolar.",
     "S-H trap: the course treats S-H as nonpolar (difference 0.38).",
     "C-O is polar too (difference 0.89).",
     "C-H and S-H are nonpolar.",
     "Backwards: these are the two nonpolar ones."])

add(8, 1, "Blood buffers and protein shape",
    "During intense exercise, muscles release acid into the blood, yet blood pH stays close to 7.4. What best explains this, and why "
    "does it matter?",
    ["Buffers in the blood take up the extra H+, keeping pH near 7.4; a large pH swing would change the charges on R groups, "
     "disrupting ionic interactions and protein shape",
     "Water is basic, so it neutralizes any acid added to blood",
     "Blood has no buffers, but pH does not matter to proteins because their peptide bonds are covalent",
     "The extra H+ bonds covalently to proteins, which removes it from the blood with no effect on them"], 0,
    "Buffers soak up or release H+ so pH barely moves. That matters because acidic and basic R groups gain or lose H+ as pH changes, "
    "which changes their charges, breaks ionic interactions and can unfold proteins.",
    ["Correct. Buffers hold pH; pH controls R-group charges and protein shape.",
     "Pure water is neutral (pH 7), not basic.",
     "Shape depends on noncovalent interactions, which pH does disrupt.",
     "H+ is taken up reversibly by buffers; and changing protein charges does affect proteins."])

add(9, 2, "Which functional groups are charged",
    "A drug molecule contains one amine, one amide, one carboxyl and one hydroxyl group. Which of these groups carry a charge at pH 7.4?",
    ["All four", "The amine (+1) and the carboxyl (−1) only", "The amine and the amide (+1 each), and the carboxyl (−1)",
     "Only the carboxyl (−1)", "The amide and the hydroxyl only"], 1,
    "Amines are basic and pick up H+ (+1). Carboxyls are acidic and lose H+ (−1). Amides and hydroxyls are polar but uncharged.",
    ["Amides and hydroxyls are polar but not charged.",
     "Correct. Amine +1, carboxyl −1.",
     "Amide trap: an amide looks like an amine but is uncharged.",
     "The amine is charged too.",
     "These are the two uncharged polar groups."])

add(11, 2, "Macromolecules and their linkages",
    "Which macromolecule and linkage pairing is INCORRECT?",
    ["Proteins: peptide bonds between amino acids",
     "Nucleic acids: phosphodiester linkages between nucleotides",
     "Starch: glycosidic linkages between sugars",
     "Fats (triglycerides): ester linkages between glycerol and fatty acids",
     "Cellulose: peptide bonds between sugars"], 4,
    "Proteins use peptide bonds, nucleic acids phosphodiester linkages, carbohydrates glycosidic linkages, and fats ester linkages. "
    "Cellulose is a carbohydrate, so its sugars are joined by glycosidic linkages, not peptide bonds.",
    ["True.", "True.", "True.", "True.", "Correct (the incorrect pairing). Cellulose uses glycosidic linkages."])

add(13, 2, "Naming quaternary structure",
    "Hemoglobin is made of four polypeptide chains: two identical alpha chains and two identical beta chains. How is its quaternary "
    "structure described?",
    ["Homotetramer", "Heterotetramer", "Heterodimer", "Homodimer", "It has no quaternary structure"], 1,
    "Count the chains (four: tetramer) and ask whether they are all the same (homo) or not (hetero). Alpha and beta differ, so it is a "
    "heterotetramer.",
    ["Homo would mean all four chains are identical; alpha and beta are different.",
     "Correct. Four chains, two kinds.",
     "Dimer means two chains; there are four.",
     "Two errors: four chains, and not all the same.",
     "Any protein with more than one chain has quaternary structure."])

add(14, 2, "Reading SDS-PAGE bands",
    "A sample is boiled in SDS with a reducing agent and run on SDS-PAGE. Stained for protein, it shows one dark band at 40 kDa and one "
    "faint band at 25 kDa. Which conclusion is best supported?",
    ["The sample contains polypeptides of two different sizes, with much more of the 40 kDa one",
     "The 25 kDa polypeptide is larger, because it travelled farther",
     "The 40 kDa band must contain two different polypeptides, because it is dark",
     "The faint band ran faster because it is more highly charged",
     "The sample contains exactly two polypeptide molecules"], 0,
    "Number of bands = number of different sizes. Position = size (small runs farther, toward the bottom). Darkness = amount. So two "
    "sizes, and far more of the 40 kDa one.",
    ["Correct. Two sizes; dark means more.",
     "Backwards: smaller polypeptides run farther.",
     "Darkness shows amount, not how many kinds are in the band.",
     "SDS gives every polypeptide the same charge-to-size ratio, so size alone decides position.",
     "A band holds huge numbers of molecules; it shows sizes, not counts of molecules."])

p, _ = figs.amino_panel("jic-15", "EGK")
add(15, 2, "Gels without SDS sort by charge",
    "Three peptides of the same length (20 residues each) are made: one entirely of glutamate, one entirely of lysine, and one entirely "
    "of glycine (structures below). They are run on a gel WITHOUT SDS at pH 7.4, with the positive electrode at the bottom. Which runs "
    "farthest toward the bottom?",
    ["The lysine peptide", "The glutamate peptide", "The glycine peptide", "All three run the same distance, because they are the same length"], 1,
    "Without SDS, a polypeptide keeps its own charge, and charge decides direction. Glutamate's R group carries a carboxyl (−1 each), so "
    "the poly-glutamate peptide is strongly negative and moves farthest toward the positive electrode.",
    ["Lysine's R groups are positive, so that peptide moves the other way.",
     "Correct. Most negative, runs farthest toward +.",
     "Glycine's R group is H: uncharged, so it barely moves.",
     "SDS thinking: without SDS, charge, not size, decides."],
    p, "Skeletal structures, neutral form, alphabetical: glutamate, glycine, lysine.")

add(16, 2, "Cross-linking reveals subunit number",
    "A protein gives a single 30 kDa band on SDS-PAGE with a reducing agent. Researchers then treat the native protein with a chemical "
    "that covalently links subunits that touch each other, and run SDS-PAGE again. Now they see bands at 30, 60 and 90 kDa. What is the "
    "best conclusion?",
    ["The native protein is a homotrimer of 30 kDa subunits",
     "The native protein contains three different subunits",
     "The native protein is a single 90 kDa chain",
     "The native protein is a homodimer",
     "The cross-linker added 30 kDa of mass each time it reacted"], 0,
    "Every subunit is 30 kDa (one band without cross-linking, so all subunits are the same size). Cross-linking that is not complete "
    "traps monomers, dimers and trimers: 30, 60, 90. The largest product, 90, shows three subunits in the native protein.",
    ["Correct. Largest cross-linked product = whole complex.",
     "Without cross-linking there is only one band size, so the subunits are the same size.",
     "Then it would run at 90 kDa even without cross-linking.",
     "A dimer would give 30 and 60 at most.",
     "Cross-linkers are small; the steps of 30 kDa come from whole subunits."])

p, _ = figs.amino_panel("jic-17", "LD")
add(17, 2, "The hydrophobic core",
    "In a soluble enzyme, a leucine buried in the hydrophobic core is replaced by aspartate (structures below). What is the most likely "
    "effect?",
    ["No effect: residues inside the core do not affect folding",
     "The protein folds more tightly, because aspartate forms hydrogen bonds in the core",
     "The charged R group inside the nonpolar core disrupts the hydrophobic interactions, so the protein is likely to misfold",
     "Only the primary structure changes; the tertiary structure cannot change"], 2,
    "The core is held together by hydrophobic interactions among nonpolar R groups. Aspartate's R group is charged at pH 7.4 and does not "
    "belong there, so the core is disrupted and the protein is likely to misfold. Misfolded proteins can expose hydrophobic patches and "
    "aggregate, which is what prions do, and chaperones help proteins avoid this.",
    ["The core is exactly what holds the fold together.",
     "A charge buried in a nonpolar core is destabilizing.",
     "Correct. Charged R group in the hydrophobic core.",
     "Primary structure determines the higher levels; changing it can change the fold."],
    p, "Skeletal structures, neutral form, alphabetical: aspartate and leucine.")

smi18 = "Nc1ncnc2c1ncn2C1OC(COP(=O)(O)O)C(O)C1O"
p = figs.molecule("jic-18", smi18, "C10H14N5O7P")
add(18, 2, "DNA or RNA from the structure",
    "The nucleotide shown below was isolated from a newly discovered virus. Which conclusion is best supported?",
    ["It comes from RNA, because its sugar has an -OH on the 2' carbon; its base, with two rings, is a purine",
     "It comes from DNA, because it has a phosphate group",
     "It comes from RNA, because its base has two rings",
     "It comes from DNA; its base, with one ring, is a pyrimidine"], 0,
    "DNA and RNA differ at the sugar's 2' carbon: RNA's ribose has an -OH there, DNA's deoxyribose has only H. This sugar has the 2' -OH. "
    "The base has two fused rings, so it is a purine; purines (A, G) occur in both DNA and RNA.",
    ["Correct. 2' -OH means ribose; two rings means purine.",
     "Both DNA and RNA nucleotides have phosphate.",
     "Right answer, wrong reason: purines occur in DNA too. The sugar decides.",
     "The base has two fused rings, and the sugar has a 2' -OH."],
    p, "Skeletal structure of a nucleotide: a two-ring nitrogenous base attached to a five-membered sugar ring carrying OH groups on the two carbons next to each other, plus a CH2-O-phosphate.")

add(19, 2, "RNA stem-loops",
    "A single RNA strand has the sequence 5'-GGCAUAUUUGCC-3'. On its own, what structure is it most likely to form?",
    ["A stem-loop (hairpin): GGCA at the 5' end pairs with UGCC at the 3' end, antiparallel, leaving UAUU as an unpaired loop",
     "None: RNA is always single-stranded and never pairs with itself",
     "A double helix, but only with a second, identical strand",
     "A stem in which GGCA pairs with GGCA"], 0,
    "RNA can pair with itself. Read the 3' end backwards: C-C-G-U. That pairs with G-G-C-A at the 5' end (G-C, G-C, C-G, A-U), antiparallel. "
    "The four bases between them, UAUU, form the loop.",
    ["Correct. Intra-strand pairing makes a hairpin.",
     "RNA folds by pairing with itself, as in tRNA.",
     "It can pair with itself on one strand; no partner is needed.",
     "G pairs with C, not G, and the pairing must be antiparallel."])

add(20, 3, "Alpha vs beta linkages",
    "Starch and cellulose are both polymers of the same six-carbon sugar. Humans digest starch easily but cannot digest cellulose. What "
    "best explains this?",
    ["Cellulose is made of a different sugar",
     "Our digestive enzymes fit the alpha glycosidic linkages of starch but not the beta glycosidic linkages of cellulose",
     "Cellulose is held together by peptide bonds",
     "Starch molecules are smaller than cellulose molecules"], 1,
    "Same monomer, different linkage. Starch (and glycogen) use alpha linkages; cellulose uses beta linkages, which give a different "
    "shape. Enzymes are specific to shape, and human enzymes only fit the alpha linkage.",
    ["The stem says they are polymers of the same sugar.",
     "Correct. Enzyme shape matches the alpha linkage.",
     "Polysaccharides use glycosidic linkages.",
     "Size is not the issue; linkage geometry is."])

add(23, 3, "Types of membrane transport",
    "Intestinal cells take up sugar through a carrier protein that also brings in Na+. Na+ moves down its concentration gradient into the "
    "cell while the sugar moves up its concentration gradient. How is the sugar's transport best classified?",
    ["Simple diffusion", "Facilitated diffusion, because a carrier protein is used",
     "Active transport: energy released by Na+ moving down its gradient pays for moving the sugar against its gradient", "Osmosis"], 2,
    "Moving something against (up) its gradient always needs energy, so it is active transport, even though no ATP is used here. Na+ "
    "flowing down its gradient is exergonic and pays for the endergonic sugar movement (course fact: the Na+/glucose symporter).",
    ["Simple diffusion goes down a gradient without a protein.",
     "Trap: a carrier alone does not make it facilitated. Facilitated diffusion goes down the gradient.",
     "Correct. Against the gradient = active.",
     "Osmosis is the movement of water."])

add(24, 4, "Activation energy, not ΔG, sets the rate",
    "Hydrolysis of peptide bonds has a negative ΔG, yet a protein kept in sterile water can last for years. What best explains this?",
    ["ΔG becomes positive once the protein is in water",
     "The reaction is already at equilibrium",
     "Its activation energy is very high, so without a catalyst the reaction is extremely slow",
     "Peptide bonds are hydrolyzed by condensation, which needs no water"], 2,
    "A negative ΔG says the reaction is favourable, not fast. The rate depends on the activation energy, which is high for peptide bond "
    "hydrolysis. That is why digestion needs enzymes (proteases).",
    ["ΔG for this hydrolysis is negative in water.",
     "If it were at equilibrium there would be no net change to explain; the protein is far from equilibrium.",
     "Correct. Favourable but slow.",
     "Hydrolysis uses water; condensation releases it."])

add(25, 4, "Equilibrium and Le Chatelier",
    "In blood, CO2 + H2O ⇌ H2CO3. Which statement about this reaction at equilibrium is correct, and what happens when extra H2CO3 is added?",
    ["At equilibrium the amounts of reactants and products are equal; adding H2CO3 shifts the reaction to the right",
     "At equilibrium both reactions stop; adding H2CO3 restarts the forward reaction",
     "At equilibrium the forward and reverse rates are equal; adding H2CO3 shifts the reaction to the left, making more CO2 and H2O",
     "At equilibrium the forward and reverse rates are equal; adding H2CO3 shifts the reaction to the right"], 2,
    "Equilibrium means the forward and reverse reactions run at the same rate, not that the amounts are equal. Adding product pushes the "
    "reaction back toward reactants (Le Chatelier): to the left.",
    ["Equal rates, not equal amounts; and adding product shifts it left.",
     "Both reactions keep running at equilibrium; they just balance.",
     "Correct. Equal rates; added product shifts left.",
     "Right definition, wrong direction: added product shifts left."])

if __name__ == "__main__":
    import json
    nums = sorted(q["jic"] for q in Q)
    assert nums == [1, 3, 5, 8, 9, 11, 13, 14, 15, 16, 17, 18, 19, 20, 23, 24, 25], nums
    for q in Q:
        txt = q["q"] + " ".join(q["o"]) + q["why"] + " ".join(q["om"])
        assert "—" not in txt and "–" not in txt, q["id"]
    s = "GGCAUAUUUGCC"; comp = {"G": "C", "C": "G", "A": "U", "U": "A"}
    assert all(comp[s[i]] == s[-1 - i] for i in range(4))  # stem pairs check
    json.dump(Q, open("build/jic.json", "w"), ensure_ascii=False, indent=1)
    for q in Q:
        if "fig" in q:
            figs.png_of(figs.FIG + "/" + q["fig"]["src"].split("/")[-1])
    print(len(Q), "ok")
