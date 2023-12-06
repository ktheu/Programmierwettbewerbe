## Itertools

#### Teilmengen

``` 
# Alle 2-elementigen Teilmengen als Tuple
import itertools as it
a = [1,2,3,4]
for x in it.combinations(a,2):
    print(x)
```

``` 
# Alle Teilmengen als Tuple
import itertools as it
a = [1,2,3,4]
for x in it.chain.from_iterable(it.combinations(a, k) for k in range(len(a)+1)):
    print(x)
```

#### Permutationen 

Ziehungen ohne Zurücklegen mit Berücksichtigung der Reihenfolge

``` 
# Alle 2-elementigen Permutationen:
import itertools as it
for x in it.permutations([1,2,3],2):
    print(x)
```

``` 
# Alle Permutationen
import itertools as it
for x in it.permutations([1,2,3]):
    print(x)
```

#### Cartesische Produkte

Ziehen mit Zurücklegen mit Berücksichtigung der Reihenfolge.

``` 
# Alle 2-elementigen cartesische Produkte.
import itertools as it
for x in it.product([1,2,3],repeat=2):
    print(x)
```

#### Beispiele

``` 
# Alle 4-elementige Binärfolgen
import itertools as it
for x in it.product([0,1],repeat = 4):
    print(x)
```

``` 
# Alle n-elementigen Binärfolgen, die an genau k Stellen eine 1 haben, sonst 0.
import itertools as it
n, k = 5, 2
for x in it.combinations(range(n),k):
    print([int(i in x) for i in range(n)])
```

```
# Alle Teillisten einer Liste aufzählen
# Jedes Element kann entweder genommen werden oder nicht, also 2^n Möglichkeiten
a = [10, 9, 2, 5]
iter = it.product([0,1],repeat=len(a))
for selector in iter:
    print([d for d, s in zip(a, selector) if s])
```

```
# Wir wollen alle Möglichkeiten aufzählen der Form:
# 2 mal eine Permutation der Liste [1,2,3] + einmal True oder False
p = list(it.permutations([1,2,3]))
iter = it.product(it.product(p,repeat=2) ,[True,False])
for x in iter:
    print(x)
```
