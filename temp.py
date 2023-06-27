#0-200 licz podzielnych przez 5 ale nie przez 7
"""
suma = 0
for i in range (201):
    if (i%5 == 0) and not (i%7 == 0):
        print(i, " ", end="")
        print("jest liczbą podzielna przez 5 ale nie przez 7")
    
    
"""
#Napisz program, który doda 3 parzyste liczby dodatnie podane przez użytkownik

"""
for i in range (3):
    liczba = int(input("Podaj liczbę"))
    if (liczba % 2 == 0):
        i += liczba
    else:
        print("podałeś nieparzystą liczbę")
print("Suma dodawania to ", i)
"""

x = 0
suma = 0
while x<3 :
    liczba = int(input("Podaj liczbę"))
    if (liczba % 2 == 0):
        suma += liczba
        x+=1
    elif liczba<0:
        print("Niestety nie sumuję liczb ujemnych")
        continue
    else:
        print("Podaj liczbe parzystą")
        continue

print("Zsumowałem trzy parzyste liczby, twój wynik to: ", suma)
