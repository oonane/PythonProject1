#Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. Ohjelma palauttaa toisen
#listan, joka on muuten samanlainen kuin parametrina saatu lista paitsi että siitä on
#karsittu pois kaikki parittomat luvut. Kirjoita testausta varten pääohjelma, jossa luot
#listan, kutsut funktiota ja tulostat sen jälkeen sekä alkuperäisen että karsitun listan.

def parittomat(numero):
    parilliset = []
    for luku in numero:
        if luku % 2 == 0:
            parilliset.append(luku)
    return parilliset

alkuperainen_lista = [3, 6, 7, 22, 12, 35, 34, 86, 98, 53]
poistettu = parittomat(alkuperainen_lista)

print(f"Alkuperäinen lista on: {alkuperainen_lista}")
print(f"Parillisten lista on: {poistettu}")


