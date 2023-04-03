## Sort

```Python
a = [4,2,1,5]
a.sort()                # inplace: a wird sortiert
b = sorted(a)           # a bleibt unverändert

a.sort(reverse = True)
b = sorted(b, reverse = True)
```

Mit Schlüsselfunktion sortieren

```Python
def f(x):
    return x % 5

a = [45, 97, 80, 23, 28, 66, 45, 37, 3]
a.sort(key = f)
```

Meist nutzt man eine anonyme Funktion (lambda-Funktion)

```Python
a = [45, 97, 80, 23, 28, 66, 45, 37, 3]
a.sort(key = lambda x : x % 5)
b = sorted(a, key = lambda x : x % 5)

a.sort(key = lambda x : x % 5, reverse = True)
b = sorted(a, key = lambda x : x % 5, reverse = True)
```

### Nach mehreren Kriterien sortieren

Zunächst nach der ersten Stelle abwärts, dann nach der 2. Stelle aufwärts sortieren.

```Python
a = [(1, 'a'), (3, 'c'), (1, 'b'), (2, 'c'), (3, 'a'), (2, 'd')]
a.sort(key = lambda x : (-x[0],x[1]))
print(a)

Ausgabe:
[(3, 'a'), (3, 'c'), (2, 'c'), (2, 'd'), (1, 'a'), (1, 'b')]
```

Nach der ersten Stelle aufwärts, dann nach der 2. Stelle abwärts sortieren.

```Python
a = [(1, 'a'), (3, 'c'), (1, 'b'), (2, 'c'), (3, 'a'), (2, 'd')]
a.sort(key = lambda x : (x[0],-ord(x[1])))
print(a)

Ausgabe:
[(1, 'b'), (1, 'a'), (2, 'd'), (2, 'c'), (3, 'c'), (3, 'a')]
```
