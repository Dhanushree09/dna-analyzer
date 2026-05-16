# Project 2 - Reverse Complement Finder
# Made by: Dhanushree
# Class 12 Student - Jammu & Kashmir
# Real world use: PCR primer design, 
# gene cloning, COVID genome research

def reverse_complement(dna):
    dna = dna.upper()
    
    complement = {
        'A': 'T',
        'T': 'A',
        'G': 'C',
        'C': 'G'
    }
    
    comp_strand = ''
    for base in dna:
        comp_strand += complement[base]
    
    rev_comp = comp_strand[::-1]
    
    print("=== Reverse Complement Report ===")
    print(f"Original DNA  : {dna}")
    print(f"Complement    : {comp_strand}")
    print(f"Rev Complement: {rev_comp}")
    print(f"Length        : {len(dna)} bases")

# Test sequences
my_dna = "ATGCGATACGCTTACG"
reverse_complement(my_dna)

# ATG repeat sequence
my_dna2 = "ATGATGATG"
reverse_complement(my_dna2)

# COVID spike protein start sequence
my_dna3 = "ATGTTCGTGTTCCTG"
reverse_complement(my_dna3)
