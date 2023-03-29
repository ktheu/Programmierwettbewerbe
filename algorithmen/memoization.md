### Memoization

Memoization verhindert, dass wir bei rekursiven Aufrufen Dinge mehrfach berechnen.
Das Beispiel zeigt die rekursive Berechnung der Fibonacci-Zahlen. 

```Python
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
