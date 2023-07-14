#import modułu OS ktory pozwala kontrolować srodowisko systemu
import os

#zmienna która bedzie pokazywać ilość plików i rozmiar
totalbytes = 0

#wyciaganie listy plików w lokalizacji
dirlist = os.listdir()
for entry in dirlist:
    #sprawdzanie czy są tylko pliki bo nie chcemy folderów
    if os.path.isfile(entry):
        #jeżeli są, to dodajemy do totalbytes
        filesize = os.path.getsize(entry)
        totalbytes += filesize

#Tworzymy folder
os.mkdir("Results")

#tworzymy plik zip który bedzie w folderze

resultfile = open("Results/results.txt", "w+")
if resultfile.mode == "w+": #Sprawdzaie czy plik jest w trypie zapisu - czyli W+
    resultfile.write ("total bytecount: " + str(totalbytes) + "\n") # write zapisuje dane do pliku
    resultfile.write ("file list: \n") # kolejna linijka tekstu
    resultfile.write ("-------------------- \n") #ozdobnik

    for entry in dirlist:
        if os.path.isfile(entry):
            resultfile.write(entry+"\n")

    resultfile.close() #zamykamy plik który edytowalismy
