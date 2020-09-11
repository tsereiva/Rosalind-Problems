#Code take from: http://saradoesbioinformatics.blogspot.com/2016/06/counting-point-mutations.html
seq = [line.strip('\n') for line in open('rosalind_hamm.txt')]
hamming = 0
for line1, line2 in zip(seq[0],seq[1]):
    if line1 != line2:
        hamming += 1
print(hamming)
