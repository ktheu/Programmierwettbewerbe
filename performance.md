### Tipps zur Performance mit Python für CSES-Probleme

PyPy ist schneller als CPython 

---

```
inf = 1<<59   statt  inf = float('inf')   
```


```
a, b = map(int,input().split())  statt    a, b = [int(x) for x in input().split()]
```

```
import stdin, stdout from sys
stdin.buffer.readline()    statt   input()
stdout.write()             statt   print()
```

```
if not condition: continue   statt
if condition:
     weiter()
```

Keine Variablen wegen scheinbarer Doppelberechnung anlegen:

```
if a + b > t:
    t = a + b      statt

c = a + b
if c > t:
    t = c
```

Versuche Matrizen eindimensional zu modellieren:

```
D = [inf]* 250000  statt  D = [[inf] * 500 for _ in range(500)]
D[a + 500*b]       statt  D[a][b] 
```

Nutze join statt String-Concatenation
```
output = " ".join(["Programming" , "is", "fun"])  statt
output = "Programming " + "is " + "fun"
```

Importiere zielgenau
```
from math import sqrt
statt import math 
```

Nutze Mehrfachzuweisungen
```
a, b = 3, 5
statt 
a = 3
b = 5
```

Vermeide Funktionsaufrufe - lieber den Code wiederholen.


 

