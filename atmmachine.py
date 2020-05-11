banknotes = [200,100,50,20,10,5,1,0.50,0.25,0.10,0.05,0.01]

amount = float(input("Enter an amount: "))

for i in range (0,len(banknotes)):
    if banknotes[i] <= amount:
        banknote = int(amount // banknotes[i])
        amount = amount - banknote*(banknotes[i])
        print(banknotes[i],"banknotes:",banknote)
        
    