import os

def odczyt_parzyste():
    dane = []
    with open("nowy\parzyste.txt", "r") as zawartosc:  # otwieramy plik do odczytu
        for linia in zawartosc:
            linia = linia.replace("\n", "")  # usuwamy znaki końca linii
            linia = linia.replace("\r", "")  # usuwamy znaki końca linii
            dane.append(int(linia))
    return dane

def odczyt_nieparzyste():
    dane2 = []
    with open("nowy\\nieparzyste.txt", "r") as zawartosc:  # otwieramy plik do odczytu
        for linia in zawartosc:
            linia = linia.replace("\n", "")  # usuwamy znaki końca linii
            linia = linia.replace("\r", "")  # usuwamy znaki końca linii
            dane2.append(int(linia))
    return dane2

def suma(t1):
    i = 0
    suma = 0
    while i < len(t1):
        suma = suma+t1[i]
        i+=1
    return suma

def srednia(t1):
    i = 0
    suma = 0
    while i < len(t1):
        suma = suma+t1[i]
        i+=1
    return suma/len(t1)


tab1 = odczyt_parzyste()
tab2 = odczyt_nieparzyste()

print(f"Wycztano tablice 1: {tab1}")
print(f"Wczytano tablice 2: {tab2}")
print(f"Suma Tab 1: {suma(tab1)}")
print(f"Suma Tab 2: {suma(tab2)}")
print(f"Srednia Tab 1: {round(srednia(tab1),2)}")
print(f"Srednia Tab 2: {round(srednia(tab2),2)}")
