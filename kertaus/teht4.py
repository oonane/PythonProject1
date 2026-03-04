tarina = ""

sana = ""

while True:

    if sana != "loppu":
        sana = input("Anna sana lisättäväksi tarinaan: ")


    if sana == "loppu":

        break

    tarina = tarina + " " + sana

print(tarina)