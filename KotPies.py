kot = "^^===/"
pies = "O===/"


print("WITAM W PROGRAMIE SPRAWDZAJĄCYM ZWIERZO-LUBNOŚĆ")
print("Odpowiedz na to jedno pytanie")
print("")
print("")
pytanie = input("Wolisz kota czy psa? ")


if "kot" in pytanie.lower():
    print(kot)
    
elif "pies" in pytanie.lower():
    print (pies)
    
else:
    print("Nie kumam")

input("\nWcisnij Enter any zakończyć program")
