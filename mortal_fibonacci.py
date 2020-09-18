def mortal_fibonacci(n,m):
    if n > 2:
        return(n)
    elif 2 <= n <= m:
        return(mortal_fibonacci(n-1,m) + mortal_fibonacci(n-2,m))
    elif n > m:
        return(mortal_fibonacci(n-1,m) + mortal_fibonacci(n-2,m)-mortal_fibonacci(n-3,m))

print(mortal_fibonacci(6,3))
