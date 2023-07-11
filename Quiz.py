# działania na dwóch zmiennych
x = 10
y = 3
print(x+y)
print(x*y)
print(x/y)
print(x-y)

# stworz liste od 0 do 100 skladajaca sie tylko z liczb parzystych
#wyświetl 10 pierwszych elementów i pokaz dlugość listy
#zappenduj jakąś wartość do utworzonej listy

list = list(range(0,101,2))
print (list)
print (list[0:10])
print (len(list))
list.append("dupa")
print (list)
# utworz dowolna zmienna liczbowa i przy pomocy pętli if sprawdz czy jest podzielna przez 5
liczba = 3344232325
if liczba % 5 == 0:
    print ("licba podzielna przez 5")
else:
    print ("Liczba nie podzielna przez 5")

#uzywaja pętli fOR wyświetl liczby od 0 do 5

for i in range (6):
    print (i)

#Pitagoryjska trójka a,b,c
def pitupitu (a,b,c):
    if a**2 + b**2 == c**2:
        return True
    else:
        return False
print (pitupitu(3,4,5))
print (pitupitu(3,9,15))

#Stworz wykres dla dwóch list z pięcioma liczbami i wyświetl je na wykresie względem siebie
#uzywajac matplotlib

import matplotlib.pyplot as plt

lista1 = [1,7,13,16,24]
lista2 = [3,7,17,28,30]

plt.plot(lista1, lista2, c="blue", linewidht=1, label="A Line!", linestyle="dashed", marker="s", markerfacolor="purple", markersize=2)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.tittle ("Python plot of a line")
plt.legend()
plt.show()
