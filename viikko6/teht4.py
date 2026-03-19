#Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. Ohjelma palauttaa
#listassa olevien lukujen summan. Kirjoita testausta varten pääohjelma, jossa luot listan,
#kutsut funktiota ja tulostat sen palauttaman summan.

def summa_num(numerot):
    summa = 0
    for n in numerot:
        summa += n
    return summa

numerot = [5, 3, 98, 56, 27, 45, 7]
tulos = summa_num(numerot)

print(tulos)


