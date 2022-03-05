
def czy_przystepny(a):
    return (a % 4 == 0) and (a % 100 != 0) or (a % 400 == 0)



a = int(input("Podaj rok: "))
print(czy_przystepny(int(a)))