import datetime
rok = int(input("Pofaj rok: "))
miesiac = int(input("Pofaj miesiac: "))
dzien = int(input("Pofaj dzien: "))

now = datetime.datetime.now()
year = int(now.strftime("%Y"))
month = int(now.strftime("%m"))
day = int(now.strftime("%d"))



a = datetime.datetime(2022,3,4)
b = datetime.datetime(rok,miesiac,dzien)
wynik = (a-b).days

print(f"Od {dzien}.{miesiac}.{rok} do dzisiaj: {day}.{month}.{year} mineło: {wynik} dni ")
