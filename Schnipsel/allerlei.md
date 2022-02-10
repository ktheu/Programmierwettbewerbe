## Schnipsel

```
a = Liste, m = dictionary, c = Zeichen, i,j,k = ints, x,y = numbers, s = String
n = ganze Zahl.
Bei dicts: k - key, v - value
```

### [Listen](https://docs.python.org/3/tutorial/datastructures.html#)

```
a = []                 # leere Liste

a = [0,1,2,3,4]        # Liste mit Zahlen 0-4
a = list(range(5))     # Liste mit Zahlen 0-4
a.append(5)            # etwas ans Ende der Liste dranhängen
x = a.pop()            # etwas vom Ende der Liste wegnehmen

a.sort()               # eine Liste sortieren (inplace: a wird verändert)
b = sorted(a)          # eine neue sortierte Liste erstellen (a wird nicht verändert)

a = [3,4]
x, y = a               # die Inhalte der Liste Variablen zuweisen (unpack)

```

Eine Liste durchlaufen

```
for i in range(len(a)):    # den Index einer Liste durchlaufen
    print(a[i])

for x in a:                # die Listenelemente durchlaufen
    print(x)
```

### [Strings](https://docs.python.org/3/library/stdtypes.html#string-methods)

```

s.isupper()    # s nur aus Großbuchstaben?
s.islower()
s.isalpha()    # s nur aus Buchstaben?
s.isalnum()    # s nur aus Buchstaben oder Ziffern?
s.isdigit()    # s nur aus Ziffern?
s = s.upper()  # alles in Großbuchstaben
s = s.lower()

s = "10/4+9/3"
s1 = s.replace('/','//')       # alle Vorkommen ersetzen: -> "10//4+9//3"

a = s.split(' ')   # die mit blank getrennten Stringteile in eine Liste speichern

s = 'Michelangelo passes the ball to Raphael'
von, zu = s.split(' passes the ball to ')                # split mit Separator
```

### Zeichen

```
ord(c)           # Unicode-Zahl für Zeichen c, ord('a') = 97, ord('A') = 65
chr(k)           # Zeichen für die Unicode-Zahl
'e' <= c <= 'k'  # Liegt Zeichen c zwischen 'e' und 'k'?

```

### Dictionaries

```
m = {}  oder   m = dict()         # leeres dictionary
m = {'Thorben':2, 'Soeren':3, 'Maike':2}
m['Maike']                      # lookup mit key als Index
m['Lena'] = 1                   # Eintrag hinzufügen
'Meike' in m                    # key vorhanden?
del(m['Soeren'])                # Eintrag löschen
len(m)                          # Die Länge ist die Anzahl der keys

m.keys()                        # die Menge aller keys
list(m.keys())                  # die Menge aller keys als Liste
m.values()                      # die Menge aller values
m.items()                       # die Menge aller (key,value)-Paare

for k in m:                     # die keys des dicts durchlaufen
    print(k, m[k])
```

### Defaultdict

Wird auf einen key zugegriffen, der noch nicht vorhanden ist, so wir ein
default key-value Paar erstellt durch Aufruf der mitgelieferten Funktion. In
den Beispielen: int() liefert 0, list() liefert [].

```
# Hier wird die Buchstabenhäufigkeit gezählt
from collections import defaultdict
s = 'mississippi'
d = defaultdict(int)
for k in s:
    d[k] += 1
```

```
# Die Liste mit den Tupeln wird in ein dict umgewandelt.
a = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in a:
      d[k].append(v)
```

### Itertools

```
import itertools as it
a = [0,1]
iter = it.product(a,repeat = 3)
for x in iter: print(x)

Ausgabe:
(0, 0, 0)
(0, 0, 1)
(0, 1, 0)
(0, 1, 1)
(1, 0, 0)
(1, 0, 1)
(1, 1, 0)
(1, 1, 1)
```

### Binary, Hex, etc.

```
int('1011',2)    # wandelt binary String in Dezimalzahl
int('01E2',16)   # wandelt hex String in Dezimalzahl
bin(n)           # wandelt in binary String mit Prefix 0b
hex(n)           # wandlet in hex String mit Prefix 0x
```

### eval

Eval interpretiert den übergebenen String als Python-Ausdruck oder Anweisung und wertet
den Ausdruck aus bzw. führt die Anweisung aus.

```
s = "10/4+9/3"
print(eval(s))

s = "print('Hello world')"
eval(s)
```

### [Formatierte Ausgabe](https://docs.python.org/3/reference/lexical_analysis.html#f-strings)

```

f'{'E':0>2}'     # rechtsbündig mit führender 0: '0E'

```

### [Datum und Zeit](https://docs.python.org/3/library/datetime.html)

```
import datetime as dt
s = '26.04.2018'
d1 = dt.datetime.strptime(s, '%d.%m.%Y')
(d2-d1).days     # Anzahl Tage zwischen d1 und d2
```
