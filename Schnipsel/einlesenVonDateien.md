# Einlesen von Dateien

### Einlesen von Zahlen

```
'''
Die erste Zahl ist die Anzahl der folgenden Datensätze.
Jede Zeile des Datensatzes besteht aus einer Zahl.

4
10
20
30
40
'''

f = open('./daten1.txt')
anzahl = int(f.readline())

zahlen = []
for i in range(anzahl):
    zahlen.append(int(f.readline()))
f.close()

print(zahlen)
```

```
Ausgabe:
[10, 20, 30, 40]
```

---

### Einlesen von Strings und Zahlen

```
'''
Die erste Zeile besteht aus 2 Zahlen. Sie geben an,
wieviele Farben und wieviele Zahlen folgen.

3 5
rot
grün
gelb
10
20
30
40
50
'''

f = open('./daten2.txt')
anz1, anz2 = [int(x) for x in f.readline().split()]

farben = []
zahlen = []
for i in range(anz1):
    farben.append(f.readline().strip())

for i in range(anz2):
    zahlen.append(int(f.readline()))
f.close()

print('Anzahl Farben:',anz1)
print('Anzahl Zahlen:',anz2)
print(farben, zahlen)
```

```
Ausgabe:
Anzahl Farben: 3
Anzahl Zahlen: 5
['rot', 'grün', 'gelb'] [10, 20, 30, 40, 50]
```

---

### Einlesen von Koordinaten

```
'''
Die erste Zeile ist die Anzahl der folgenden Datensätze.
Jeder folgende Datensatz ist eine Koordinate bestehend aus 2 Zahlen.

4
4 5
3 8
1 2
3 -2
'''

f = open('./daten3.txt')
anzahl = int(f.readline())
daten = []

for i in range(anzahl):
    daten.append([int(x) for x in f.readline().split()])
f.close()

print("Anzahl Koordinaten:", anzahl)
print(daten)

```

```
Ausgabe:
Anzahl Koordinaten: 4
[[4, 5], [3, 8], [1, 2], [3, -2]]
```

---

### Einlesen einer Matrix (grid) aus Zahlen

```
'''
In der ersten Zeile stehen die Anzahl Zeilen und die Anzahl Spalten
der folgenden Matrix aus Zahlen.

3 5
1 0 1 3 1
0 0 1 1 2
2 1 1 2 1
'''

f = open('./daten4.txt')
rows, cols = [int(x) for x in f.readline().split()]

grid = []
for i in range(rows):
    grid.append([int(x) for x in f.readline().split()])
f.close()

print("Anzahl Zeilen:", rows)
print("Anzahl Spalten", cols)
print(grid)
```

```
Ausgabe:
Anzahl Zeilen: 3
Anzahl Spalten 5
[[1, 0, 1, 3, 1], [0, 0, 1, 1, 2], [2, 1, 1, 2, 1]]

```
