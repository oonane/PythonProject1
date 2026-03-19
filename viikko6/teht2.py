#Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen
#yhteismäärän. Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa.
#Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan
#maksimisilmäluku, joka kysytään käyttäjältä ohjelman suorituksen alussa.

import random

tahko = int(input("Anna tahkojen lukumäärä: "))
def heita ():
    return random.randint(1,tahko)

silmaluku = 0

while silmaluku != tahko:
    silmaluku = heita()
    print(f"tulos on {silmaluku}")