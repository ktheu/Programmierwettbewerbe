### Kürzeste Wege: Floyd-Warshall und Dijkstra

#### Floyd-Warshall

Der Algorithmus von Floyd-Warshall berechnet die kürzestesten Wege zwischen allen
Knoten in einem Graphen (all-pairs-shortest-path) in $O(n^3)$.



```
def floyd(c):
    ''' 
    c: Kostenmatrix = Graph als Adjazenzmatrix
    returns: d, p - Distanzmatrix und Wegematrix mit dem Vorgänger des kürzesten Wegs 
    '''
    n = len(c)
    d = [[0]*n for j in range(n)]   # Distanzmatrix
    p = [[0]*n for j in range(n)]   # Wegematrix mit den Vorgängern (prevs)
    for i in range(n):
        for j in range(n):
            d[i][j] = c[i][j]
            p[i][j] = i

    for k in range(n):
        for i in range(n):
            for j in range(n):
                tmp = d[i][k] + d[k][j]
                if tmp < d[i][j]:
                    d[i][j] = tmp
                    p[i][j] = p[k][j]
    return d, p

def getPath(p, i, j):
    if i == j: return str(i)
    return getPath(p,i,p[i][j]) + ' - ' + str(j)


inf = float('inf')
G = [[0,   8,   2, inf],
     [inf, 0, inf,   4],
     [inf, 1,   0,   6],
     [inf, 2, inf,   0]]

d, p = floyd(G)

print(getPath(p,0,3))            # kürzester Weg von Knoten 0 nach Knoten 3
print("Kosten =",d[0][3])        # Kosten dieses Weges
```

 
#### Dijkstra

Der Algorithmus von Dijkstra berechnet die kürzeste Entfernung eines Knotens zu allen 
anderen Knoten in einem Graphen mit nicht-negativen Kantenkosten (single-source-shortest-path)
in $O((|V|+|E|)⋅log|V|)$.
 

``` 
G = {
'a': {'b':2, 'c':9},
'b': {'c':5, 'd':13},
'c': {'d':6, 'e':9},
'd': {'e':1, 'f':5},
'e': {'f':2},
'f': {}
}

from heapq import heapify, heappop, heappush

def reconstructPath(s,u,prev):
    temp = []
    while u != s:
        temp.append(u)
        u = prev[u]
    temp.append(s)
    temp.reverse()
    return temp

inf = float('inf')
dist = {v:inf for v in G}
prev = {v:None for v in G}

s = 'a'         # startknoten
dist[s] = 0
endgueltig = set()    

vorlaeufig = [(dist[v],v) for v in G]
heapify(vorlaeufig)

while vorlaeufig:
    _, u = heappop(vorlaeufig)
    if u in endgueltig: continue
    endgueltig.add(u)
    for v in G[u]:
        if dist[v] > dist[u] + G[u][v]:
            dist[v] = dist[u] + G[u][v]
            prev[v] = u
            heappush(vorlaeufig,(dist[v],v))
ziel = 'f'
print('Pfad von',s,'nach',ziel,':',*reconstructPath('a','f',prev))
print('Distanz:',dist[ziel])
```


#### Bellman-Ford

Der Algorithmus von Bellman-Ford berechnet die kürzeste Entfernung eines Knotens zu allen 
anderen Knoten in einem Graphen auch bei negativen Kantenkosten falls es
keine negativen Zyklen gibt (single-source-shortest-path) 
in $O(|V| \cdot |E|)$.

``` 
G = {
'a': {'b':6,'e':7},
'b': {'d':-4,'e':8,'c':5},
'c': {'b':-2},
'd': {'c':7},
'e': {'c':-3,'d':9}
}

def reconstructPath(s,u,prev):
    temp = []
    while u != s:
        temp.append(u)
        u = prev[u]
    temp.append(s)
    temp.reverse()
    return temp

inf = float('inf')
dist = {v:inf for v in G}
prev = {v:None for v in G}

start, ziel = 'a' , 'b'
dist[start] = 0

changed = True
while changed:
    changed = False
    for u in G:
        for v in G[u]:
            if dist[v] > dist[u] + G[u][v]:
                dist[v] = dist[u] + G[u][v]
                prev[v] = u
                changed = True

print('Pfad von',start,'nach',ziel,':',*reconstructPath(start,ziel,prev))
print('Distanz:',dist[ziel])

```