## Geometrie 2D

### Euklidsche Distanz zwischen zwei Punkten

```Python
import math
p1, p2 = (0,0), (1,1)
math.dist(p1,p2)
```

### Koordinatenform

Koordinatenform einer Geraden, die durch zwei Punkte gegeben ist. Der Vector (a,b) ist eine
Normale.

```Python
def koordinatenform(p1, p2):
    ''' Geradengleichung a*x + b*y = c '''
    x1, y1 = p1
    x2, y2 = p2
    a = -(y2-y1)
    b = (x2-x1)
    c = a*x1 + b*y1
    return a, b, c
```

### Abstand Punkt-Gerade

```Python
def abstand_punkt_gerade(p, p1, p2):
    '''
    p Punkt, p1-p2 definieren die Gerade g
    returns: Abstand von p zu g.         
    '''
    if p1 == p2: raise Exception(f'keine Gerade durch {p1} und {p2} gegeben')
    x, y = p
    x1, y1 = p1
    x2, y2 = p2
    nx, ny =  -(y2-y1),(x2-x1)  # Normale
    return abs(nx*(x-x1) + ny*(y-y1))/math.sqrt(nx*nx+ny*ny)

```

### Schnittpunkt zweier Geraden

```Python
def schnittpunkt(p1, p2, p3, p4):
    ''' returns Schnittpunkt der beiden Geraden, 
    die durch p1, p2 bzw. p3, p4 gegeben sind '''
    xd = p1[0]-p2[0], p3[0]-p4[0]
    yd = p1[1]-p2[1], p3[1]-p4[1]
    
    def det(a,b):
        return a[0]*b[1]-a[1]*b[0]
    
    div = det(xd,yd)
    if div == 0:
        raise Exception('kein Schnittpunkt')
    d = det(p1,p2), det(p3,p4)
    x = det(d, xd) / div
    y = det(d, yd) / div
    return x, y
```



### Winkel im Dreieck

Winkel in Grad in einem Dreieck.

```Python
def getWinkel(p1,p2,p3):
    '''
    returns: Winkel am Punkt p1 im Dreieck p1-p2-p3
    '''
    dx = p3[0]-p1[0]    # Ziel - Start
    dy = p3[1]-p1[1]
    alpha1 = math.degrees(math.atan2(dy,dx))
    dx = p2[0]-p1[0]    # Ziel - Start
    dy = p2[1]-p1[1]
    alpha2 = math.degrees(math.atan2(dy,dx))
    angle = abs(alpha1-alpha2)
    if angle > 180: angle-= 360
    return abs(angle)
```
