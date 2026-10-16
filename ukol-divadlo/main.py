x1 = 2
y1 = 1.5
x2 = 6
y2 = 7

xb = float(input("Zadej x souřadnici panáčka: "))
yb = float(input("Zadej y souřadnici panáčka: "))

if xb>x1 and xb<x2 and yb>y1 and yb<y2:
    print("Jsi v zone")
elif xb >= x1 and xb <= x2 and yb >=y1 and yb <= y2:
    print("Jsi na kraji strany")
else:
    print("Nejsi v zone")
