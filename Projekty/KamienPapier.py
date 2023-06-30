import random

#Zmienne
user_win = 0
computer_win = 0
options = ["k", "n", "p"]

#kod
while True:
    user_input = input("Wybierz: K / P / N albo Q aby wyjść z programu: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue #Ta funkcja wraca do początku IF i robi pętle od nowa
    random_number = random.randint(0,2)
    #  K = 0 P = 1 N = 2
    computer_pick = options[random_number]
    print ("Twój przeciwnik wybrał: ", computer_pick)
    if user_input == "k" and computer_pick == "n":
        print ("Wygrałeś!\n")
        user_win += 1
    elif user_input == "n" and computer_pick == "p":
        print ("Wygrałeś!\n")
        user_win += 1
    elif user_input == "p" and computer_pick == "k":
        print ("Wygrałeś!\n")
        user_win += 1
    else:
        print ("Przegraleś!\n")
        computer_win += 1

print ("\nWygraleś ", user_win, " razy")
print ("Komputer wygrał ", computer_win, " razy")
print ("Dzięki za gre!")

input("\nWcisnij Enter any zakończyć program")