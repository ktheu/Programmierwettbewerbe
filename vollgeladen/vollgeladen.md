<img src=a2.png>

[Lösungshinweise](vollgeladen.pdf)

#### Beispieldaten (1-5)

Jede Datei beschreibt eine Route und enthält

  * in der ersten Zeile die Anzahl der Hotels n,
  * in der zweiten Zeile Gesamtfahrzeit t in Minuten
  * in den weiteren n Zeilen jeweils für jedes Hotel:
    * die Entfernung t_i des Hotels vom Start, sowie
    * die Bewertung b_i des Hotels.
    
Die maximale Tagesreise beträgt 6*60 = 360 Minuten


```python
nr = 1
f = open('./beispieldaten/hotels'+str(nr)+'.txt')
print(f.read())
```

    12
    1680
    12 4.3
    326 4.8
    347 2.7
    359 2.6
    553 3.6
    590 0.8
    687 4.4
    1007 2.8
    1008 2.6
    1321 2.1
    1360 2.8
    1411 3.3
    
    

Die Reise darf 5 Tage dauern. Die Ankunft ist kein Hotel, sondern die Verwandten in Portugal. Also darf man höchstens 4 Hotels für die Übernachtung aussuchen. Wir müssen uns also (maximal) 4 mal für ein Hotel entscheiden. In der Menge der Entscheidungsmöglichkeiten suchen wir eine optimale Lösung: die niedrigste Bewertung eines Hotels soll so hoch wie möglich sein.

Als *state* wählen wir das Tupel der bisherigen Entscheidungen. 

```
state = (326, 687)      # Der state mit 2 Hotelübernachtungen
```


```python
startstate = ()               # leeres Tupel
```

Wir müssen die beiden Funktionen *goaltest* und *nextstates* implementieren. Für den Zielwert erlauben wir uns eine globale Variable.
Die Hotels modellieren wir als dictionary.


```python
nr = 1
f = open('./beispieldaten/hotels'+str(nr)+'.txt')
anz = int(f.readline())
ziel = int(f.readline())
hotels = {}
for i in range(anz):
    t, b =  f.readline().split()
    t = int(t)
    b = float(b)
    if t in hotels and b > hotels[t]:
        hotels[t]=b
    if t not in hotels:
        hotels[t]=b
print(hotels)
print(ziel)
    
 
```

    {12: 4.3, 326: 4.8, 347: 2.7, 359: 2.6, 553: 3.6, 590: 0.8, 687: 4.4, 1007: 2.8, 1008: 2.6, 1321: 2.1, 1360: 2.8, 1411: 3.3}
    1680
    


```python
def goaltest(state):
    if ziel <= 360:
        return True
    if len(state) == 0: return False
    return ziel - state[-1] <= 360
```


```python
def nextstates(state):
    tmp = []
    if len(state) == 4: return tmp
    pos = state[-1] if len(state) > 0 else 0
    for h in hotels:
        if h - pos <= 360:
            tmp.append(state + (h,))
    return tmp        
    
```

Da wir uns den ganzen Pfad merken, benötigen wir das dict *prev* nicht. 


```python
from collections import deque

def bfs(startstate):
    frontier =  deque([startstate])
    while frontier:
        state = frontier.popleft()
        if goaltest(state):
            solutions.append(state)
        for v in nextstates(state):
            frontier.append(v)

```


```python
%%time 
startstate = ()
solutions = []
bfs(startstate)

```

    CPU times: total: 0 ns
    Wall time: 1 ms
    


```python
best = None
best_val = 0
for sol in solutions:
    val = min([hotels[t] for t in sol])
    if val > best_val:
        best_val = val
        best = sol

print(f'Beste Etappe: {best} mit Bewertung {best_val}')

```

    Beste Etappe: (347, 687, 1007, 1360) mit Bewertung 2.7
    

#### Es dauert zu lang

Bei Beispiel 3 merken wir, das unser Search-Space zu groß ist. Wir verbessern unsere *nextstates*-Funktion. Es kommen als Folgehotels nur solche in Frage, mit denen sich die Tour mit maximal 4 Übernachtungen schaffen lässt. 

#### Das vollständige Programm

In der Variablen *zaehl* protokollieren wir, wieviele *states* wir aus der frontier geholt haben.


```python
%%time
from collections import deque

def goaltest(state):
    if ziel <= 360:
        return True
    if len(state) == 0: return False
    return ziel - state[-1] <= 360

def nextstates(state):
    n = len(state)
    if n == 4: return []
    tmp = []
    pos = state[-1] if len(state) > 0 else 0
    for h in hotels:
        if h - pos <= 360 and ziel-h <= (4-n)*360:
            tmp.append(state + (h,))
    return tmp   

def bfs(startstate):
    frontier =  deque([startstate])
    while frontier:
        state = frontier.popleft()
        if goaltest(state):
            solutions.append(state)
        for v in nextstates(state):
            frontier.append(v)


nr = 5
f = open('./beispieldaten/hotels'+str(nr)+'.txt')
anz = int(f.readline())
ziel = int(f.readline())
hotels = {}
for i in range(anz):
    t, b =  f.readline().split()
    t = int(t)
    b = float(b)
    if t in hotels and b > hotels[t]:
        hotels[t]=b
    if t not in hotels:
        hotels[t]=b
 
startstate = ()
solutions = []
bfs(startstate)

best = None
best_val = 0
for sol in solutions:
    val = min([hotels[t] for t in sol])
    if val > best_val:
        best_val = val
        best = sol

print(f'Beste Etappe: {best} mit Bewertung {best_val}')

```

    Beste Etappe: (280, 636, 987, 1271) mit Bewertung 5.0
    CPU times: total: 31.1 s
    Wall time: 31.1 s
    

