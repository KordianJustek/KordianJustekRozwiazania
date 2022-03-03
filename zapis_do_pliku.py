import os
import string
import tarfile


def katalog():
    katalog = os.getcwd()
    katalog = katalog + "\\nowy"
    print(katalog)
    if os.path.exists(katalog):
        print("istnieje")
    else:
        print("Nie Istnieje")
        os.mkdir(katalog)
    return katalog

def zapisdopliku_parzyste(tablica):
    plik  = open("nowy\parzyste.txt", 'a')
    i = 0
    while i < len(tablica):
        plik.write(str(tablica[i])+"\n")
        i+=1
    plik.close()

def zapisdopliku_nieparzyste(tablica):
    plik  = open("nowy\\nieparzyste.txt", 'a')
    i = 0
    while i < len(tablica):
        plik.write(str(tablica[i]) + "\n")
        i+=1

    plik.close()


kat = katalog()
print()

tablia_parzyste = []
tablia_nie_parzyste = []

while True:
    znak = input("Podaj Liczbe: ")
    if znak == 'x':
        break
    if znak.isdigit():
        if int(znak) % 2 == 0:
            tablia_parzyste.append(znak)
        else:
            tablia_nie_parzyste.append(znak)


zapisdopliku_parzyste(tablia_parzyste)
zapisdopliku_nieparzyste(tablia_nie_parzyste)

print(tablia_parzyste)
print(tablia_nie_parzyste)