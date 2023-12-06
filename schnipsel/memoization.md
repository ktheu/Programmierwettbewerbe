### Memoization

Memoization verhindert, dass wir bei rekursiven Aufrufen Dinge mehrfach berechnen.
Das Beispiel zeigt die rekursive Berechnung der Fibonacci-Zahlen. 


``` 
def fib(n):
    if n in memo: return memo[n]   
    if n <= 2: 
        result = 1
    else:
        result = fib(n-2) + fib(n-1)
    memo[n] = result
    return result

memo = {}
fib(120)
```

Statt memo als globale Variable zu definieren, können wir es beim ersten Aufruf erzeugen und dann
an die weiteren Aufrufe mitgeben. 

```
def fib(n, memo={}):
    if n in memo: return memo[n]   
    if n <= 2: 
        result = 1
    else:
        result = fib(n-2, memo) + fib(n-1, memo)
    memo[n] = result
    return result
 
fib(120)
```