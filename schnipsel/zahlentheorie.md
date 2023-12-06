### Zahlentheorie

#### Summenformeln


``` 
# Summe der Zahlen von 1 bis n
summe =  n*(n+1)//2
```

``` 
# Geometrische Summenformel: 1 + r + r^2 + ... r^k
r = 0.75
k = 3
summe = (1 - r ** k) / (1 - r)
```


#### Euklidscher Algorithmus

``` 
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

``` 
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

#### Anzahl der Teiler

``` 
def anzahlFaktoren(n):
    '''
    n: positive ganze Zahl
    returns: Liste mit der Anzahl der Teiler aller Zahlen <= n 
    '''
    tmp = [1] * (n+1)
    for i in range(2,n+1):
        for j in range(i,n+1,i):
            tmp[j]+=1
    return tmp
```