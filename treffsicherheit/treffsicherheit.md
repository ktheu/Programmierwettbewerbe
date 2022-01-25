## Treffsicherheit

40\. Bundeswettbewerb Informatik - Junioraufgabe 2

[Aufgabenstellung](treffsicherheit.png) - [Beispieldaten](beispieldaten.md) - [Lösungshinweise](Treffsicherheit.pdf)

#### Python

```
k = 1
f = open('./beispieldaten/praeferenzen'+str(k)+'.txt')

'''
Den Kalender modellieren wir als eine Liste von (Zeilen-)Listen

'''
kalender = []
rows, cols = [int(x) for x in f.readline().split()]
for i in range(rows):
    kalender.append([int(x) for x in f.readline().split()])

def istMinimum(a,k):
    '''
    a: Liste mit Zahlen
    k: gültiger Index für a
    returns: True, wenn a[k] Minimum in a ist
    '''
    return a[k] == min(a)


'''
In der Liste aenderungen merken wir uns für jede Spalte (d.h. für jeden
Termin), wie häufig dieser Termin nicht der beste Termin für die
beteiligten Personen ist.
'''
aenderungen = []

for j in range(cols):
    anz = 0
    for i in range(rows):
        if not istMinimum(kalender[i],j):    # kalender[i] = Termine für die i-te Person
            anz+=1
    aenderungen.append(anz)

'''
best = index der Spalte, für die die wenigsten Änderungen nötig sind.
Termin mit index 0 ist der 1. Termin, daher in der Ausgabe best+1
'''
best = aenderungen.index(min(aenderungen))
print(f'Kalender {k}: Fuer Termin {best+1} benoetigt man {aenderungen[best]} Aenderungen.')

```

Ausgabe:

```
Kalender 0: Fuer Termin 6 benoetigt man 2 Aenderungen.
Kalender 1: Fuer Termin 2 benoetigt man 1 Aenderungen.
Kalender 2: Fuer Termin 4 benoetigt man 0 Aenderungen.
Kalender 3: Fuer Termin 18 benoetigt man 7 Aenderungen.
Kalender 4: Fuer Termin 22 benoetigt man 14 Aenderungen.
Kalender 5: Fuer Termin 31 benoetigt man 34 Aenderungen.
```
