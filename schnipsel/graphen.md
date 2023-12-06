## Graphen - Modellierung

#### Adjazenzmatrix

Ungewichtete Graphen: 0 = es exisitiert keine Kante

``` 
G = [[0, 1, 1, 0],  
     [0, 0, 0, 1],  
     [0, 1, 0, 1],  
     [0, 1, 0, 0]]

G[0][1] == 1                                    # True, wenn es Kante von 0 nach 1 gibt
[j for j in range(len(G)) if G[0][j] == 1]      # alle Nachbarn von 0
``` 

Gewichtete Graphen: inf = es exisitiert keine Kante

``` 
inf = float('inf') 
G = [[0,   8,   2, inf],  
     [inf, 0, inf,   4],  
     [inf, 1,   0,   6],  
     [inf, 2, inf,   0]]

G[0][1]                                                 # die Kosten der Kante von 0 nach 1
[j for j in range(len(G)) if j!=0 and G[0][j] < inf]    # alle Nachbarn von 0

```

#### Adjazenz'listen' - Implementation mit sets und dicts


Ungewichtete Graphen

``` 
G = {'a':set('bc'),
     'b':set('d'), 
     'c':set('bd'),
     'd':set('b')}

'b' in G['a']        # True, wenn es Kante von a nach b gibt   
G['a']               # alle Nachbarn von 'a'
``` 

Gewichtete Graphen

``` 
G = {
'a': {'b':2, 'c':9},
'b': {'c':5, 'd':13},
'c': {'d':6, 'e':9},
'd': {'e':1, 'f':5},
'e': {'f':2},
'f': {}
}

'b' in G['a']        # True, wenn es Kante von a nach b gibt   
G['a']['b']          # Die Kosten der Kante von a nach b
[v for v in G['a']]  # alle Nachbarn von 'a'
``` 

#### Adjazenzlisten - Implementation mit Listen

Wenn die Frage, ob zwei Knoten benachbart sind, nicht so häufig vorkommt, ist 
die Implementation mit Listen in der Regel schneller.


Ungerichteter, ungewichteter Graph

```
n, m = map(int, stdin.readline().split())   # n Knoten, m Kanten
adj = [[] for _ in range(n+1)]              # Knoten starten bei 1

for _ in range(m):                         
    u, v = map(int, stdin.readline().split())   # Kante zwischen u und v
    adj[u].append(v) 
    adj[v].append(u)

for v in adj[u]:   # alle Nachbarn von u
    pass
```



Gerichteter, gewichteter Graph

```
n, m = map(int, stdin.readline().split())   # n Knoten, m Kanten   
adj = [[] for i in range(n+1)]              # Knoten starten bei 1        

for i in range(m):                   # Kante von u nach v mit Kosten c               
    u, v, c = map(int, stdin.readline().split())    
    adj[u].append((v,c))

for v,c in adj[u]:         # alle Nachbarn von u mit ihren Kosten
     pass

``` 
