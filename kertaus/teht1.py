
while True:
    nimi = input("Kerro nimesi: ")

    if nimi != "Matti":
        keittoannos = int(input("Montako keittoannosta: "))
        kokonaishinta = 5.90 * keittoannos
        print(f"Kokonaishinta on: {kokonaishinta}")
        print("Seuraava, kiitos!")


    else:
        print("Seuraava, kiitos!")
        break
