from random import randint

def generuj2():
    tablica = []
    i = 1
    while i <= 10:
        wylosowana_liczba = randint(1, 20)
        while wylosowana_liczba in tablica:
            wylosowana_liczba = randint(1,20 )
        else:
            tablica.append(wylosowana_liczba)
        i += 1
    return tablica

def czesc_wspolna(tab1,tab2):
    tab_wynik = []
    i = 0
    j = 0
    while i < len(tab1):
        j = 0
        while j < len(tab2):
            if tab1[i] == tab2[j]:
                tab_wynik.append(tab1[i])
            j += 1
        i += 1
    w = list(set(tab_wynik))
    return w

def suma(tab1,tab2):
    i=0
    tablica_wynik = tab1[:]
    while i < len(tab2):
        tablica_wynik.append(tab2[i])
        i+=1
    w = list(set(tablica_wynik))
    return w

def roznica(t1,t2):
    tablica_wynikow = []
    i = 0
    while i < len(t1):
        while t1[i] in t2:
            i +=1
        else:
            tablica_wynikow.append(t1[i])
        i += 1
    return tablica_wynikow


    w = list(set(tablica_wynikow))
    return w




tab1 = generuj2()
tab2 = generuj2()

print(f"Wylosowany zbior 1: {tab1}")
print(f"Wylosowany zbior 2: {tab2}")

wynik = czesc_wspolna(tab1,tab2)
wynik2 = suma(tab1,tab2)
wynik_roznica = roznica(wynik2,wynik)

print(f"Częśc wspolna:      {wynik}")
print(f"Suma:               {wynik2}")
print(f"Wynik roznica:      {wynik_roznica }")
