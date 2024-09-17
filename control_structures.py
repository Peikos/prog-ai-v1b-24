# s = str()
# woord = 'hogeschool utrecht'
#
# for i in range(11, len(woord)):
#     s = s + woord[i]
#
# print("i =", i)
#
# print(s)
#
#
# for x in range(6):
#     print("hallo")

# temp = int(input("Wat is de temperatuur?"))

# MAAK HIER DE FUNCTIE mijn_functie VAK
if temp < 10:
    print("Brr!")
# elif temp >= 10 and temp < 16:
elif temp < 16:
    print("Fris hier!")
# elif temp >= 16 and temp < 21:
elif temp < 21:
    print("Dat is ok")
# elif temp >= 21:
else:
    print("Poeh wat warm")
    print("Mag het raam open?")
print("Klaar!")

# if temp in range(16,21):
#     print("Nogmaals: dat is ok.")



temp = int(input("Wat is de temperatuur?"))
commentaar = mijn_functie(temp)
print(commentaar.upper())














leeftijd = 37

# Leeftijd < 18       -> jong
# 18 <= leeftijd < 24 -> prima leeftijd
# <= 24               -> F*cking oud