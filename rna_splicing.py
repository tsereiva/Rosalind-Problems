from Bio import SeqIO
from Bio.Seq import Seq
import regex as re
with open('rosalind_splc.txt') as my_file:
    dna_data = []
    for line in my_file:
        line = line.strip()
        if not line:
            continue
        if line.startswith(">"):
            continue
        else:
            dna_data.append(line)

full_dna = dna_data[0]
introns = dna_data[1:]

for i in range(len(introns)):
    full_dna = full_dna.replace(introns[i], '')

seq_exons = Seq(full_dna)
protein = seq_exons.translate(to_stop = True)
print(protein)
