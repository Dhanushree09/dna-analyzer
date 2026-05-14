# DNA Analyzer - My First Bioinformatics Project
# Made by: Dhanushree
# Class 12 Student - Jammu & Kashmir

def analyze_dna(dna):
    dna = dna.upper()
    
    a = dna.count("A")
    t = dna.count("T")
    g = dna.count("G")
    c = dna.count("C")
    total = len(dna)
    
    gc_content = (g + c) / total * 100
    at_content = (a + t) / total * 100
    
    print("=== DNA Analysis Report ===")
    print(f"DNA Sequence : {dna}")
    print(f"Total Length : {total} bases")
    print(f"Adenine  (A) : {a}")
    print(f"Thymine  (T) : {t}")
    print(f"Guanine  (G) : {g}")
    print(f"Cytosine (C) : {c}")
    print(f"GC Content   : {gc_content:.2f}%")
    print(f"AT Content   : {at_content:.2f}%")

# DNA sequences analyzed
my_dna = "ATGCGATACGCTTACGATGCATCG"
analyze_dna(my_dna)

my_dna2 = "AAAAAATTTTTTGGGGGGCCCCCC"
analyze_dna(my_dna2)

my_dna3 = "ATGATGATGATGATGATGATGATG"
analyze_dna(my_dna3)
