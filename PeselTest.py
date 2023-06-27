pesel = input ("Podaj numer PESEL: ")

#sprawdzamy czy numer składa sie z samych cyfr
if not pesel.isdigit():
    print("Podany numer jest błędny")

#Teraz sprawdzam czy czy ma 11 znaków:
    
elif len(pesel) !=11:
    print ("Podany numer ma za mało cyfr")

#Teraz robie wyliczenie matematyczne nr pesel dla weryfikacji

else:
    baza=[1, 3, 7, 9, 1, 3, 7, 9, 1, 3, 1]
    suma=0
    #zmienna i w pentli if bedzie mnożyć po kolei cyfry z listy
    for i in range (11):
        suma += int(pesel[i]) * baza[i]

    if suma % 10 ==0:
        print ("Numer PESEL prawidłowy")

    else:
        print ("Numer PESEL niepoprawny")
