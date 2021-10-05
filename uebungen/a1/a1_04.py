

import math

def abstand(pos1, pos2):
    '''
    pos1: Koordinate in der Form [x, y] 
    pos2: wie pos1
    returns: abstand zwischen pos1 und pos2
    '''
    return math.sqrt((pos2[0]-pos1[0])**2 + (pos2[1]-pos1[1])**2)

def minAbstand(pos,a):
    '''
    pos: Koordinate der Form [x,y]
    a: eine (nicht leere) Liste von Koordinaten
    returns: den kleinsten Abstand von pos zu einer Koordinate in a
    '''
    minab = abstand(pos,a[0])
    for x in a:
        ab = abstand(pos,x)
        if ab < minab:
            minab = ab
    return minab

# Kontrolle
a = [[0, 0], [0, 1], [1, 1]]
print(minAbstand([1,2],a))
print(minAbstand([-1,2],a))

'''
Erwartete Ausgabe:
1.0
1.4142135623730951
'''
       
