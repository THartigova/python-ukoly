
print("POZDRAV PODLE HODINY") 

time = int(input("Zadejte čas "))
if time < 0:
    print("Zadávejte hodiny v rozmezí 0 až 23.")
elif time > 23:
    print("Zadávejte hodiny v rozmezí 0 až 23.")


elif 5 <= time < 9:
    print("Dobré ráno")
elif 9 <= time < 12:
    print("Dobré dopoledne")
elif time == 12:
    print("Dobré poledne")
elif 12 < time < 16:
    print("Dobré odpoledne")
elif 16 <= time < 22:
    print("Dobrý večer")
else:
    print("Dobrou noc")