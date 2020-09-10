def fibonacci(n,k):
    if n < 2:
        return(n)
    else:
        return(fibonacci(n-1, k) + (fibonacci(n-2, k)*k))
print(fibonacci(29,2))
