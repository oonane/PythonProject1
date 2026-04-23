arvot = {"John" : ["John", 30, "Engineer"],
         "Emily" : ["Emily", 25, "Artist"],
         "Anna" : ["Anna", 22, "Student"]}


print(f"Nimi on: {arvot['John'][0]} ja ikä on {arvot['John'][1]}")
print(f"Emilyn ammatti on: {arvot['Emily'][2]}")

arvot["Anna"][2] = "Teacher"

arvot["James"] = ["James", 28, "Writer"]

arvot["Sophia"] = ["Sophia", 35, "Doctor"]

del arvot["Emily"]

print(arvot)