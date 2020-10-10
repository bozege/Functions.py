#collatz calculator 3n + 1 until it reaches 1.

def collatz():
    
    n = int(input("Enter a starting number: "))
    lst = list()
    lst.append(n)
    
    while n > 1:
        if n % 2 == 0:
            n = int(n / 2)
            lst.append(n)
        else:
            n = 3*n + 1
            lst.append(n)
    
    return(lst)

result = collatz()
print(result,"\n\nThere are {} elements in the list.".format(len(result)),"\n\nThe highest number in the list is {}.".format(max(result)))