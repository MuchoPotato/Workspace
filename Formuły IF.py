#program obliczający bok kwadratu

import math

dana = input("Podaj pole kwadratu: ")
pole = float(dana)

if pole > 0:
    bok = math.sqrt(pole)    
    print ("Bok kwadratu wynosi ",bok)

#I teraz mamy możliowść zrobienia tego poprzez drugie IF
# W ten sposób:

# if pole <=0:
#    print("Wartość nie moze być ujemna lub równa zeru")
#    print ("\nNara")


#Lub poprzez instrukcje Else
# w ten sposób:

# else:
#    print("Wartość nie moze być ujemna lub równa zeru")
#    print ("\nNara")

#  wstawka \n oznacza ze tekst zaczyna się od nowej linijki

else:
    print("Wartość nie moze być ujemna lub równa zeru")
    print ("\nNara")
