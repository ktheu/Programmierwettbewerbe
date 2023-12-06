## Listen

#### Shift/Rotation von Listen

Ein k-facher Linksshift mit wrap-around der Liste a bedeutet, dass die Anfangsliste der Länge k nach hinten verschoben wird.
Eine k-facher Rechtsshift ist ein len(a)-k (oder -k) fache Linksshift.

``` 
def shiftLeft(a,k):
    idx = k%len(a)
    return a[idx:]+a[:idx]

def shiftRight(a,k):
    return shiftLeft(a,-k)
``` 

#### Flatten

Eine Liste von Listen kann mit einer doppelten Listcomprehension geflattet werden.

``` 
aa = [[2, 3, 1], [4, 5], [6, 0]]
b = [x for a in aa for x in a]
```
