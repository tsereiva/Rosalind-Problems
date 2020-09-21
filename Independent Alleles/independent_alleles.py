import math
from math import factorial as fac
from math import comb
def ind_allele(k,N):
    Pop = 2**k
    probability = 0
    for i in range(N, Pop+1):
        probability += comb(Pop, i) * (0.25**i) * (0.75**(Pop-i))
    return(round(probability, 3))

print(ind_allele(7,38))
