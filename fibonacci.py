#Returns all of the fibonacci numbers as a list below the given limit.
def fibonacci():
    n = int(input("Enter a limit number: "))
        
    fib1 = 1
    fib2 = 2
    fib3 = fib1 + fib2
    fiblist = [1,2]
    while fib3 < n:
        fiblist.extend([fib3])
        fib1 = fib2
        fib2 = fib3
        fib3 = fib1 + fib2
    
    return(fiblist)

