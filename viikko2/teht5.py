import math

leiviskat = int(input("Anna leiviskät:"))

naulat = int(input("Anna naulat:"))

luodit = float(input("Anna luodit:"))

kokonaisluodit = ( leiviskat * 20 *32 ) + (naulat * 32) + luodit

grammat = kokonaisluodit * 13.3

kilot = int(grammat // 1000)

grammat = grammat % 1000

print(f"Massa on {kilot} kiloa ja {grammat} grammaa")