from math import comb
def expoff (a,b,c,d,e,f):
    totoffspring = (a+b+c+d+e+f)*2
    pdd = float(a*1*2)
    pdh = float(b*1*2)
    pdr = float(c*1*2)
    phh = float(d*0.75*2)
    phr = float(e*0.5*2)
    prr = float(f*0*2)
    domoff = pdd+pdh+pdr+phh+phr+prr
    return(domoff)
print(expoff(16927, 18498, 19017, 17967, 19971, 18385))
