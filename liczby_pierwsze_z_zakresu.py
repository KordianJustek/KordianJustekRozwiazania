
def f(x): return x % 2 != 0 and x %3 != 0

print( list(filter(f,range(10,25))) )