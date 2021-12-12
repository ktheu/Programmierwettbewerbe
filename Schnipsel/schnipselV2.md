## Schnipsel

```
a = Liste, m = dictionary, c = Zeichen, i,j,k = ints, x,y = numbers, s = String
n = ganze Zahl
```

### [Strings]

```
s = 'Michelangelo passes the ball to Raphael'
von, zu = s.split(' passes the ball to ')                # split mit Separator

s.isupper()    # s nur aus Großbuchstaben?
s.islower()
s.isalpha()    # s nur aus Buchstaben?
s.isalnum()    # s nur aus Buchstaben oder Ziffern?
s.isdigit()    # s nur aus Ziffern?
s = s.upper()  # alles in Großbuchstaben
s = s.lower()


```

### Zeichen

```
ord(c)           # Unicode-Zahl für Zeichen c, ord('a') = 97, ord('A') = 65
chr(k)           # Zeichen für die Unicode-Zahl
'e' <= c <= 'k'  # Liegt Zeichen c zwischen 'e' und 'k'?

```

### Binary, Hex, etc.

```
int('1011',2)    # wandelt binary String in Dezimalzahl
int('01E2',16)   # wandelt hex String in Dezimalzahl
bin(n)           # wandelt in binary String mit Prefix 0b
hex(n)           # wandlet in hex String mit Prefix 0x
```

### Formatierte Ausgabe

```

f'{'E':0>2}'     # rechtsbündig mit führender 0: '0E'

```

### Datum und Zeit

```
import datetime as dt
s = '26.04.2018'
d1 = dt.datetime.strptime(s, '%d.%m.%Y')
(d2-d1).days     # Anzahl Tage zwischen d1 und d2
```
