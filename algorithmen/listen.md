## Listenoperationen

### Rotation von Listen

Eine n-fache Linksrotation der Liste a bedeutet, dass die Anfangsliste der Länge n nach hinten verschoben wird.
Eine n-fache Rechtsrotation ist eine len(a)-n fache Linksrotation.

```Python
def rotateLeft(a,k):
    return a[k:]+a[:k]

def rotateRight(a,k):
    return rotateLeft(a,len(a)-k)
``` 

```Python
a = [0,1,2,3,4,5]
for i in range(5):
    print(i,rotateLeft(a,i))

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
