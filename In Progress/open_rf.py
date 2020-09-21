from Bio.Seq import Seq

with open('test.txt') as my_file:
    sequence_name = ""
    dnaseq = ""
    for line in my_file:
        line = line.strip()
        if not line:
            continue
        if line.startswith(">"):
            sequence_name = line[1:]
        else:
            dnaseq = "".join((dnaseq, line))
    dseq = Seq(dnaseq)
    revseq = dseq.reverse_complement()
    trans_dna = str(dseq.translate())
    print(trans_dna)
    exit()
    trans_rna = str(revseq.translate())
    total_trans = "*".join((trans_dna,trans_rna))
    orfs = total_trans.split("*")
    for item in orfs:
        print(item)
