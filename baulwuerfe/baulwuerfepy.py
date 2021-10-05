def solo(x,y):
    '''
    returns: True, wenn an position x, y ein 'X' steht, das kein weiteres 'X' als Nachbar hat.
    '''
    if grid[x][y] != 'X': return False
    for (xn,yn) in nb(x,y):
        if grid[xn][yn] == 'X': return False
    return True

def nb(x,y):
    # returns list of neigbor indices
    tmp = []
    for xd, yd in dirs:
        xn, yn = x+xd, y+yd
        if 0 <= xn < height and 0 <= yn < width:
            tmp.append((xn,yn))
    return tmp

def anzahl(nr):
    global grid, height, width
  
    f = open('./beispieldaten/karte'+str(nr)+'.txt')
    width = int(f.readline())
    height = int(f.readline())
    
    grid = []
    for x in range(height):
        grid.append(list(f.readline())[:width])
        
    allX = sum([grid[x][y] == 'X' for x in range(height) for y in range(width)])
    
    anzSolo = 0
    for x in range(height):
        for y in range(width):
            if solo(x,y):
                anzSolo+= 1

    return int((allX-anzSolo)/10)

N, E, S, W  = (-1,0), (0,1), (1,0), (0,-1)
dirs = [N,E,S,W]

for i in range(7):
    print('Beispiel',i,anzahl(i))    
