## Graphen - Modellierung

### Adjazenzmatrix

Ungewichtete Graphen: 0 = es exisitiert keine Kante

```Python
G = [[0, 1, 1, 0],  
     [0, 0, 0, 1],  
     [0, 1, 0, 1],  
     [0, 1, 0, 0]]

G[0][1] == 1                                    # True, wenn es Kante von 0 nach 1 gibt
[j for j in range(len(G)) if G[0][j] == 1]      # alle Nachbarn von 0
``` 

Gewichtete Graphen: inf = es exisitiert keine Kante

```Python
inf = float('inf') 
G = [[0,   8,   2, inf],  
     [inf, 0, inf,   4],  
     [inf, 1,   0,   6],  
     [inf, 2, inf,   0]]

G[0][1]                                                 # die Kosten der Kante von 0 nach 1
[j for j in range(len(G)) if j!=0 and G[0][j] < inf]    # alle Nachbarn von 0

```

### Adjazenz"listen"

Ungewichtete Graphen

```Python
G = {'a':set('bc'),
     'b':set('d'), 
     'c':set('bd'),
     'd':set('b')}

'b' in G['a']        # True, wenn es Kante von a nach b gibt   
G['a']               # alle Nachbarn von 'a'
``` 

Gewichtete Graphen

```Python
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