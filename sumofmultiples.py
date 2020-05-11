def sumofmultiples():
    a = 0
    b = 0
    n = 0
    sum = 0

    while a == 0:
        a = int(input("Enter the first parameter: "))
        
    while b == 0:
        b = int(input("Enter the second parameter: "))
        
    while n == 0:
        n = int(input("Enter a max point: "))

    for i in range (1,n):
        if i % a == 0 or i % b == 0:
            sum += i
        
    return(sum)

print(sumofmultiples())
        