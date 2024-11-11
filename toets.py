

inp = input("Geef een getal: ")

# inp = 23
# inp = str(inp)

product = 1
for c in inp:
    product *= int(c)

print("Het is", product)