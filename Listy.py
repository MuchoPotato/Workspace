#Lista to kontener do przechowywania wielu elementów
#Do tych elementów mozemy sie odnosic, dodawac, usuwac itp

#Kazdy element, niezależnie od typu, ma swój numer porządkowy
imiona = ["kuba", "anna", "wiola", "arek", "stefan"]
        #   0        1        2       3        4
        
liczby = [3,44,-3,444,2323]
mieszane = [2,"aaa", 333, "kubek"]

print(imiona)

#Można sie odnosić do każdego z elementów osobno poprzez [nr porzadkowy]
print (imiona[0])
print (imiona[1])
print (imiona[2])
print (imiona[3])
print (imiona[4])

#możemy liczyć też "od końca" poprzez -1, -2 itd...
# -1 to "ostati element" gdy np. nie wielu ile jest elementów w liście

#ostatni element
print(imiona[-1])

#przed ostatni element
print (imiona[-2])

#ZMIANA wartości w liście, dodanie, odjęcie elementu

#lista    pozycja    nowa wartośc
imiona     [-1]    =  "wojtek"    

print(imiona[-1])
print('')
print('')
print('')
#
#

#in
#not In
#Operacje na listach

listaimion = ["kuba", "anna", "wiola", "arek", "stefan", "wojtek"]
listaliczb = [3, 12, 24, -8]

print("wojtek" in listaimion) # wyświetli True of Falase

if ("wojtek" in listaimion):
    print("Cześć wojtek")
    
if (2 not in listaliczb):
    print("nie ma liczby 2")
else:
    print("2 jest w liście")

#łączenie list

print([3,44,222] + listaliczb)
print(listaliczb)
#takie połączenie nie jest twałe i odnosie sie tylko do printa
#jeżeli chcemy na trwałe połączyc listy, to musimy uzyc =

listaliczb = [3,44,222] + listaliczb
print(listaliczb)

#możemy też użyć * aby wyświetlić liczbę kilkukrotnie

print(4 * listaliczb)






