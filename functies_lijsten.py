def functie(lst):
    lst[2] = 5                  # Hier wordt de lijst buiten de functie aangepast via de verwijzing
    lst = [5,4,3]               # Hier wordt de verwijzing zelf overschreven
    lst[2] = 9                  # Hier wordt alleen de lokale lijst aangepast

lst = [1, 2, 3]
functie(lst)
print(lst)                      # [1, 2, 5]