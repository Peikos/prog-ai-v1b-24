# file = open("testfile", "w")
# file.write("foo")
# file.close()                      <-- die miste in de Wooclap
# file = open("testfile", "a")
# file.write("bar")
# file.close()                      <-- die miste in de Wooclap
# exit()


def nieuwe_box(naam): # Maak / overschrijf bestand met naam "<naam>.txt" en zet hier 0.0 in # HINT: f-strings
    file = open(f"{naam}.txt", "w")
    file.write("0.0")
    file.close()


def leeg_box(naam): # Open het bestand "<naam>.txt", print hoeveel geld erin zit, reset naar 0 # Bonus: print EUR 13,30 (met 2 decimalen)
    # Open het bestand om te lezen
    file = open(f"{naam}.txt", "r")

    # Lees de waarde en maak er een float van
    waarde = float(file.read())

    # Sluit het bestand
    file.close()

    # Print het resultaat
    print(f"EUR {waarde:.2f}")

    # Open het bestand om te schrijven
    # Schrijf 0.0
    # Sluit het bestand
    nieuwe_box(naam) # Hier was al een functie voor


def euro(naam): # Hoog het bedrag in de box met 1 euro op
    file = open(f"{naam}.txt", "r")
    bedrag = float(file.read())
    file.close()
    bedrag += 1

    # Netter: na een with block wordt de file automatisch gesloten
    with open(f"{naam}.txt", "w") as file:
        file.write(str(bedrag))


def tientje(naam): # Hoog het bedrag op met 10 euro   - KUN JE EEN ALGEMENERE FUNCTIE VERZINNEN DAN EURO EN TIENTJE?
    pass


def meer_dan(naam, bedrag): # Return true als er tenminste <bedrag> euro in de box zit, anders false
    pass


# Test
nieuwe_box("spaarpot")
euro("spaarpot")
leeg_box("spaarpot")