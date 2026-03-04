

laskutoimitus = input("Kerro laskutoimitus: ")
luku1 = float(input("Kerro luku: "))
luku2 = float(input("Kerro luku: "))

while True:

    if laskutoimitus == "yhteenlasku":
        print(luku1+luku2)

    elif laskutoimitus == "miinuslasku":
        print(luku1-luku2)

    elif laskutoimitus == "kertolasku":
        print(luku1*luku2)

    elif laskutoimitus == "jakolasku":
        print(luku1/luku2)

    else:
        break

    laskutoimitus = input("Kerro laskutoimitus: ")
    luku1 = float(input("Kerro luku: "))
    luku2 = float(input("Kerro luku: "))

