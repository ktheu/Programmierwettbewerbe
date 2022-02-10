## Comprehensions

Comprehensions sind spezielle Anweisungen, mit denen eine
Liste, ein Dictionary oder ein Set mit einer Vorschrift erzeugt werden.

### list-Comprehensions

```
>>> [k for k in range(1,10)]
[1, 2, 3, 4, 5, 6, 7, 8, 9]

>>> [k*k for k in range(1,10)]
[1, 4, 9, 16, 25, 36, 49, 64, 81]

>>> a = [4, 7, -3, 9]
>>> [k + 2 for k in a]
[6, 9, -1, 11]

>>> [ord(c) for c in 'Hallo']
[72, 97, 108, 108, 111]

>>> import random as r
>>> b = [r.randint(1,100) for i in range(20)]
>>> b
[41, 28, 58, 80, 64, 4, 5, 35, 39, 59, 22, 21, 44, 59, 21, 64, 32, 8, 98, 67]

>>> # an die Aufnahme in die Liste kann mit if eine Bedingung gestellt werden.
>>> [x for x in b if x % 3 == 0]
[39, 21, 21]

>>> # addiere zwei als Listen dargestellte Vektoren
>>> v1 = [1, 7, -3]
>>> v2 = [-8, 3, 10]
>>> [v1[i] + v2[i] for i in range(3)]
[-7, 10, 7]

>>> # oder so:
>>> [sum(x) for x in zip(v1,v2)]
[-7, 10, 7]

>>> # eine Comprehension kann mehrere for-Bereiche haben
>>> lst1 = list('abc')
>>> lst2 = list('123')
>>> [a+b for a in lst1 for b in lst2]
['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']

>>> # mehrere Inputs als Liste speichern
>>> [int(k) for k in input('Bitte Zahlen mit blank getrennt eingeben: ').split()]
Bitte Zahlen mit blank getrennt eingeben: 4 5 8 2
[4, 5, 8, 2]
```

### dict-Comprehensions

```
>>> namen = ["Donald", "Dagobert", "Daisy", "Gustav"]
>>> {k:len(k) for k in namen}
{'Donald': 6, 'Dagobert': 8, 'Daisy': 5, 'Gustav': 6}

>>> # verdopple für jeden key den Wert
>>> m1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
>>> {k : 2*m1[k] for k in m1}
{'a': 2, 'b': 4, 'c': 6, 'd': 8, 'e': 10}

```

### set-Comprehensions

```
>>> import random as r
>>> {r.randint(1,10) for i in range(10)}
{1, 2, 5, 7, 9, 10}


```
