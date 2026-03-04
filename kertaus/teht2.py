
viikonpaiva = input("Viikonpäivä: ")
tyotunti = int(input("Työtunnit: "))
palkka = int(input("Palkka: "))

if viikonpaiva != "sunnuntai":
    paivapalkka = palkka * tyotunti
    print(f"Päiväpalkka on {paivapalkka}")

else:
    sunnuntaipaivapalkka = (palkka * 2) * tyotunti
    print(f"Päiväpalkka on {sunnuntaipaivapalkka}")


