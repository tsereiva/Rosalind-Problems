from itertools import permutations
import math
from math import factorial as fact
def enumerate_genes(n):
    values = []
    for num in range(1,n+1):
        values.append(num)
    perm = permutations(values)
    print(fact(n))
    for sequence in perm:
        print(*sequence)
    # * removes tuple formatting
print(enumerate_genes(7))