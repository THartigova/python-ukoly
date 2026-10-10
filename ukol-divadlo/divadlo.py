print("ÚKOL NA CENU DO DIVADLA")

basePrice = 500
 
age = float(input("Věk návštěvníka: "))
studentAnswer = input("Je student (ano/ne): ").strip().lower()
peopleCount = int(input("Počet osob: "))
 
if peopleCount >= 4:
    discountName = "Skupinová sleva 25 %"
    priceMultiplier = 0.75
elif studentAnswer == "ano" and age < 26:
    discountName = "Studentská sleva 30 %"
    priceMultiplier = 0.7
elif age >= 65:
    discountName = "Seniorská sleva 20 %"
    priceMultiplier = 0.8
else:
    discountName = "Bez slevy"
    priceMultiplier = 1
 
ticketPrice = basePrice * priceMultiplier
totalPrice = ticketPrice * peopleCount
 
print(f"Typ slevy: {discountName}")
print(f"Cena za jednu vstupenku: {ticketPrice:.2f} Kč")
print(f"Celková cena: {totalPrice:.2f} Kč")