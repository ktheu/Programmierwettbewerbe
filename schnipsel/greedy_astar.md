## Best-first Search (Greedy) und A*

#### Best first search

Best-first search ist ein allgemeiner Begriff für eine Suche, bei dem der state als nächstes aus der frontier geholt wird, der laut einer Evaluations-Funktion den besten (=niedrigsten) Wert hat.

#### Greedy

Greedy ist eine Form des best-first search. Der state ist am besten, der die größte Ähnlichkeit (oder den kleinsten Abstand) zum goalstate hat.

``` 
def h(state):
    '''
    returns: Vorwärtskosten laut Heuristik
    '''
    return pass


from heapq import heappop, heappush
def greedy(s):
    frontier =[(h(s),s)]  
    prev = {s:None}
    while frontier:
        _ ,state = heappop(frontier)  
        if goaltest(state):
            return prev, state
        for v in nextstates(state):
            if v not in prev:
                heappush(frontier,(h(v),v))
                prev[v] = state
    return None, None
```

#### A*  

Der A*-Algorithmus berücksichtigt sowohl die vermuteten Vorwärtskosten laut Heuristik, als auch die bisher tatsächlich angefallenen (Rückwärts)-Kosten. 

Eine Heuristik heißt zulässig, wenn sie die tatsächlich anfallenden Kosten nicht überschätzt. Mit einer zulässigen Heuristik findet A* die optimale Lösung.

``` 
def h(state):
    '''
    returns: Vorwärtskosten laut Heuristik
    '''
    return pass


from heapq import heappop, heappush
def astar(s):
    frontier =[(h(s),s)]  
    prev = {s:None}
    g = {s:0}           # Rückwärtskosten
    while frontier:
        _ ,state = heappop(frontier)   
        if goaltest(state):
            return prev, state
        for v in nextstates(state):
            gg = g[state] + 1                # hier werden pro "Zug" die Rückwärtskosten um 1 erhöht
            if v not in prev or gg < g[v]:   # wenn v noch nicht gesehen oder 
                g[v] = gg                    # die Rückwärtskosten geringer als bisher
                heappush(frontier,(g[v]+h(v),v))
                prev[v] = state
    return None, None
```
