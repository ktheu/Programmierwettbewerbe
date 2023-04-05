## Listen

### Shift/Rotation von Listen

Ein k-facher Linksshift mit wrap-around der Liste a bedeutet, dass die Anfangsliste der Länge k nach hinten verschoben wird.
Eine k-facher Rechtsshift ist ein len(a)-k (oder -k) fache Linksshift.

```Python
def shiftLeft(a,k):
    idx = k%len(a)
    return a[idx:]+a[:idx]

def shiftRight(a,k):
    return shiftLeft(a,-k)
``` 

```Python
a = [0,1,2,3,4,5]
for i in range(5):
    print(i,shiftLeft(a,i))

Ausgabe:
0 [0, 1, 2, 3, 4, 5]
1 [1, 2, 3, 4, 5, 0]
2 [2, 3, 4, 5, 0, 1]
3 [3, 4, 5, 0, 1, 2]
4 [4, 5, 0, 1, 2, 3]
```

### Flatten
Eine Liste von Listen kann mit einer doppelten Listcomprehension geflattet werden.

```Python
aa = [[2, 3, 1], [4, 5], [6, 0]]
b = [x for a in aa for x in a]
print(b)

Ausgabe:
[2, 3, 1, 4, 5, 6, 0]
```
