## Kassiopeia

34\. Bundeswettbewerb Informatik - Junioraufgabe 2

[Aufgabenstellung](kassiopeia.pdf) - [Beispieldaten](beispieldaten.md) -  [Lösungshinweise](kassiopeia_loesung.pdf) 

#### Pseudocode und Datenstrukturen

```
Die Eingabe lesen wir in eine zweidimensionale Liste grid (eine Liste der Zeilen).
Dabei ist grid[x][y] das Element in Zeile x und Spalte y.
Die Positionen (state) modellieren wir als Tupel (x,y).

Starte von der Startposition (startstate) eine Breitensuche und zähle dabei, wieviele
Felder besucht wurden.
```
```
Breitensuche (bfs):

Die noch zu untersuchenden Positionen werden in einer Schlange verwaltet (frontier)
Die schon besuchten Positionen werden in einem Set gespeichert (visited)

füge den startstate in die Schlange frontier ein
initialisiere ein leeres set visited

solange noch etwas in der frontier:
     state = das nächste Element der frontier
     kennzeichne state als besucht
     für alle Nachbarn von state:
         falls sie noch nicht besucht wurden:
             füge sie in die frontier ein

gib die Anzahl der besuchten Positionen zurück

```


#### Python

```
from collections import deque
def bfs(s):
    frontier =  deque([s])
    visited = set()
    while frontier:
        state = frontier.popleft()
        visited.add(state)
        for v in nextstates(state):
            if v not in visited:
                frontier.append(v)
    return len(visited)
            
def nextstates(state):
    x0, y0 = state
    tmp = []
    for x1, y1 in dirs:
        x, y = x0+x1, y0+y1
        if 0 <= x < rows and 0 <= y < cols and grid[x][y] != '#':
            tmp.append((x,y))
    return tmp

def check(nr):
    global rows, cols, grid
    f = open('./beispieldaten/kassiopeia'+str(nr)+'.txt')
    rows, cols = [int(k) for k in f.readline().split()]
    grid = [list(f.readline().strip()) for i in range(rows)]
    f.close()

    countWhite = 0
    startstate = None
    for y in range(cols):
        for x in range(rows):
            if grid[x][y] == 'K':
                startstate = (x,y)
            if grid[x][y] != '#':
                countWhite+=1
     
    if bfs(startstate) == countWhite:
        return "Ja"
    else:
        return "Nein"

#  grid[x][y] ist Element in Zeile x und Spalte y
N, E, S, W  = (-1,0), (0,1), (1,0), (0,-1)
dirs = [N,E,S,W]

for i in range(8):
    print('kassiopeia',i,check(i))
```

Ausgabe:

```
kassiopeia 0 Ja
kassiopeia 1 Nein
kassiopeia 2 Ja
kassiopeia 3 Ja
kassiopeia 4 Ja
kassiopeia 5 Ja
kassiopeia 6 Ja
kassiopeia 7 Ja
```