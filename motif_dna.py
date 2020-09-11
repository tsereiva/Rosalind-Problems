import re
with open("rosalind_subs.txt", "r") as my_file:
    s,t = my_file.readlines()
    sequence = s.rstrip()
    motif = t.rstrip()
    Q=re.compile(motif)
    output = [item.start(0) for item in Q.finditer(sequence)]
    print(output)
