tekst=input("Podaj tekst do zaszyfrowania: ")
tekst=tekst.upper().strip()
szyfr = ""

for znak in tekst:
    if znak.isalpha():
        if znak == "Z":
            znak = "A"
        else:
            znak = chr(ord(znak) + 1)
        szyfr += znak

print(szyfr)
