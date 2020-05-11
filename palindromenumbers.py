#Lists all of the palindrome numbers below 1000000. 

def find_palindrome():
    palindromelist = []
    for i in range (999,100,-1):
        for j in range (999,100,-1):
            if str(i*j) == str(i*j)[::-1]:
                palindromelist.append((i*j))
    return max (palindromelist)  #delete max if you want to list all the palindromes.

print(find_palindrome())