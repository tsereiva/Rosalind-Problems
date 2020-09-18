from Bio import SeqIO
from Bio.Seq import Seq
dna_data = []
handle = open("rosalind_splc.fasta", "r")
for record in SeqIO.parse(handle, "fasta"):
    line = str(record.seq)
    dna_data.append(line)
full_dna = dna_data[0]
introns = dna_data[1:]

for i in range(len(introns)):
    full_dna = full_dna.replace(introns[i], '')

seq_exons = Seq(full_dna)
protein = seq_exons.translate(to_stop=True)
print(protein)
