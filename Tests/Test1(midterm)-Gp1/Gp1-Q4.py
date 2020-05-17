def factors(n):
    """
    Input: n is a positive integer.
    Output: a list of all factors of n
    """
    L = []
    for i in range(1,n//2+1):
        if n % i == 0:
            L.append(i)

    L.append(n)
    return L


print(factors(6))
print(factors(90))
print(factors(312))
print(factors(3120))

