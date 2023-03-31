### Zahlentheorie

Summe der Zahlen von 1 bis n:

```Python
summe =  n*(n+1)//2
```

#### Euklidscher Algorithmus


```Python
def ggt(a,b):
    '''
    a, b: positive ganze Zahlen
    returns: größten gemeinsamen Teiler von a und b
    '''
    while b != 0:
        a, b = b, a % b
    return a
```

#### Sieb des Eratosthenes 

```Python
def eratosthenes(n):
    '''
    n: positive ganze Zahl
    returns: Liste mit allen Primzahlen <= n
    '''
    tmp = []
    prim = [True] * (n+1)
    for i in range(2,n+1):
        if prim[i]:
            tmp.append(i)
            for j in range(i+i,n+1,i):
                prim[j] = False
    return tmp
```

#### Anzahl der Faktoren

```Python
def anzahlFaktoren(n):
    '''
    n: positive ganze Zahl
    returns: Liste mit den Anzahl der Faktoren aller Zahlen <= n 
    '''
    tmp = [1] * (n+1)
    for i in range(2,n+1):
        for j in range(i,n+1,i):
            tmp[j]+=1
    return tmp
```