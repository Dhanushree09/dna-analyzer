# Project 4 - NCBI Gene Fetcher
# Made by: Dhanushree Dabgotra
# Class 12 Student - Jammu & Kashmir
# Real world use: Fetches real genome data
# from NCBI database used by researchers worldwide

from Bio import Entrez, SeqIO

Entrez.email = "dabgotradhanushree@gmail.com"

def fetch_gene(gene_id):
    print(f"=== Fetching Gene: {gene_id} from NCBI ===")
    print("Connecting to NCBI database...")
    
    handle = Entrez.efetch(
        db="nucleotide",
        id=gene_id,
        rettype="gb",
        retmode="text"
    )
    
    record = SeqIO.read(handle, "genbank")
    handle.close()
    
    print(f"Gene Name      : {record.name}")
    print(f"Description    : {record.description}")
    print(f"Sequence Length: {len(record.seq)} bases")
    print(f"First 50 bases : {record.seq[:50]}")
    print(f"Organism       : {record.annotations.get('organism', 'Unknown')}")
    print(f"Source         : {record.annotations.get('source', 'Unknown')}")

# Fetch original SARS-CoV-2 Wuhan genome
# MN908947 = first COVID genome ever sequenced
# January 2020 - Wuhan, China
fetch_gene("MN908947")
