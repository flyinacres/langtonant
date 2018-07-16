# At white, flip color to 1, turn 90 right, proceed one square
# At black, flip color to 0, turn 90 left, proceed one square

_BLACK = 1
_WHITE = 0

# directions: 0 right, 1 down, 2 left, 3 up
# ant starts on grid at 0, 0
_RIGHT = 0
_DOWN = 1
_LEFT = 2
_UP = 3

def nextXY(direction, x, y):
    if direction == _RIGHT:
        x = x + 1
    elif direction == _DOWN:
        y = y + 1
    elif direction == _LEFT:
        x = x - 1
    else: # Must be _UP direction
        y = y - 1

    return x, y


def printKMoves(K):
    x = K
    y = K
    minx = K
    maxx = K
    miny = K
    maxy = K
    direction = 0
    
    grid = {}
    
    for i in range(K):
        key = str(y) + "," + str(x)
        if key in grid:
            if grid[key] == _BLACK:
                direction = (direction - 1) % 4
            else:
                direction = (direction + 1) % 4
                
            grid[key] = grid[key] ^ 1
        else: # if never before seen, the square must be white
            grid[key] = _BLACK
            direction = (direction + 1) % 4
            
        x, y = nextXY(direction, x, y)
        
        if i < K - 1:
            # Get values to define the grid shape
            if x < minx:
                minx = x
            elif x > maxx:
                maxx = x
            if y < miny:
                miny = y
            elif y > maxy:
                maxy = y
        
        #print(key, grid[key])
        #print("direction = ", direction, ", x = ", x, ", y = ", y)
   # print(minx, maxx)
    #print(miny, maxy)

    for y in range(miny, maxy+1):
        for x in range(minx, maxx+1):
            key = str(y) + "," + str(x)
            if key in grid:
                print(grid[key], end='')
            else:
                print(0, end='')
        print("", end='\n')
        

     
        
printKMoves(11669)

