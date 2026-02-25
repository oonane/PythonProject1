raha = float(input("Kuinka paljon sinulla on rahaa?"))

if raha >= 5:
    print("Voit ostaa kahvin")

else:
    puuttuva = 5-raha
    print("Et voi ostaa kahvia, sinulta puuttuu", puuttuva)

print("Kiitos hei!")


a = True
b = False

if a and b:
    print("Molemmat ovat totta.")

if a or b:
    print("Toinen ehto oli totta.")

if not a and b:
    print("Kumpikaan ei ole totta.")


numero = int(input("Anna kokonaisluku: "))

if numero > 0:
    print("Luku on positiivinen.")

elif numero < 0:
    print("Luku on negatiivinen.")

else:
    print("Luku on 0.")
