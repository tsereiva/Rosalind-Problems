from Bio.SeqUtils import GC
with open("rosalind_gc.txt", "r") as my_file:
    #Fasta file into dictionary
    fasta_dictionary = {}
    sequence_name = ""
    for line in my_file:
        line = line.strip()
        if not line:
            continue
        if line.startswith(">"):
            sequence_name = line[1:]
            if sequence_name not in fasta_dictionary:
                fasta_dictionary[sequence_name] = []
            continue
        sequence = line
        fasta_dictionary[sequence_name].append(sequence)

#Totally independent code. Sequences lines are joined so that Biopython can be used
for sequence_name in fasta_dictionary:
    analysis = ''.join(fasta_dictionary[sequence_name])
    fasta_dictionary[sequence_name] = analysis
for sequence_name in fasta_dictionary:
    seq = fasta_dictionary[sequence_name]
    count = GC(seq)
    fasta_dictionary[sequence_name] = count

#https://stackoverflow.com/questions/52141785/sort-dict-by-values-in-python-3-6
#reverse added to sort dictionary from greatest to least
output = {k: v for k, v in sorted(fasta_dictionary.items(), key=lambda x: x[1], reverse = True)}
#https://stackoverflow.com/questions/44656381/printing-multiple-variables-in-a-separate-lines-using-a-single-print
print(list(output)[0], output[list(output)[0]], sep='\n')
