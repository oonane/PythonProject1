#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän
# merkkijonon lopetusmerkiksi. Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta
# suuruusjärjestyksessä suurimmasta alkaen. Vihje: listan alkioiden lajittelujärjestyksen voi
# kääntää antamalla sort-metodille argumentiksi reverse=True.

luvut = []


while True:
    luku = input("Anna luku (tyhjä lopettaa): ")

    if luku == "":
        print("Virheellinen luku")
        break

    if luku != "":
        numero = int(luku)
        luvut.append(numero)

luvut.sort(reverse=True)

print("Viisi suurinta lukua: ")
for luku in luvut[:5]:
    print(luku)