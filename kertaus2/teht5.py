def suurin_arvo(luku1, luku2, luku3):
    suurin = max(luku1, luku2, luku3)
    return suurin

luku1 = int(input("Anna luku: "))
luku2 = int(input("Anna luku: "))
luku3 = int(input("Anna luku: "))

tulos = suurin_arvo(luku1, luku2, luku3)

print(f"Suurin arvo on: {tulos}")
