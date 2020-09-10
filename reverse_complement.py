from Bio.Seq import Seq
with open("rosalind_revc.txt", "r") as my_file:
    str = ''.join(my_file)
    seq = Seq(str)
    print(seq.reverse_complement())
