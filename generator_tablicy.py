
n = 10
#generator:
tab = [[0 for i in range(n) ] for j in range(n)   ]


suma = 0
for i in range(n):
    for j in range(n):
        if i == j:
            tab[i][j] = i
            suma = suma + tab[i][j]

for a in tab:
    print(a)

print(suma)