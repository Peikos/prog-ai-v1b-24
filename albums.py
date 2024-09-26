print("Les 7 - Collections, Errors en Random")

# Database en album-collectie

albums = {
    "MarvinGaye1971": {"artist": "Marvin Gaye", "album": "What’s Going On", "year": 1971},
    "BeachBoys1966": {"artist": "The Beach Boys", "album": "Pet Sounds", "year": 1966},
    "JoniMitchell1971": {"artist": "Joni Mitchell", "album": "Blue", "year": 1971},
    "StevieWonder1976": {"artist": "Stevie Wonder", "album": "Songs in the Key of Life", "year": 1976},
    "Beatles1969": {"artist": "The Beatles", "album": "Abbey Road", "year": 1969},
    "Nirvana1991": {"artist": "Nirvana", "album": "Nevermind", "year": 1991},
    "FleetwoodMac1977": {"artist": "Fleetwood Mac", "album": "Rumours", "year": 1977},
    "Prince1984": {"artist": "Prince and the Revolution", "album": "Purple Rain", "year": 1984},
    "BobDylan1975": {"artist": "Bob Dylan, ‘", "album": "Blood on the Tracks", "year": 1975},
    "LaurynHill1998": {"artist": "Lauryn Hill", "album": "The Miseducation of Lauryn Hill", "year": 1998},
    "Beatles1966": {"artist": "The Beatles", "album": "Revolver", "year": "1966"}
    }

my_collection = { "MarvinGaye1971", "LaurynHill1998", "Beatles1966", "Beatles1969" }

# Oefeningen

# Hoe kan ik nu het beste een album uit de database aan mijn collectie toevoegen?
    # Schrijf een functie die een album toevoegt

def add_album(tag):
    pass

# Wat is het verschil tussen myBands1 en myBands2? Welke is in dit geval 'beter'?

def my_bands1():
    return [ albums[tag]["artist"] for tag in my_collection ]

def my_bands2():
    return { albums[tag]["artist"] for tag in my_collection }

# Voeg het album "tag" toe met de add_album functie hierboven. Roep nu een van beide my_bands aan. Wat gebeurt er?
    # Pas de functie add_album aan zodat deze een error geeft bij het toevoegen van een niet bestaande album-tag.



# Maak een functie die true geeft als ik een album uit een gegeven jaar bezit

def bezit_album_jaar(jaar):
    pass

# Print de namen van mijn albums, gesorteerd op jaar

def mijn_albums():
    pass

# Kies een random album uit mijn collectie om af te spelen

def random_owned_album():
    pass

# Kies een random album dat ik nog niet bezit om mijn waardebon te verzilveren

def random_unowned_album():
    pass

# Gegeven een naam van een artiest, geef een random album uit albums.
# Extra: Als de artiest niet in de database bekend is, geef een error.

def random_album_by(artist):
    pass

# Exporeer een JSON met de gegevens van alle albums in mijn collectie

def export_collection_json(filename):
    pass

# Importeer een JSON file om de albumlijst uit te breiden

def load_json_update_collection(filename):
    pass
