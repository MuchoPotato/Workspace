pesel = input("Podaj numer PESEL: ")

# Sprawdzenie, czy numer PESEL składa się tylko z cyfr
if not pesel.isdigit():
    print("Numer PESEL powinien składać się tylko z cyfr.")
else:
    # Sprawdzenie, czy numer PESEL ma 11 cyfr
    if len(pesel) != 11:
        print("Numer PESEL powinien mieć 11 cyfr.")
    else:
        # Sprawdzenie, czy numer PESEL jest poprawny
        weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3, 1]
        sum = 0
        for i in range(11):
            sum += int(pesel[i]) * weights[i]
        if sum % 10 == 0:
            print("Numer PESEL jest poprawny.")
        else:
            print("Numer PESEL jest niepoprawny.")
