def mortal_fibonacci(n,m):
    if n < 2:
        return(n)
    while n < m:
        return(mortal_fibonacci(n-1, m) + (mortal_fibonacci(n-2, m)))
    while n > m:
        return(mortal_fibonacci(n-1, m) + (mortal_fibonacci(n-2, m)) - mortal_fibonacci(n-(int(m)+1), m))
print(mortal_fibonacci(6,3))
