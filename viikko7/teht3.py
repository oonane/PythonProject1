#Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi. Ohjelma kysyy
#käyttäjältä, haluaako tämä syöttää uuden lentoaseman, hakea jo syötetyn lentoaseman tiedot
#vai lopettaa. Jos käyttäjä valitsee uuden lentoaseman syöttämisen, ohjelma kysyy käyttäjältä
#lentoaseman ICAO-koodin ja nimen. Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin
#ja tulostaa sitä vastaavan lentoaseman nimen. Jos käyttäjä haluaa lopettaa, ohjelman suoritus
#päättyy. Käyttäjä saa valita uuden toiminnon miten monta kertaa tahansa aina siihen asti,
#kunnes hän haluaa lopettaa. (ICAO-koodi on lentoaseman yksilöivä tunniste. Esimerkiksi
#Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK. Löydät koodeja helposti selaimen avulla.)

lentoasemat = {"EFHK" : "Helsinki-Vantaan lentoasema",
               "EGLL" : "Heathrow’n lentoasema",
               "LFPG" : "Charles de Gaullen kansainvälinen lentoasema"}

while True:
    print("\nValitse toiminto: ")
    print("1 - Syötä uusi lentoasema.")
    print("2 - Hae lentoaseman tiedot.")
    print("0 - Lopeta.")

    valinta = input("Valinta: ")

    if valinta == "1":
        ICAO = input("Anna ICAO-koodi: ")
        nimi = input("Anna lentoaseman nimi: ")
        lentoasemat[ICAO] = nimi
        print(f"Lisätty: {ICAO} - {nimi}")

    elif valinta == "2":
        ICAO = input("Anna ICAO-koodi: ").upper()
        if ICAO in lentoasemat:
            print(f"Lentoaseman nimi: {lentoasemat[ICAO]}")

        else:
            print("Lentoasemaa ei löydy.")

    elif valinta == "0":
        print("Ohjelma päättyy.")
        break

    else:
        print("Virheellinen valinta.")
        break

