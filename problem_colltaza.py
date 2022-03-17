
def colltaz(value):
    if value % 2 == 0:
        return value / 2
    else:
        return 3 * value + 1

try:
        value = input("PROBLEM COLTAZA\nPodaj liczbę całkowitą: ")
        while colltaz(int(value)) > 1:
            l = colltaz(int(value))
            print(round(l))
            value = l
        print(1)

except ValueError:
    print("Musisz podać liczbę cakowitą")
