#Dictionary / Słownik
#słownik uzywa nawiasów klamrowych {}
#Słownik to pojemnik do przechowywania danych
#Działa na zasadzie KLUCZ - WARTOŚĆ

# nazwa  klucz   wartość  kolejny klucz   kolejna wartość 
pokoje =  {49:    "Jakub",     69:          "Marzenka"}

#kluczem jest 49 i 69 i pod nimi jest informacja o Kubie i Marzence

#kluczami mogą byc tez słowa (stringi)Może byc tez inna forma zapisu

ksiega = {
    "imie": "jakub",
    "Stan": "Żonaty",
    "nazwisko": "Łogusz"
    }

"""
#dodawanie wielu elementów jednoczesnie do slownika
pokoje.update({1: "Jasiu Kowalski", 2: "Jan Kowalski"})

#usuwanie
del(pokoje[1])
#lub
pokoje.pop(1)
#lub
pokoje.popitem()

#usuwanie wszystkiego ze słownika
pokoje.clear()

print(pokoje)
print(ksiega)
"""
