## Lineare Suche und Binäre Suche


#### Lineare Suche

Beispiel: bei welchem Index in der Liste a ist die Zahl, die bei Division durch 17 den größten Rest hat.

```
def lineareSuche(a):
    best = None
    best_val = None  
    for i in range(len(a)):
        val = a[i] % 17               
        if best_val is None or val > best_val:
            best_val = val
            best = i                # hier ist der Index gesucht
    return best   

```

#### Binäre Suche 

```
def binaereSuche(a, x):
    '''
    a: sortierte Liste mit Zahlen
    x: Zahl
    returns: Index von x in a, falls x in a
             -1              , falls x nicht in a
    '''
    links = 0
    rechts = len(a)-1
    mitte = (links + rechts)//2
    while links <= rechts and a[mitte] != x:
        if a[mitte] < x:
            links = mitte + 1
        else:
            rechts = mitte - 1
        mitte = (links + rechts)//2

    if links > rechts:
        return -1
    else:
        return mitte
```



