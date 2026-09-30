# 
print("KALKULAČKA SPROPITNÉHO")    #tisk nadpisu
amount = float(input("Zadej celkovou cenu: "))
procentage = int(input("Zadejte spropitné v %: "))
people = int(input("Počet lidí: "))

amount = float(amount + (amount / 100 * procentage))
print(amount)
amountForOne = round((amount/people)+0.5)
print(amountForOne)