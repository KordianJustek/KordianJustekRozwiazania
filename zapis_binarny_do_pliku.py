import pickle

koniec_pliku = False

slownik = {"Magdalena":'500100200',"jakub":'501101201','slawek':'503111200' }

plik = open("info.dat","wb")

pickle.dump(slownik,plik)
plik.close()

plik2 = open("info.dat","rb")

while not koniec_pliku:
    try:
        slownik = pickle.load(plik2)
        print(slownik)
    except EOFError:
        koniec_pliku = True
plik2.close()