#has to be fixed, returns the halves as a list
n = int(input("Enter a number: "))
strn = str(n)
half1 = []
half2 = []
if len(strn) % 2 == 0:
    for i in range (0,len(strn)):
        while len(half1) != len(strn)/2:
            half1.append(strn[i])
            break
        if len(half1) == len(strn)/2:
            half2.append(strn[i])

print("First half is: ", half1,"\nSecond half is: ", half2)