
luku = input("Anna luku, tyhjä lopettaa")

pienin = luku
suurin = luku

while luku != " ":
    numero = int(luku)

    if suurin == luku or numero > suurin:
            suurin = numero

    if pienin == luku or numero < pienin:
            pienin = numero

    luku = input("Anna luku, tyhjä lopettaa")

print(f"Suurin luku on: {suurin} ja pienin luku on {pienin}")

