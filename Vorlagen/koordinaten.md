# Koordinaten

Wir modellieren Koordinate (x/y) als eine Liste mit zwei Zahlen: [x,y]

### Abstand zwischen zwei Koordinaten

und minimaler Abstand zu einer Liste von Koodinaten

```
import math

def abstand(pos1, pos2):
    '''
    pos1, pos2: Koordinaten in der Form [x, y]
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


a = [[0, 0], [0, 1], [1, 1]]
print(minAbstand([1,2],a))
print(minAbstand([-1,2],a))
```

```
Ausgabe:
1.0
1.4142135623730951
```
