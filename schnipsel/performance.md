## Performance 

Python: Wenn bei Aufgaben das Zeitlimit nicht reicht, können folgende Änderungen
versucht werden:

```
stdin.readline()   statt input()
stdout.write()     statt print()
```

```
if not condition: continue       statt
if condition:
     weiter()
```

Keine Variablen wegen scheinbarer Doppelberechnung anlegen:

```
if a + b > t:
    t = a + b      statt

c = a + b
if c > t:
    t = c
```

Versuche Matrizen eindimensional zu modellieren:

```
D = [inf]* 250000  statt  D = [[inf] * 500 for _ in range(500)]
D[a + 500*b]       statt  D[a][b] 
```

Nutze join statt String-Concatenation
```
output = " ".join(["Programming" , "is", "fun"])  statt
output = "Programming " + "is " + "fun"
```


Nutze Mehrfachzuweisungen
```
a, b = 3, 5
statt 
a = 3
b = 5
```

Vermeide Funktionsaufrufe mit Parameterübergabe - lieber den Code wiederholen.

Das Hauptprogramm in eine Funktion verpacken.



 


