import math

luku = int(input("Kerro kokonaisluku: "))

while luku >= 0:
    from math import sqrt
    print(sqrt(luku))
    luku = int(input("Kerro kokonaisluku: "))


if luku < 0:
    print("Virheellinen numero.")
    luku = int(input("Kerro kokonaisluku: "))


