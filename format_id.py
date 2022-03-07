x = 100
print(format(id(x), 'x'))
s = 'w3resource'
print(format(id(s), 'x'))

print(format( 16,'x'))

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

# id() - zwraca numer obiektu
#format - formatuje napis zgodnie ze wzrocem