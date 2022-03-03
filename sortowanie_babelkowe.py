def sortowanie_babelkowe(lista):
    n = len(lista)

    while n > 1:
        zamien = False
        for l in range(0, n - 1):
            if float(lista[l]) > float(lista[l + 1]):
                lista[l], lista[l + 1] = lista[l + 1], lista[l]
                zamien = True

        n -= 1
        if zamien == False: break

    return lista