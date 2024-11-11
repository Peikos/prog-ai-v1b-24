# we krijgen een lijst l en getal t
# voor elk getal g in l:
  # als g gelijk aan t:
    # geef True, klaar
# als klaar met l:
  # geef False

def search(list, target):
    for v in list:
        if v == target:
            return True
    return False