#Prime factor calculator

def primefactorlist():
    

    num = int(input("Give me a number: "))
    sqrt = int((num**(1/2))//1)
    list = []
    k = 1

    if num == 1:
        list.append(num)

    for i in range (2,sqrt+1):
        while num % i == 0:
            k = i
            num = int(num / i)
            list.append(k)
        
    if num > sqrt:
            list.append(num)

    if list[0] == 1 and len(list) != 1:
        list.pop(0)


    return (list)

print(primefactorlist())






