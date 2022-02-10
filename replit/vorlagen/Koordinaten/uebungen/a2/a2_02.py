def spalte(grid,k):
    '''
    grid: eine Matrix als Liste von Zeilen-Listen
    k: eine gültiger Spaltenindex für grid
    returns: die k-te Spalte von grid als Liste
    '''

    tmp = []
    for i in range(len(grid)):
        tmp.append(grid[i][k])
    return tmp

def zeile(grid,k):
    '''
    grid: eine Matrix als Liste von Zeilen-Listen
    k: eine gültiger Zeilenindex für grid
    returns: die k-te Spalte von grid als Liste
    '''
    return grid[k]



# Kontrolle
grid = [[0, 0, 0, 0, 0], [1, 0, 0, 3, 1], [2, 2, 2, 1, 2], [2, 1, 1, 5, 2]]
print(spalte(grid,0))
print(spalte(grid,3))
print(zeile(grid,0))
print(zeile(grid,2))


'''
Erwartete Ausgabe:
[0, 1, 2, 2]
[0, 3, 1, 5]
[0, 0, 0, 0, 0]
[2, 2, 2, 1, 2]
'''

