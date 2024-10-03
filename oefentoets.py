# Oefentoets

# Opdracht 1

tekst = input("Voer een string in: ")

omgekeerd = ""

for c in tekst:
    omgekeerd = c + omgekeerd

print("Deze string omgekeerd:", omgekeerd)



# Opdracht 2

a = int(input("Getal 1: "))
b = int(input("Getal 2: "))
c = int(input("Getal 3: "))

mid = sorted([a, b, c])[1]

print("Het middelste getal is:", mid)


# Opdracht 3

x1 = float(input("X positie van coordinaat 1 (X1): "))
y1 = float(input("Y positie van coordinaat 1 (Y1): "))
x2 = float(input("X positie van coordinaat 2 (X2): "))
y2 = float(input("Y positie van coordinaat 2 (Y2): "))

afstand = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print(f"Afstand tussen coordinaten ({x1},{y1}) en ({x2},{y2}): {afstand:.4f}")


# Opdracht 4

total = 1
answer = ""
while answer != "stop":
    if answer != "":
        total *= int(answer)
    answer = input("Voer een getal in: ")
print("Als je deze getallen vermenigvuldigt, is het resultaat:", total)


# Opdracht 5

def isPositiefEnKleinerDan(x, y):
    return y > x > 0