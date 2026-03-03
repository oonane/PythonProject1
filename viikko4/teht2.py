import math

tuuma = float(input("Kerro tuumien määrä (negatiivinen luku lopettaa):"))


while tuuma >= 0:
    senttimetri = tuuma * 2.54
    print(f"Tuuma {tuuma} on {senttimetri} senttimetriä.")

    tuuma = float(input("Kerro tuumien määrä (negatiivinen luku lopettaa):"))

print("Ohjelma loppuu")