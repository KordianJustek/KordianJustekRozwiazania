
a = input("Liczba: ")
a = int(a)

wynik = ""

while a > 0:
    wynik = str(a % 2) + wynik
    a = a // 2
print(wynik)
