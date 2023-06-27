"""
Otrzymujesz listę osób które dostaną dostep do tajnych informacji:

imiona = ["Arkadiusz", "Wiola", "Antek"]

jeśli ktoś z listy "imiona" zostanie podany prez użytkownika w zmiennej "imię"
wyświetl:
"Masz dostęp"

w innym przypadku:
"Brak dostępu"
"""

imiona = ["Arkadiusz", "Wiola", "Antek"]
imie = input("Cześc, Podaj imię;")

if (imie in imiona):
    print("Masz dostęp")
else:
    print("Nie masz dostępu")
