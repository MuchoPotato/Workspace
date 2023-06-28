#test funkcji def
#
# def powitanie (imie):
#     print ("Siema ", imie)
#
# powitanie ("anna")

def oblicz_pole_prostokata(dlugosc, szerokosc):
    pole = dlugosc * szerokosc
    return pole

pole_prostokata = oblicz_pole_prostokata(4, 6)

print("Pole prostokąta wynosi:", pole_prostokata)