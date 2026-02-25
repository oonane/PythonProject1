summa = 0

while True:
    numero = int(input("Anna luku, jonka haluat lisätä, -1 lopettaa: "))
    if numero == -1:
        break
    elif numero <= 10:
        continue
    summa += numero

print("Summa on: ", summa)

