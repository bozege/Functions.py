#This function finds the smallest number that can be divided by each of the numbers from a to b.
def minimumdivisible_fromatob():
    a = 0
    b = 0
    while a == 0:
        a = int(input("Enter the first parameter: "))
    while b == 0:
        b = int(input("Enter the second parameter: "))
    if b < a:
        c = a
        a = b
        b = c
    print("Please wait...")
    n = 1
    i = a
    list =[]
    while len(list) == 0:
        
        while n % i == 0:
            
            i += 1
            
            if i == b+1:
                list.append(n)
                break
            
            
        n += 1
        i = a

    return (list[0])

result = minimumdivisible_fromatob()
print ("Your number is: ", result)
       
    
