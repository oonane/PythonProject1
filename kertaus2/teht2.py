
lista = []

while True:
    luku = int(input("Kerro luku: "))

    if luku == 0:
       break

    lista.append(luku)
    print("Nyt lista on: ", lista)
    print("Järjestetty lista on: ", sorted(lista))
