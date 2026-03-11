ostoslista = ["maito", "porkkana", "kala"]

print("Ostoslista:", ostoslista)

while ostoslista:
    ostos = input("Ostettava asia: ").lower()

    if ostos in ostoslista:
        ostoslista.remove(ostos)
        print("Jäljellä", ostoslista)

    else:
        print("Ei listalla.")

print("Ostokset suoritettu")

