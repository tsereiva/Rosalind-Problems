from Bio.Seq import Seq
with open("rosalind_prot.txt", "r") as my_file:
    for line in my_file:
        m_rna = Seq(line)
        print(m_rna.translate())
