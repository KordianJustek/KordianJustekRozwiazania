#f0:0
#f1:1
#a(n-2) + a(n-1)
def fiob(n,jeden=0,dwa=1):
    for _ in range(n):
        print(jeden,",", end="",sep="")
        jeden,dwa = dwa,jeden+dwa
fiob(10)

print()
n = 10
tab = []
wynik = 0
for i in range(n):
    if i <= 1:
        tab.append(i)
    if i > 1:
        wynik = tab[i-2]+tab[i-1]
        tab.append(wynik)

print(tab)


