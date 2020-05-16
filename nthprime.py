#This function returns the nth prime number
def nthprime():
    n = int(input("Which prime number do you need?: "))
    primes = [2,3,5,7]
    i = 8
    while len(primes) < n:
        sqrt = int((i**(1/2))//1)
        for j in range (2,sqrt+1):
            if i % j == 0:
                break
        if i % j != 0:
            primes.append(i)
        i += 1
    return primes[n-1]

print("Your number is: ", nthprime())
