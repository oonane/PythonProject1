def summa(a, b):
    return a + b

def erotus(a, b):
    return a - b

def tulo(a, b):
    return a * b

def osamaara(a, b):
    return a / b

laskutoimitus = input("Kerro laskutoimitus: ")
a = float(input("Kerro luku: "))
b = float(input("Kerro luku: "))

while True:

    if laskutoimitus == "summa":
        print(summa(a, b))

    elif laskutoimitus == "erotus":
        print(erotus(a, b))

    elif laskutoimitus == "tulo":
        print(tulo(a, b))

    elif laskutoimitus == "osamaara":
        print(osamaara(a, b))

    else:
        break

    laskutoimitus = input("Kerro laskutoimitus: ")
    a = float(input("Kerro luku: "))
    b = float(input("Kerro luku: "))