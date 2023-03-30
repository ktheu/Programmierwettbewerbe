## Itertools

Nützlich for complete search (=brute force) Ansätze.

### Teilmengen

Alle 2-elementigen Teilmengen als Tuple

```Python
import itertools as it
a = [1,2,3,4]
for x in it.combinations(a,2):
    print(x)
```

Alle Teilmengen als Tuple

```Python
import itertools as it
a = [1,2,3,4]
for x in it.chain.from_iterable(it.combinations(a, k) for k in range(len(a)+1)):
    print(x)
```

### Permutationen 

Ziehungen ohne Zurücklegen mit Berücksichtigung der Reihenfolge

Alle 2-elementigen Permutationen:

```Python
import itertools as it
for x in it.permutations([1,2,3],2):
    print(x)
```

Alle Permutationen

```Python
import itertools as it
for x in it.permutations([1,2,3]):
    print(x)
```

### Cartesische Produkte

Ziehen mit Zurücklegen mit Berücksichtigung der Reihenfolge.

Alle 2-elementigen cartesische Produkte.


```Python
import itertools as it
for x in it.product([1,2,3],repeat=2):
    print(x)
```

### 0-1 Folgen

Alle 4-elementige Binärfolgen

```Python
import itertools as it
for x in it.product([0,1],repeat = 4):
    print(x)
```

Alle n-elementigen Binärfolgen, die an genau k Stellen eine 1 haben, sonst 0.

```Python
import itertools as it
n, k = 5, 2
for x in it.combinations(range(n),k):
    print([int(k in x) for k in range(n)])
```
