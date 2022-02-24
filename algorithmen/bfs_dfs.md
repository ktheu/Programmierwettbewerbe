## Breitensuche und Tiefensuche

In vielen Problemstellung geht es darum, in einer (meist sehr großen) Menge von Möglichkeiten
eine Lösung zu finden. Beispiel: 8-Puzzle

<img src='./such_bild1.png'>

Einzelne Spielstellungen stellen wir uns als Knoten vor. Die Kanten zwischen den Knoten sind mögliche Spielzüge.
Die Startstellung ist die Wurzel eines Suchbaums, in dem wir einen Pfad zu einem Knoten suchen, der den **goaltest** besteht.

### Bäume

Begriffe im Zusammenhang mit Bäumen

<img src='./baum.png'>

Ein einfacher Beispielbaum mit Zahlen als Knoten:

<img src='./zahlenbaum.png'>

```
baum = {1:[12,6,7], 12: [14,22,10], 6: [4,8], 7: [2,18], 22:[3,9], 2:[13]}
```

### Breitensuche und Tiefensuche

Einen Baum _traversieren_ heißt, nacheinander alle seine Knoten zu besuchen.

Die Reihenfolge bei der _Breitensuche_:

```
1 12 6 7 14 22 10 4 8 2 18 3 9 13
```

Die Reihenfolge bei der _Tiefensuche_:

```
1 12 14 22 3 9 10 6 4 8 7 2 13 18
```

Unser Vorgehen beim Suchen nach einem Knoten, der den goaltest besteht (Zielknoten):
Zunächst _expandieren_ wir die Wurzel. _Expandieren_ bedeutet:
Wir schauen, ob dies der Zielknoten ist. Wenn der Knoten, den wir expandiert haben, der Zielknoten ist, sind wir fertig.
Wenn das nicht der Fall ist, fügen wir alle seine Kinder in die _frontier_ ein. Die _frontier_ sind die Knoten, die noch zur Untersuchung anstehen. Wir fügen einen Knoten nur dann in die _frontier_ ein, wenn er nicht schon früher untersucht wurde oder bereits in der _frontier_ vorhanden ist. Dazu nutzen wir das dictionary _prev_, in dem wir alle Knoten, die jemals aus der _frontier_ geholt worden sind, mit ihrem Elternknoten abspeichern. Das machen wir solange, bis die _frontier_ leer ist.
Mit den Informationen in _prev_ verfolgen wir vom Zielknoten den Pfad zurück zur Wurzel.

Bei der Breitensuche ist die _frontier_ eine _Schlange_ (_queue_), bei der Tiefensuche ein _Keller_ (_stack_).

```
from collections import deque
def bfs(startstate):
    frontier =  deque([startstate])
    prev = {startstate:None}
    while frontier:
        state = frontier.popleft()
        if goaltest(state):
            return prev, state
        for v in nextstates(state):
            if v not in prev:
                frontier.append(v)
                prev[v] = state
    return None, None

def dfs(startstate):
    frontier =  [startstate]
    prev = {startstate:None}
    while frontier:
        state = frontier.pop()
        if goaltest(state):
            return prev,state
        for v in nextstates(state):                  # nach rechts runter, für links: reversed(nextstates(state))
            if v not in prev:
                frontier.append(v)
                prev[v] = state
    return None, None

def reconstructPath(prev,goalstate):
    state = goalstate
    path = []
    while state is not None:
        path.append(state)
        state = prev[state]
    path.reverse()
    return path
```

Für ein konkretes Suchprobem sind folgende Punkte zu bearbeiten:

1. Wie sieht ein state aus?
2. Wie sieht der startstate aus?
3. Implementierung der Funktion _goaltest_
4. Implementierung der Funktion _nextstates_

Da wir _state_ als Schlüssel im dict _prev_ verwenden, nehmen wir als Datenstruktur für
das _state_ meist ein Tuple. Das Tuple muss die benötigten Informationen liefern, um die _nextstates_ zu berechnen.

### Beispiel 1

Unser Zahlenbaum. Wir suchen eine Pfad zur Zahl 18.

Ein state ist eine Zahl, startstate = 1

```
def nextstates(state):
    if state in baum:
        return baum[state]
    else: return []

def goaltest(state):
    return state == 13


baum = {1:[12,6,7], 12: [14,22,10], 6: [4,8], 7: [2,18], 22:[3,9], 2:[13]}
startstate = 1
prev, goalstate = dfs(startstate)
print(reconstructPath(prev,goalstate))

Ausgabe:
[1, 7, 2, 13]

```

### Beispiel 2

8-Puzzle. Ein state ist ein tuple, das den Zustand des 8-Puzzles zeilenweise
abbildet. Für die Leerstelle schreiben wir 0. Im _tauschdict_ ordnen wir jeder
Position ihre möglichen Tauschpositionen zu.

Für das Beispiel oben ergibt sich:

```
startstate =  (7,2,4,5,0,6,8,3,1)
goalstate = (0,1,2,3,4,5,6,7,8)
```

```
def swap(state,i,j):
    '''
    state: tuple
    i,j: gueltige Indizes für das tuple
    returns: tuple mit vertauschten Werten an Positionen i und j
    '''
    tmp = list(state)
    tmp[i],tmp[j] = tmp[j],tmp[i]
    return tuple(tmp)

def show(state):
    '''
    printed state als 3x3 Matrix
    '''
    for i in range(9):
        if i%3==0:
            print()
        print(state[i],end = ' ')
    print()

def nextstates(state):
    tmp = []
    i = state.index(0)
    for j in tauschDict[i]:
        tmp.append(swap(state,i,j))
    return tmp

def goaltest(state):
    return state == (0,1,2,3,4,5,6,7,8)
```

```
tauschDict = {0:[1,3],1:[2,4,0],2:[5,1],3:[4,6,0],4:[5,7,3,1],5:[8,4,2],6:[7,3],7:[8,6,4],8:[7,5]}
startstate = (7,2,4,5,0,6,8,3,1)
#startstate = (1,2,3,4,5,6,8,7,0)    # nicht lösbar
prev, goalstate = bfs(startstate)
if prev is None:
    print('nicht lösbar')
else:
    path = reconstructPath(prev,goalstate)
    print(f'Lösung in {len(path)-1} Zügen gefunden.')

Ausgabe: Lösung in 26 Zügen gefunden.
```

Um die Lösung zu sehen, geben wir die Elemente des path aus.

```
for state in path:
    show(state)


7 2 4
5 0 6
8 3 1

7 2 4
0 5 6
8 3 1

0 2 4
7 5 6
8 3 1

2 0 4
7 5 6
8 3 1

2 5 4
7 0 6
8 3 1

2 5 4
7 6 0
8 3 1

2 5 4
7 6 1
8 3 0

2 5 4
7 6 1
8 0 3

2 5 4
7 6 1
0 8 3

2 5 4
0 6 1
7 8 3

2 5 4
6 0 1
7 8 3

2 5 4
6 1 0
7 8 3

2 5 4
6 1 3
7 8 0

2 5 4
6 1 3
7 0 8

2 5 4
6 1 3
0 7 8

2 5 4
0 1 3
6 7 8

2 5 4
1 0 3
6 7 8

2 5 4
1 3 0
6 7 8

2 5 0
1 3 4
6 7 8

2 0 5
1 3 4
6 7 8

0 2 5
1 3 4
6 7 8

1 2 5
0 3 4
6 7 8

1 2 5
3 0 4
6 7 8

1 2 5
3 4 0
6 7 8

1 2 0
3 4 5
6 7 8

1 0 2
3 4 5
6 7 8

0 1 2
3 4 5
6 7 8
```
