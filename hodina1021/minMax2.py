a = int(input("Zadej A: "))
b = int(input("Zadej B: "))
c = int(input("Zadej C: "))

min = a
max = a

if a > b:
    temp = a
    a = b
    b = temp
if b > c:
    temp = b
    b = c
    c = temp
if a > b:
    temp = a
    a = b
    b = temp

print(f'{a} < {b} < {c}')