#this function returns the factors of the given number.
def factorsofnum(n):
    factors = []
    for i in range (1,n+1):
        if n % i == 0:
            factors.append(i)
    
    return factors

