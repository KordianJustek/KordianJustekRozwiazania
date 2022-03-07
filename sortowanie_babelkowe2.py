
tablica = [3,44,38,5,47,36,27,2,46,48,50]
#tablica = [1,2,3,6,5,7,8,9,10,11]
print(tablica)
licznik = 0
swapped = True
temp = 0

while swapped:
    swapped = False
    for i in range(len(tablica)-1 - temp):
        print(licznik)
        licznik +=1
        if tablica[i] > tablica[i+1]:
            tablica[i],tablica[i+1] = tablica[i+1],tablica[i]
            swapped = True
    temp +=1

print(tablica)