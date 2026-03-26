lista = ["sauna", "hattu", "olo", "hevonen", "kuusi", "viidakko", "henkilö", "kurkku"]

yli = 0

for i in lista:
    if len(i) > 5:
        yli += 1

print("Yli viisikirjaimisia sanoja on yhteensä: ", yli)