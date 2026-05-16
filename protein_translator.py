# Project 3 - Protein Translator
# Made by: Dhanushree Dabgotra
# Class 12 Student - Jammu & Kashmir
# Real world use: Drug discovery,
# vaccine design, genetic research

# Codon table - DNA to Amino Acid
codon_table = {
    'TTT': 'Phe', 'TTC': 'Phe',
    'TTA': 'Leu', 'TTG': 'Leu',
    'CTT': 'Leu', 'CTC': 'Leu',
    'CTA': 'Leu', 'CTG': 'Leu',
    'ATT': 'Ile', 'ATC': 'Ile',
    'ATA': 'Ile', 'ATG': 'Met',
    'GTT': 'Val', 'GTC': 'Val',
    'GTA': 'Val', 'GTG': 'Val',
    'TCT': 'Ser', 'TCC': 'Ser',
    'TCA': 'Ser', 'TCG': 'Ser',
    'CCT': 'Pro', 'CCC': 'Pro',
    'CCA': 'Pro', 'CCG': 'Pro',
    'ACT': 'Thr', 'ACC': 'Thr',
    'ACA': 'Thr', 'ACG': 'Thr',
    'GCT': 'Ala', 'GCC': 'Ala',
    'GCA': 'Ala', 'GCG': 'Ala',
    'TAT': 'Tyr', 'TAC': 'Tyr',
    'TAA': 'Stop','TAG': 'Stop',
    'CAT': 'His', 'CAC': 'His',
    'CAA': 'Gln', 'CAG': 'Gln',
    'AAT': 'Asn', 'AAC': 'Asn',
    'AAA': 'Lys', 'AAG': 'Lys',
    'GAT': 'Asp', 'GAC': 'Asp',
    'GAA': 'Glu', 'GAG': 'Glu',
    'TGT': 'Cys', 'TGC': 'Cys',
    'TGA': 'Stop','TGG': 'Trp',
    'CGT': 'Arg', 'CGC': 'Arg',
    'CGA': 'Arg', 'CGG': 'Arg',
    'AGT': 'Ser', 'AGC': 'Ser',
    'AGA': 'Arg', 'AGG': 'Arg',
    'GGT': 'Gly', 'GGC': 'Gly',
    'GGA': 'Gly', 'GGG': 'Gly'
}

def translate_dna(dna):
    dna = dna.upper()

    # Find start codon ATG
    start = dna.find('ATG')
    if start == -1:
        print("No start codon ATG found!")
        return

    print("=== Protein Translation Report ===")
    print(f"Full DNA Sequence : {dna}")
    print(f"Translation starts at position: {start + 1}")
    print(f"Reading from: {dna[start:]}")
    print()

    # Translate codon by codon
    protein = []
    codons_read = []

    for i in range(start, len(dna)-2, 3):
        codon = dna[i:i+3]
        amino_acid = codon_table.get(codon, '???')
        codons_read.append(f"{codon}={amino_acid}")

        if amino_acid == 'Stop':
            print("Stop codon reached — protein complete!")
            break
        protein.append(amino_acid)

    print(f"Codons read: {' | '.join(codons_read)}")
    print()
    print(f"Protein chain: {' - '.join(protein)}")
    print(f"Protein length: {len(protein)} amino acids")

# Test sequences
my_dna = "ATGTTCGTGTTCCTGTAA"
translate_dna(my_dna)
