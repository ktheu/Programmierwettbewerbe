### Backtracking


Backtracking ist ein systematisches Ausprobieren. Wenn wir in eine Sackgasse geraten sind, gehen wir zurück (backtrack) und probieren die nächste Variante aus. Meistens sind alle möglichen Lösungen gefragt.

Backtracking ist anwendbar, wenn wir eine Lösung schrittweise aufbauen können und wenn wir für eine
Teillösung die möglichen Kandidaten aufzählen können, die die Teillösung erweitern. 

Eine Teillösung bezeichnen wir mit $x$. $x$ ist eine Liste mit Entscheidungen $x[0]...x[k]$, die zur Lösung führen sollen.

Im Gegensatz zur rekursiven Tiefensuche wird beim backtracking derselbe Pfad immer wieder verändert. Erst wenn eine Lösung gefunden wird, wird eine Kopie gesichert.

```
def back(x):
    if isSolution(x):
        solutions.append(x.copy())
    else:
        for cand in candidates(x):
            if isGood(cand,x):
                x.append(cand)
                back(x)
                x.pop()
                
def isSolution(x):
    '''
    returns: True, wenn der Lösungsvektor x eine Lösung darstellt
    '''
    pass

def candidates(x):
    '''
    returns: Liste von Entscheidungen, die den Lösungsvektor x um eine Stufe erweitern
    '''
    pass

def isGood(cand, x):
    '''
    returns: True, wenn die Entscheidung cand den Lösungsvektor x sinnvoll erweitert.
    '''
               
solutions = []
back([])
```