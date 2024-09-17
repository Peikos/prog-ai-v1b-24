def mijn_functie(temp):
    if temp < 10:
        return ("Brr!")
    # elif temp >= 10 and temp < 16:
    elif temp < 16:
        return ("Fris hier!")
    # elif temp >= 16 and temp < 21:
    elif temp < 21:
        return ("Dat is ok")
    # elif temp >= 21:
    else:
        return ("Poeh wat warm\Mag het raam open?")
    # print("Klaar!")

temp = int(input("Wat is de temperatuur?"))
commentaar = mijn_functie(temp)
print(commentaar.upper())