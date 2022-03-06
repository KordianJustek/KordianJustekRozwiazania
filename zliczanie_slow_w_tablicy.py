zmienna = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."
tab = zmienna.split(" ")

znaki = {}

for slowo in tab:
    znaki[slowo] = znaki.get(slowo,0)+1

print((znaki))

