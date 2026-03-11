import random

arpa = int(input("Anna arpakuutioiden lukumäärä: "))

summa = 0



for heitot in range(arpa):
    heitot = random.randint(1, 6)
    summa += heitot
    print(f"Arvo on {heitot}")


print(f"Summa on {summa}")
