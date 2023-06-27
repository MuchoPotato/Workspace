"""
    czy:   el. unikalne | kolejność | zmiana konkretnego el. | nowe elementy
listy          NIE           TAK             TAK                   TAK
krotki         NIE           TAK             NIE                   NIE
słowniki       TAK           NIE             TAK                   TAK
zbiory         TAK           NIE             NIE                   TAK

        ZBIORY: BONUS w postaci | & - ^ 
"""
#zbiory uzywaja { tak jak słowniki ale nie uzywaja kluczy!
zbior = {1,20,3,4,5,20}

#zbiory używają wartości Unikalnych czy nie przechowują powtórzeń
#zbiory nie zachwoują kolejnności, domyślnie przypisują rosnącą
#przykład:
print(zbior) #{1, 3, 4, 5, 20}


"""
Używanie zbiorów jest przydatne wtedy gdy mamy listę gdzie może byc
duzo zduplikowanych wartości - np. baza użytkowników
A my chcemy wyświetlić tylko unikalne wartości
"""

# zmiana listy w zbiór

lista = [1,2,3,3,3,4,55,55,6,6]

#uzywamy funkcji set(NazwaListy)
print (set(lista))#{1, 2, 3, 4, 6, 55}


#usuwanie wartości:
lista.discard(1)
"""
DODATKOWE opcje to
| suma
& Koniunkcja
- minus
^  
"""
zbior1 = {1,2,3,4,5}
zbior2 = {-1, 2,3,33,4}

# & - porównujemy ze sobą kilka zbiorów np. (zbior1 & zbior2)
# w efekcie pokazuje nam tylko wspólne wartosci
print (zbior1 & zbior2) #{2, 3, 4}

# | znak łączy kilka zbiorów i pokazuja wszystkie wartosci, bez powtórzeń (unikalne)
print (zbior1 | zbior2) #{1, 2, 3, 4, 5, 33, -1}

# - usuwa z jednego zbioru zduplikowane wartosci drugiego zbioru
print (zbior1 - zbior2) #{1, 5}
print (zbior2 - zbior1) #{33, -1}

#^ xor/alternatywa wykluczająca, pokazuje tylko zduplikowane wartosci
print (zbior1 ^ zbior2) #{33, 1, 5, -1}

