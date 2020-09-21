from Bio import SeqIO
data = SeqIO.read("rosalind_revp.fasta", "fasta")
fwd_seq = str(data.seq)
rev_seq = str(data.seq.complement())
for a in range(len(fwd_seq)):
    for b in range(0, len(rev_seq)):
        fwd_subset = fwd_seq[a:b + 1]
        rev_subset = rev_seq[a:b + 1]
        if 4 <= len(fwd_subset)<= 12:
            # [::-1] reverses a list
            if fwd_subset == rev_subset[::-1]:
                     print(a + 1, len(fwd_subset))
#a+1 because positon is "the total number of symbols to the left of the target symbol, including itself"
