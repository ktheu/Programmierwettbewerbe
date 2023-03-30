## Ein/Ausgabe

### Eingabe über stdin

Einen einzelnen Wert pro Zeile

```Python
s = input()                 # einen String
x = int(input())            # eine ganze Zahl
```

Mehrere Werte pro Zeile

```Python
a = input().split()                    # durch leerzeichen getrennte Strings als Liste
a = [int(x) for x in input.split()]    # durch Leerzeichen getrennte Zahlen als Liste
```

### Ausgabe über stdout

Seit Python 3.6 gibt es f-Strings.

```Python
name, alter = 'Lena', 14
print(f'{name} ist {alter} Jahre alt.')     

x = 3.233474234
print(f'x = {x:.0f}')              # gerundet ohne Dezimalstelle
print(f'x = {x:.4f}')              # gerundet mit 4 Dezimalstellen
```

### Eingabe/Ausgabe über Datei durch Umlenken von stdin/stdout

Wenn man stdin/stdout umlenkt, kann man weiter mit input() und print() arbeiten.

```Python
import sys
sys.stdin = open("problem.in", "r")
sys.stdout = open("problem.out", "w")
```

### Lesen einer Datei

```Python
f = open('input.txt')

s = f.readline().strip()           # eine Zeile als String
x = int(f.readline())              # eine Zeile als ganze Zahl

a = f.readline().split()           # Zeile mit Strings
b = [int(x) for x in f.readline().split()]    # Zeile mit ganzen Zahlen
f.close()
```


### Lokale Entwicklung

Die Eingabe geht auf dem Linux-Server über stdin, auf der lokalen Windows-Umgebung
durch Lesen einer Datei input.txt. 

``` Python
import platform, sys
if platform.system() == 'Windows':
    sys.stdin = open("input.txt", "r")
```
