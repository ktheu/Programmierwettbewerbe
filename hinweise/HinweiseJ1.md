### Hinweise J1

Einlesen der Daten:


```python
f = open('wundertuete0.txt')
anzahl_tueten = int(f.readline())
anzahl_sorten = int(f.readline())
spiele = []
for _ in range(anzahl_sorten):
    spiele.append(int(f.readline()))

f.close()
print(f'Anzahl Wundertüten: {anzahl_tueten}')
print(f'Anzahl Spielesorten: {anzahl_sorten}')
print(f'Spiele: {spiele}')
```

    Anzahl Wundertüten: 3
    Anzahl Spielesorten: 3
    Spiele: [4, 4, 2]
    

Wir modellieren die Wundertüten als Liste. Beispiel:

```[1,3,2]``` bedeutet: In der Wundertüte sind: 1 Spiel der 1.Sorte, 3 Spiele der 2.Sorte und 2 Spiele der 3.Sorte

Zu Beginn verschaffen wir uns leere Wundertüten:


```python
tueten = [[0]*anzahl_sorten for _ in range(anzahl_tueten)]
print(tueten)
```

    [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    

------

Nützliches:


```python
30 // 7      # ganzzahlige Division
```




    4




```python
30 % 7       # der Rest der Division
```




    2


