# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
# The element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,¡­Y-1.
# Example
# Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

x = 3
y = 5
i = 0
j = 0

tab = []
while i < x:
    tab2 = []
    j = 0
    while j < y:
        tab2.append(i*j)
        j+=1
    tab.append(tab2)
    i+=1

print( tab)

#tablica 3 wymiarowa:
array = [[ ['*' for col in range(6)] for col in range(4)] for row in range(3)] # na koncu jest 1 element