yritykset = 0

while yritykset < 5:
    kayttajatunnus = input("Kerro käyttäjätunnus: ")
    salasana = input("Kerro salasana: ")

    if kayttajatunnus == "python" and salasana == "rules":
        print("Tervetuloa")
        break

    else:
        yritykset += 1

    if yritykset == 5:
        print("Pääsy evätty")
