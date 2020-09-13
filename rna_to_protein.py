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
with open('rosalind_mrna.txt') as my_file:
    mrna = my_file.read().strip()
#Codon Table from https://github.com/mtarbit/Rosalind-Problems/blob/master/e008-prot.py
    count = 0
    for item in range(0, len(mrna), 3):
        try:
            if RNA_CODON_TABLE[mrna[item: item+3]] != 'Stop':
                count += 1
        except:
            continue

        else:
            break
print(count%1000000)
