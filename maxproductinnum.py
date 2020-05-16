#This function calculates the max product of adjacent n characters in the given number.
   
def maxproductinnum():
    num = int(input("Give me a number: "))
    chars = int(input("How many adjacent numbers should I calculate in that number?: "))
    strnum = str(num)
    product = 0
    maxproduct = 0
    
    def findproduct(strnum):
        product = 1
        for i in range (len(strnum)):
            product = int(strnum[i])*product
        return product

    for i in range (len(strnum)):
        product = findproduct(strnum[i:i+chars])
        if product > maxproduct:
            maxproduct = product
    
    return maxproduct
    

print("The answer is: ", maxproductinnum())



