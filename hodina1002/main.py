x = -5

if x >= 0:
    if x > 0:
        print(f"{x} je kladné číslo")
    else:
        print(f"{x} je nula")
else:
    print(f"{x} je záporné číslo")
    x = -x
print(f"Absolutní hodnota: {x}")