nr = 1
f = open('./beispieldaten/wintervorrat'+str(nr)+'.txt')
xmax, ymax = [int(x) for x in f.readline().split()]
anzVoegel = int(f.readline())
voegel = []
for i in range(anzVoegel):
    x, y, t, r = f.readline().split()
    voegel.append((int(x), int(y), int(t), r))
    
print(voegel)

 
grid = [[0]*xmax for i in range(ymax)]
for i in range(xmax*ymax):
    x = i % xmax
    y = int(i / xmax)
    grid[y][x] = i

 
def showGrid():
    for row in grid:
        print(row,sep=' ')

N, E, S, W  = (-1,0), (0,1), (1,0), (0,-1)

def newpos(pos,richtung,plus):
    xn = richtung[0] if plus else -richtung[0]
    yn = richtung[1] if plus else -richtung[1]
    return (pos[0] + xn, pos[1] + yn)

def fly(start,richtung,anzahl):
    '''
    start = (x/y) startkoordinate, richtung = N,E,S,W,
    anzahl = anzahl flugschritte
    returns: Liste mit den Koordinaten pro Flugschritt
    '''
    zaehl = 0
    pos = start
    tmp = [start]
    plus = True
    for i in range(anzahl-1):
        pos1 = newpos(pos,richtung,plus)
        tmp.append(pos1)
        anzahl+=1
        if richtung == E and pos1[1] == xmax - 1:
            plus = False
        if richtung == W and pos1[1] == 0:
            plus = False
        if richtung == S and pos1[0] == ymax - 1:
            plus = False
        if richtung == N and pos1[0] == 0:
            plus = False
        elif pos1 == start:
            plus = True
        pos = pos1
       
    return tmp

def vogelfly(vogel):
    x, y, zeit, richtung = vogel
    if richtung == 'N': richtung = S
    elif richtung == 'S': richtung = N
    elif richtung == 'W': richtung = W
    elif richtung == 'O': richtung = O
    tmp = [(0,0)]*zeit
    return tmp + fly((y,x),richtung,720-zeit)

                      
showGrid()

v = voegel[0]
print(vogelfly(v))
            
        
        
