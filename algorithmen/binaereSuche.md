## Binäre Suche


```Python
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



