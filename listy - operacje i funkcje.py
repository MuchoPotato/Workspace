#len() - długość - length
#.append - dodać
#.extend - rozszerzyć
#.insert(index, co) - wstawić
#.index - indeks danego el.
#sort(reverse=False) - sortuj rosnąco
#max()
#min()
#.count - ile razy coś wystąpi
#.pop - usuń ostatni el.
#.remove - usuń pierwsze wystąpienie
#.clear - wyczyść liste
#.reverse - zamień kolejność


lista1 = [54, 1, -2, 20, 1]
lista2 = [54, 1, -2, 20, 1]
lista3 = ["Arkadiusz", "Wioletta"]

print(len(lista1))

lista1.append([1,2,3,4])#dodaje całą liste do listy  do listy na końcu
#[54, 1, -2, 20, 1, [1, 2, 3, 4]]
print (lista1)

lista2.extend ([1,2,3,4]) #dodała cyfry do listy juz istniejącej
#[54, 1, -2, 20, 1, 1, 2, 3, 4]
print (lista2)

#lista      miejsce   wartosc
lista3.insert (2,     "Kuba")  #wstawia wartość w wyznaczone miejsce
print(lista3)
