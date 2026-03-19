#Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä
#sekä pizzan hinnan euroina. Funktio laskee ja palauttaa pizzan yksikköhinnan euroina
#per neliömetri. Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat sekä
#ilmoittaa, kumpi pizza antaa paremman vastineen rahalle (eli kummalla on alhaisempi
#yksikköhinta). Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.

import math

def yksikkohinta(halkaisija, hinta):
    sade = (halkaisija/2)/100
    pinta_ala = math.pi * (sade**2)
    return hinta / pinta_ala

d1 = float(input("Anna ensimmäisen pizzan halkaisija (cm): "))
e1 = float(input("Anna ensimmäisen pizzan hinta (€): "))

d2 = float(input("Anna toisen pizzan halkaisija (cm): "))
e2 = float(input("Anna toisen pizzan hinta (€): "))

hinta1 = yksikkohinta(d1, e1)
hinta2 = yksikkohinta(d2, e2)

print(f"Ensimmäisen pizzan hinta {hinta1:.2f} €/m^2")
print(f"Toisen pizzan hinta {hinta2:.2f} €/m^2")

if hinta1 > hinta2:
    print("Toinen pizza on halvempi")

elif hinta1 < hinta2:
    print("Ensimmäinen pizza on halvempi")

else:
    print("Pizzat ovat samanarvoiset")

