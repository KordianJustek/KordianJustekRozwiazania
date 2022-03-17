# symulacja zycia komorki
import random,time,copy

WIDTH = 40
HEIGHT = 10

nextCells = []
for x in range(WIDTH):
    colum = []
    for y in range(HEIGHT):
        if random.randint(0,1) == 0:
            colum.append('#')
        else:
            colum.append(' ')
    nextCells.append(colum)

while True:
    print('\n' * 5 )
    currentCell = copy.deepcopy(nextCells)

    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCell[x][y], end='')
        print()
        print

    for x in range(WIDTH):
        for y in range(HEIGHT):
            leftCoord = (x-1) % WIDTH
            rightCoord = (x+1) % WIDTH
            aboveCord = (y-1) % HEIGHT
            belowCord = (y+1) % HEIGHT

        numNeighbors = 0
        if currentCell[leftCoord][aboveCord] == '#':
            numNeighbors +=1
        if currentCell[x][aboveCord] == '#':
            numNeighbors +=1
        if currentCell[rightCoord][aboveCord] == '#':
            numNeighbors +=1
        if currentCell[leftCoord][y] == '#':
            numNeighbors +=1
        if currentCell[rightCoord][y] == '#':
            numNeighbors +=1
        if currentCell[leftCoord][belowCord] == '#':
            numNeighbors +=1
        if currentCell[x][belowCord] == '#':
            numNeighbors +=1
        if currentCell[rightCoord][belowCord] == '#':
            numNeighbors +=1

        #określamy stan komórki
        if currentCell[x][y] == '#' and (numNeighbors == 2 or numNeighbors ==3):
            nextCells[x][y] = '#'
        elif currentCell[x][y] == ' ' and numNeighbors == 3:
            nextCells[x][y] = '#'
        else: nextCells[x][y] = ' '

    time.sleep(1)








