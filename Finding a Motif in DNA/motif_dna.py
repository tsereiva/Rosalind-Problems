import regex as re
with open("rosalind_subs.txt", "r") as my_file:
    s,t = my_file.readlines()
    sequence = s.rstrip()
    motif = t.rstrip()
    Q=re.compile(motif)
    output = [item.start(0)+1 for item in Q.finditer(sequence, overlapped = True)]
#https://stackoverflow.com/questions/3590165/join-a-list-of-items-with-different-types-as-string-in-python
#Explains iterative .join function
    print(' '. join(str(x) for x in output))

#https://stackoverflow.com/questions/5616822/python-regex-find-all-overlapping-matches
#Helped find third-party regex module that supports overlapping matches