### Ein anderer Ansatz
Es kann möglich sein, auf verschiedenen Pfaden zu einem Hotel h zu kommen und trotzdem dieselbe Bewertung für die Pfade zu erhalten.
Wir benötigen für unsere Aufgabe aber jeweils nur einen Pfad. Deswegen ändern wir die Modellierung unseres *state* ab. Dadurch wird sich die Größe unseres Search-Space weiter reduzieren.

```
Anzahl frontier-Entnahmen bei Beispiel 5:
Variante 1:  6302797
Variante 2:     6990
```


State ist eine Minutenangabe zusammen mit den noch verfügbaren Tagen und der bisherigen Bewertung (Minimum der bisherigen Unterkünfte)



```python
startstate = (0,5,10)  # Start an Position 0, noch 5 Tage zur Verfügung, = 10 bisherige minimale Bewertung (damit entscheidet 0 nichts)

def goaltest(state):
    zeit, tag, _ = state   # tag = noch verfügbare Tage
    return (ziel-zeit) <= 360 and tag >= 1 

def nextstates(state):
    tmp = []
    zeit, tag, b =  state
    
    for h in hotels:
        if 0 < h-zeit <= 360 and ziel-h<= 360 * (tag-1):
            tmp.append((h,tag-1,min(b,hotels[h])))
    return tmp
```


```python
from collections import deque

def bfs(startstate):
    frontier =  deque([startstate])
    prev = {startstate:None}
    while frontier:
        state = frontier.popleft()
        if goaltest(state):
            solutions.append(state)
        for v in nextstates(state):
            if v not in prev:
                frontier.append(v)
                prev[v] = state
    return prev

def reconstructPath(prev,goalstate):
    state = goalstate
    path=[]
    while state is not None:
        path.append(state)
        state = prev[state]
    path.reverse()
    return path
```


```python
nr = 5
f = open('./beispieldaten/hotels'+str(nr)+'.txt')
anz = int(f.readline())
ziel = int(f.readline())
hotels = {}
for i in range(anz):
    t, b =  f.readline().split()
    t = int(t)
    b = float(b)
    if t in hotels and b > hotels[t]:
        hotels[t]=b
    if t not in hotels:
        hotels[t]=b

solutions = []
prev = bfs(startstate)

```


```python
best = None
best_val = 0

for sol in solutions:
    path = reconstructPath(prev,sol)
    val = min([hotels[tup[0]] for tup in path[1:]])
    if val > best_val:
        best_val = val
        best = path.copy()
print(best_val, best)
```

    5.0 [(0, 5, 10), (280, 4, 5.0), (636, 3, 5.0), (987, 2, 5.0), (1271, 1, 5.0)]
    

#### Das vollständige Programm - Version 2



```python
%%time
from collections import deque

def goaltest(state):
    zeit, tag, _ = state   # tag = noch verfügbare Tage
    return (ziel-zeit) <= 360 and tag >= 1 

def nextstates(state):
    tmp = []
    zeit, tag, b =  state
    
    for h in hotels:
        if 0 < h-zeit <= 360 and ziel-h<= 360 * (tag-1):
            tmp.append((h,tag-1,min(b,hotels[h])))
    return tmp

def bfs(startstate):
    frontier =  deque([startstate])
    prev = {startstate:None}
    while frontier:
        state = frontier.popleft()
        if goaltest(state):
            solutions.append(state)
        for v in nextstates(state):
            if v not in prev:
                frontier.append(v)
                prev[v] = state
    return prev

def reconstructPath(prev,goalstate):
    state = goalstate
    path=[]
    while state is not None:
        path.append(state)
        state = prev[state]
    path.reverse()
    return path

nr = 5
f = open('./beispieldaten/hotels'+str(nr)+'.txt')
anz = int(f.readline())
ziel = int(f.readline())
hotels = {}
for i in range(anz):
    t, b =  f.readline().split()
    t = int(t)
    b = float(b)
    if t in hotels and b > hotels[t]:
        hotels[t]=b
    if t not in hotels:
        hotels[t]=b
 
solutions = []
startstate = (0,5,10) 

prev = bfs(startstate)

best = None
best_val = 0


for sol in solutions:
    path = reconstructPath(prev,sol)
    val = min([hotels[tup[0]] for tup in path[1:]])
    if val > best_val:
        best_val = val
        best = path.copy()

print(f'Hotels für Beispiel {nr}:')
for x in best[1:]:
    print(f'{x[0]} - {hotels[x[0]]},',end=' ')
print('minimale Bewertung:', best_val)
 
```

    Hotels für Beispiel 5:
    280 - 5.0, 636 - 5.0, 987 - 5.0, 1271 - 5.0, minimale Bewertung: 5.0
    CPU times: total: 562 ms
    Wall time: 570 ms
    
