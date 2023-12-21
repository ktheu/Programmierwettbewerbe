### Algorithmen

#### Breitensuche


```
Füge den Startknoten in eine queue ein und markiere ihn als besucht,
alle anderen als nicht besucht.
Solange die queue nicht leer:
    hole den ersten Knoten u aus der queue
    Für jeden Nachbarn v von u:
        Falls v noch nicht besucht:
            Markiere v als besucht.
            Füge ihn in die queue ein
            ggf: Merke u als Vorgänger von v
```

#### Tiefensuche (iterativ)

Wie Breitensuche, nur stack statt queue.


#### Tiefensuche (rekursiv)

```
Markiere alle Knoten als nicht besucht
def dfs(u):
    markiere u als besucht
    für alle Nachbarn v von u:
        falls v noch nicht besucht:
            dfs(v)
```       







        