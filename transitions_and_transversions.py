from Bio import SeqIO

data = []
handle = open('rosalind_tran.fasta', 'r')
for record in SeqIO.parse(handle, 'fasta'):
    data.append(str(record.seq))
handle.close()
seq1 = data[0]
seq2 = data[1]
transitions = 0
transversions = 0
for a, b in zip(seq1, seq2):
    # https://careerkarma.com/blog/python-zip/
    if a != b:
        if a in ["A", "G"] and b in ["A", "G"] or  a in ["C", "T"] and b in ["C", "T"]:
            transitions += 1
        else:
            transversions += 1
print(transitions/transversions)
