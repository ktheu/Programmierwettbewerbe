### Breitensuche 

Wir beginnen mit einem startstate. Mögliche Folgeaktionen führen uns zu den nextstates. Die Knoten in unserem Suchbaum sind nicht die Aktionen, sondern die aus den Aktionen resultierenden Zustände. Unterschiedliche Aktionsfolgen können dieselben Zustände erzeugen. Dieselben Zustände wollen wir nicht nicht mehrfach untersuchen.

Die states modellieren wir als Tuple, weil wir sie als keys in dem dictionary prev verwenden wollen. Das dictionary prev speichert für ein Tuple den Vorgänger. Es dient zwei Zwecken: 1. Wir können feststellen, ob wir ein state im Laufe der Suche schon einmal gesehen haben. 2. Wir können die Abfolge der Aktionen rekonstruieren, die uns vom Start zum Ziel führen.

```Python
from collections import deque
def bfs(s):
    frontier =  deque([s])
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

def reconstructPath(prev,goalstate):
    state = goalstate
    path = []
    while state is not None:
        path.append(state)
        state = prev[state]
    path.reverse()
    return path


# Aufruf:
startstate = ....
prev, goalstate = bfs(startstate)
path = reconstructPath(prev, goalstate)

```


### Tiefensuche

Der Code für die iterative Tiefensuche gleicht dem der Breitensuche, nur verwenden wir als frontier einen Stack statt einer Schlange. 

```Python
def dfs(s):
    frontier =  [s]
    prev = {s:None}
    while frontier:
        state = frontier.pop()  
        if goaltest(state):
            return prev, state
        for v in nextstates(state):
            if v not in prev:
                frontier.append(v)
                prev[v] = state
    return None, None
```

Wenn uns der Weg zum Ziel nicht interessiert, können wir statt dem dict prev auch ein set visited nehmen

```Python
def dfs(s):
    frontier =  [s]
    visited = set()
    while frontier:
        state = frontier.pop()  
        if goaltest(state):
            return state
        visited.add(state)
        for v in nextstates(state):
            if v not in visited:
                frontier.append(v)
    return visited
```

Die rekursive Variante (am Beispiel eines Graphen).

```Python
def dfs(v):  
    visited.add(v)
    for w in G[v]:
        if w not in visited:
            dfs(w) 

G = {'a':set('bc'), 'b':set('d'), 'c':set('bd'), 'd':set('b')}
visited =  set()
dfs('c')
print(visited)

```
