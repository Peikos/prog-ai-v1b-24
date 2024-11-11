import tkinter as tk
import FreeSimpleGUI as sg

def caesar(text):
    """Codeer tekst met ROT13 Caesar Cipher. Werking niet relevant maar wordt gebruikt in GUI voorbeelden."""
    def shift(letter):
        c = ord(letter)
        if 65 <= c <= 90:
            offset = 65
        elif 97 <= c <= 122:
            offset = 97
        else:
            return letter
        return chr((c-offset + 13) % 26 + offset)

    return ''.join([shift(letter) for letter in text])


def tkinter_gui():
    window = tk.Tk()                                             # Maak een scherm
    instructions = tk.Label(text="Enter message below")          # Maak een label

    entry = tk.Entry()                                           # en een tekstvak

    def cipher_code():                                           # Functie binnen een functie - deze functie kan
        text = entry.get()                                       # bij entry om deze te lezen/schrijven.
        text = caesar(text)
        entry.delete(0, tk.END)                             # Leeg het tekstvak
        entry.insert(0, text)                              # Schrijf het resultaat van de codering in het tekstvak

    button = tk.Button(
        text="Casesar me!",
        width=25,
        height=5,
        command=cipher_code                                      # Koppel de functie aan de knop
    )

    instructions.pack()                                          # Voeg alle elementen toe aan het frame, op deze volgorde
    entry.pack()
    button.pack()

    window.mainloop()                                            # Start de GUI


# Alternatief: PySimpleGui
def fsg_gui():
    sg.theme('BluePurple')

    layout = [[sg.Text('Enter message below'), sg.Text(size=(15, 1))],     # Geef de hele UI als een lijst, vergelijkbaar met HTML
              [sg.Input(key='MSG')],                                       # Tekstvak; MSG wordt gebruikt om de waarde te lezen / schrijven
              [sg.Button('Caesar me!')]]                                   # Knop; drukken geeft een event met de tekst "Caesar me!"

    window = sg.Window('PySimpleGUI', layout)                          # Maak een scherm met de gegeven layout

    event = 0                                                              # Initieel event, deze wordt in de loop geupdate. Gebruik geen None want dat is WIN_CLOSED

    while event != sg.WIN_CLOSED:                                          # Event loop, herhaal tot het scherm gesloten wordt
        event, values = window.read()                                      # Wacht op een event, lees het event en de waardes
        if event == 'Caesar me!':                                          # Als het event van de knop kwam
            text = values['MSG']                                           # Lees de waare van het tekstvak
            text = caesar(text)
            window['MSG'].update(text)                                     # Schrijf de waarde van het tekstvak


# Demo functionaliteit
if __name__ == "__main__":
    demos = {"1": fsg_gui, "2": tkinter_gui}

    print("1 FreeSimpleGUI")
    print("2 TKInter")

    keuze = input("Run een demo (1-2) ")

    if keuze in demos:
        demos[keuze]()