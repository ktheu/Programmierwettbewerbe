<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
## Erreichbarkeit, Zusammenhangskomponenten, Topologische Sortierung


#### Erreichbarkeit

Erreichbarkeit wird mittels Tiefensuche festgestellt in $O(|V|)+O(|E|)$.

``` 
visited =  {v : False for v in G}       
def explore(v):  
    visited[v] = True
    for w in G[v]:
        if not visited[w]:
            explore(w) 
            
explore(start)
result = [v for v in G if visited[v]]            
```

### Zusammenhangskomponenten in einem ungerichteten Graphen


``` 
def explore(v):
    visited[v] = True
    ccnum[v] = cc
    for w in G[v]:
        if not visited[w]:
            explore(w)

visited = {v : False for v in G}
ccnum = {v : 0 for v in G}     # connected component nr von v
cc = 1                         # aktuelle connected component nr
for v in G:
    if not visited[v] :
        explore(v)
        cc+=1

for i in range(1,cc):
    result = [v for v in G if visited[v] and ccnum[v] == i]
    print(i,'-',*result)
```

### Starke Zusammenhangskomponenten 

In einem gerichteten Graphen heißen zwei Knoten u und v (stark) zusammenhängend, wenn u von v und v von u erreichbar ist.

[Video](https://www.youtube.com/watch?v=qm82ypRnOjI&list=PLWeMgMhRDsIHVtFQLF07HdrmbLI7dARgs&index=5)

``` 
G = {
'a': set('b'),
'b': set('ef'),
'c': set('b'),
'd': set('ag'),
'e': set('ach'),
'f': set(),
'g': set('h'),
'h': set('i'),
'i': set('fh')
}

# explore reverse Graph, merke postvisit nr
def exploreR(v):
    global counter
    visited[v] = True
    for w in Gr[v]:
        if not visited[w]:
            exploreR(w)
    postvisit[v] = counter
    counter+=1

# explore Graph, merke connected component number
def explore(v):
    visited[v] = True
    ccnum[v] = cc
    for w in G[v]:
        if not visited[w]:
            explore(w)

# Gr ist der reverse Graph von G
Gr = {v:set() for v in G}
for v in G:
    for w in G[v]:
        Gr[w].add(v)

# dfs durch den reversen Graphen, merke postvisit-nr
visited = {v : False for v in Gr}
postvisit = {v : 0 for v in Gr}
counter = 1
for v in Gr:
    if not visited[v] :
        exploreR(v)

# die Knoten in der umgekehrten postvisit-Reihenfolge des reversen Graphen
vlist = sorted(Gr,key=lambda v: postvisit[v],reverse=True)

# dfs durch den Ausgangsgraphen, in der vlist Reihenfolge, dabei component nr merken
visited = {v : False for v in G}
ccnum = {v : 0 for v in G}
cc = 1
for v in vlist:
    if not visited[v] :
        explore(v)
        cc+=1

# Ausgabe
for i in range(1,cc):
    result = [v for v in G if ccnum[v] == i]
    print(i,'-',*result)

```