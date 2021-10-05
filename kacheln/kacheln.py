import numpy as np
import random


f = open('./beispieldaten/map4_compact.txt')
rows = int(f.readline())*2
cols = int(f.readline())*2

grid = np.zeros((rows, cols), dtype = int)

for i in range(rows):
    zeile = f.readline()
    for j in range(cols):
        grid[i,j] = 9 if zeile[j] == '*'  else int(zeile[j])
f.close()

def spacy(grid):
    print(rows//2)
    print(cols//2)
    print()
    for x in range(rows):
        for y in range(cols):
            if y%2 != 0: print(str(grid[x,y]),end='   ')
            else: print(str(grid[x,y]),end=' ')
        if x%2 == 0: print()
        else: 
            print()
            print()

def inGrid(tup):
    return 0 <= tup[0] < rows and 0 <= tup[1] < cols

def nb(x,y):
    tmp = [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
    return [t for t in tmp if inGrid(t)]
    

def nbforce(x,y):
    xg = x % 2 == 0
    yg = y % 2 == 0
    if xg and yg: tmp = [(x,y-1),(x-1,y)]
    if xg and not yg: tmp = [(x-1,y),(x,y+1)]
    if not xg and not yg: tmp = [(x,y+1),(x+1,y)]
    if not xg and yg: tmp = [(x+1,y),(x,y-1)]
    return [t for t in tmp if inGrid(t)]
    
def go():
    # returns: 0 - wenn unmöglich, 1 - wenn nix geändert, 2 - wenn was geändert, 3 - wenn fertig
    rvalue = 3 
    for x in range(rows):
        for y in range(cols):
            if grid[x,y] == 9:
                if rvalue == 3: rvalue = 1
                mustHave = None
                for xn,yn in nbforce(x,y):
                    if grid[xn,yn] != 9:
                        if mustHave is None:
                             mustHave = grid[xn,yn]
                             grid[x][y] = mustHave
                             rvalue = 2
                        elif grid[xn,yn] != mustHave:
                             return 0
    return rvalue          

def choose():
    for x in range(rows):
        for y in range(cols):
            if grid[x,y] == 9:
                wert = 1 if random.random() < 0.5 else 0

                grid[x,y] = wert
                return
 
k = go()

while k < 3:
    if k == 0: break
    choose()
    k = go()

if k == 3: 
    spacy(grid)
else:
    print('unmöglich')



 

