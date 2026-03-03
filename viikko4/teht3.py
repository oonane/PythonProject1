
pienin = None
suurin = None


while True:
    luku = input("Anna luku:")

    if luku == '':
        break

    luku = float(luku)

    if pienin is None or luku < pienin:
        pienin = luku

    if suurin is None or luku > suurin:
        suurin = luku

if pienin is not None:
    print(f"Suurin luku on {suurin} ja pienin luku on {pienin}")
