sukupuoli = input("Kerro sukupuoli (mies tai nainen): ")
hemoglobiini = float(input("Kerro hemoglobiini: "))

if sukupuoli == "nainen" and 117 < hemoglobiini < 175:
    print("Hemoglobiini on normaali")

elif sukupuoli == "nainen" and hemoglobiini > 175:
    print("Hemoglobiini on korkea")

elif sukupuoli == "nainen" and hemoglobiini < 117:
    print("Hemoglobiini on matala")

if sukupuoli == "mies" and 134 < hemoglobiini < 195:
    print("Hemoglobiini on normaali")

elif sukupuoli == "mies" and hemoglobiini > 195:
    print("Hemoglobiini on korkea")

elif sukupuoli == "mies" and hemoglobiini < 134:
    print("Hemoglobiini on matala")