RNA_CODON_TABLE ={
'UUU': 'F',     'CUU': 'L',     'AUU': 'I',     'GUU': 'V',
'UUC': 'F',     'CUC': 'L',     'AUC': 'I',     'GUC': 'V',
'UUA': 'L',     'CUA': 'L',     'AUA': 'I',     'GUA': 'V',
'UUG': 'L',     'CUG': 'L',     'AUG': 'M',     'GUG': 'V',
'UCU': 'S',     'CCU': 'P',     'ACU': 'T',     'GCU': 'A',
'UCC': 'S',     'CCC': 'P',     'ACC': 'T',     'GCC': 'A',
'UCA': 'S',     'CCA': 'P',     'ACA': 'T',     'GCA': 'A',
'UCG': 'S',     'CCG': 'P',     'ACG': 'T',     'GCG': 'A',
'UAU': 'Y',     'CAU': 'H',     'AAU': 'N',     'GAU': 'D',
'UAC': 'Y',     'CAC': 'H',     'AAC': 'N',     'GAC': 'D',
'UAA': 'Stop',  'CAA': 'Q',     'AAA': 'K',     'GAA': 'E',
'UAG': 'Stop',  'CAG': 'Q',     'AAG': 'K',     'GAG': 'E',
'UGU': 'C',     'CGU': 'R',     'AGU': 'S',     'GGU': 'G',
'UGC': 'C',     'CGC': 'R',     'AGC': 'S',     'GGC': 'G',
'UGA': 'Stop',  'CGA': 'R',     'AGA': 'R',     'GGA': 'G',
'UGG': 'W',     'CGG': 'R',     'AGG': 'R',     'GGG': 'G'
}
frequency = {}
for key, value in RNA_CODON_TABLE.items():
    if value not in frequency:
        frequency[value] = 1
    else:
        frequency[value] += 1
with open('rosalind_mrna.txt') as my_file:
    mrna = my_file.read().strip()
    count = frequency['Stop']
    #https://stackoverflow.com/questions/9475241/split-string-every-nth-character
    #could make protein list more easily, but the current code has an easily adjustable interval
    n = 1
    protein =[mrna[i:i+n] for i in range(0, len(mrna), n)]
    for p in protein:
        count *= frequency[p]
print(count%1000000)

#Helped with understading the theory behind calculation:
#http://saradoesbioinformatics.blogspot.com/2016/07/inferring-mrna-from-protein.html
