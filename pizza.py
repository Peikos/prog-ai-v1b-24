import math

# Vraag "Wat is de doorsnede van uw pizza?"
doorsnede = float(input("Wat is de doorsnede van uw pizza?"))

# Berekening (onzichtbaar voor gebruiker)
oppervlakte = (doorsnede/2) ** 2 * math.pi

# Antwoord "De oppervlakte van uw pizza is ..."
print("De oppervlakte van uw pizza is ...", oppervlakte)