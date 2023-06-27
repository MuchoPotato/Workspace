# TYPY ZAGNIEŻDZONE, wypisanie wartości

imie = "Arkadiusz"
wiek = 29
plec = "mężczyzna"

imie2 = "Wioletta"
wiek2 = 23
plec2 = "kobieta"


osoba1 = ('Arkadiusz', 29, 'mężczyzna')
osoba2 = ('Wioletta', 23, 'kobieta')
osoba3 = ('Kuba', 33, 'mężczyzna')
 
listaGosci = [
                ('Arkadiusz', 28, 'mężczyzna', "666-999-000"),
                ('Wioletta', 22, 'kobieta', "666-999-111"),
                ('Kuba', 32, 'mężczyzna', "666-999-222")  
             ]
listaGosci2 = [
                ('Arkadiusz', 28, 'mężczyzna'),
                ('W', 22, 'kobieta'),
                ('K', 32, 'mężczyzna')  
             ]

 
for imie, wiek, płeć, telefon in listaGosci:
    print ("Imię", imie)
    print ("Wiek", wiek)
    print ("Płeć", płeć)
    print ("\n")

pytanie = input("Czy dodać numery telefonu?; ")

if "tak" in pytanie:
    for imie, wiek, płeć, telefon in listaGosci:
        print ("Imię", imie)
        print ("Wiek", wiek)
        print ("Płeć", płeć)
        print ("Telefon", telefon)
        print ("\n")
else:
    print ("Okey!")
