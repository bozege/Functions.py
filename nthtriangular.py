#this function returns the nth triangular number.1,3,6,10,15,21 etc.
def triangularnum():
    n = int(input("Which triangular number do you need?: "))
    tri = 0
    c = 0
    for i in range (0,n+1):
        tri += i
        c += 1

    return (tri,c-1)

result = triangularnum()
count = result[1]
num = result[0]
print("\nThe {}th triangular number is {}.".format(count,num))



