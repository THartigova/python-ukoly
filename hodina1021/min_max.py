a = int(input(("Zadej A")))
b = int(input(("Zadej B")))
c = int(input(("Zadej C")))

min = a
max = b

if b < min:
    min = b
elif b > max:
    max = b

if c < min:
    min = c
elif c > max:
    max = c


print(f'Maximum:{max} minimum:{min}')