#palindrom

def sprawdzam(n):
    temp = list(str(n))
    temp.reverse()
    temp2 = "".join(temp)
    temp1 = str(n)
    if temp1 == temp2 :
        return True
    else:
        return False

def licze(n):
    temp = list(str(n))
    temp.reverse()
    temp2 = "".join(temp)
    temp1 = str(n)
    if temp1 == temp2:
        pass
    else:
        return temp2

liczba = input("Liczba ")
i = 0
while True:
    t = liczba
    if sprawdzam(liczba) == True:
        print(liczba)
        break
    if sprawdzam(liczba) == False:
        print(licze(t))
        suma = int(t) + int(licze(t))
        liczba = suma

    i +=1
    if i > 1000:
        break
print("ilośc powtorzen petli: ",i+1)


