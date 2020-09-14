from Bio.SeqUtils.ProtParam import ProteinAnalysis
#https://biopython.org/wiki/ProtParam
with open('rosalind_prtm.txt') as my_file:
    protein = my_file.read().strip()
    analysed_seq = ProteinAnalysis(protein)
    print(analysed_seq.molecular_weight())
