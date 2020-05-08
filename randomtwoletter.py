#Generates two random letters

import random
def randomtwoletter():
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    firstletter = alphabet[random.randint(0,25)]
    secletter = alphabet[random.randint(0,25)]
    return (firstletter+secletter)

print(randomtwoletter())