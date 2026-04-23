import math

def create_point(x, y):
    return (x, y)

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

print("Anna pisteen koordinaatit.")
x1 = float(input("Pisteen x: "))
y1 = float(input("Pisteen y: "))
piste1 = create_point(x1, y1)

x2 = float(input("Pisteen x: "))
y2 = float(input("Pisteen y: "))
piste2 = create_point(x2, y2)

etaisyys = distance(piste1, piste2)

print(f"Etäisyys on {etaisyys:.2f}")



