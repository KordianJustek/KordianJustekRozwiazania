import string

def usuwanie_zankow(zmienna):
    tablica = []
    i =0
    while i < len(zmienna):
        tablica.append(zmienna[i])
        i+=1
    i =0
    while i < len(tablica):
        if tablica[i] == " " or tablica[i] == "!" :
            del tablica[i]
            continue
        else:
            i+=1
    znaki = ''.join(tablica)
    return znaki

def czy_koniata(zmienna):
    i = len(zmienna)
    if zmienna[i-1] == 'a':
        return "Jest Kobieta"
    else:
        return "Nie jest Kobieta"



sentence = "Kurs Pythona jest prosty i przyjemny"

i = 0
licznik = 0
while i < len(sentence):
    if sentence[i] != " ":
        licznik +=1
    i+=1

print(f"WYRAZENIE: {sentence}")
print(f"Zawiera {licznik} znaków")
print(sentence[18:24])

imie = input("Imie: ")
nazwisko = input("Nazwisko: ")
telefon = input("Telefon: ")

print(f"Czy Imie składa sie z liter: {imie.isalpha()}")
print(f"Czy Nazwisko składa sie z liter: {nazwisko.isalpha()}")
print(f"Czy numer telefonu składa sie z cyfr ?: {telefon.isdigit()}")

print(f"Usuwan space i '!' z imienia:  {usuwanie_zankow(imie.title()) } " )
print(f"Użytkownik: {imie} {czy_koniata(imie)}")
personal = imie + " " + nazwisko + " " + telefon
print(f"Jeden ciąga znaków: {personal}")