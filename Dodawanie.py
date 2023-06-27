print ("Witam w chujowym kalkulatorze")
print ("Wybierz operację, którą chcesz wykonać")
print("")
akcja = input("""
1 - dodawanie
2 - odejmowanie
3 - mnożenie
4 - dzielenie
5 - potęgowanie
: """)
print ("")

a = int(input("Podaj pierwszą liczbę: "))
b = int(input ("Podaj drugą liczbę: "))
          
if (akcja=="1"):
    print (a+b)
elif (akcja=="2"):
    print (a-b)
elif (akcja=="3"):
    print (a*b)
elif (akcja=="4"):
    if a == 0 or b == 0:
        print("Nie dziel przez zero!")
    else:
        print (a/b)
elif (akcja=="5"):
    print (a**b)
else:
    print("nie wybrałeś prawidlowej opcji")


    
