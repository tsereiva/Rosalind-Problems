with open("rosalind_hamm.txt", "r") as my_file:
    mutations = 0
    seqdict = {}
    for line in my_file:
    #https://stackoverflow.com/questions/6181935/how-do-you-create-different-variable-names-while-in-a-loop
        for x in range(1, 3):
            seqdict["sequence{0}".format(x)] = line
        print(seqdict)
        for a,b in (seqdict['sequence1'], seqdict['sequence2']):
            if a != b:
                mutations = mutations + 1
            else:
                continue
print(mutations)
