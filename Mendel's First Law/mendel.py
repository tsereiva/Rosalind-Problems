from math import comb
def mendel(k, m, n):
    totcomb = comb(k+m+n,2)
    pkk = float(comb(k, 2)*1)
    pkm = float(k*m*1)
    pkn = float(k*n*1)
    pmn = float(m*n*0.5)
    pmm = float(comb(m,2)*0.75)
    totaldominant = pkk+pkm+pkn+pmn+pmm
    return(totaldominant/totcomb)
print(mendel(20,27,16))
