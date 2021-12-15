## Schnipsel

```
a = Liste, m = dictionary, c = Zeichen, i,j,k = ints, x,y = numbers, s = String
n = ganze Zahl
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

a = s.split(' ')   # mit ' '-getrennte Stringteile in eine Liste speichern

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

### Binary, Hex, etc.

```
int('1011',2)    # wandelt binary String in Dezimalzahl
int('01E2',16)   # wandelt hex String in Dezimalzahl
bin(n)           # wandelt in binary String mit Prefix 0b
hex(n)           # wandlet in hex String mit Prefix 0x
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
