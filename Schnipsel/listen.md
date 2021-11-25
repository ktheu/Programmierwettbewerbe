# Listen

```
a = []                 # leere Liste

a = [0,1,2,3,4]        # Liste mit Zahlen 0-4
a = list(range(5))     # Liste mit Zahlen 0-4

a.append(5)            # etwas ans Ende der Liste dranhängen
x = a.pop()            # etwas vom Ende der Liste wegnehmen

a.sort()               # eine Liste sortieren (inplace: a wird verändert)
b = sorted(a)          # eine neue sortierte Liste erstellen (a wird nicht verändert)
```

Liste mit zufälligen Werten erstellen

```
import random
a = []
for k in range(20):
    a.append(random.randint(0,100))

```

Eine Liste durchlaufen

```
for i in range(len(a)):    # den Index einer Liste durchlaufen
    print(a[i])

for x in a:                # die Listenelemente durchlaufen
    print(x)
```

Das größte Element einer Liste finden:

```
bestwert = a[0]
for x in a:
    if x > bestwert:
        bestwert = x
print(bestwert)
```

Den Index des größten Elements finden:

```
bestwert = a[0]
bestindex = 0
for k in range(1,len(a)):
    if a[k] > bestwert:
        bestwert = a[k]
        bestindex = k
print(bestindex)
```
