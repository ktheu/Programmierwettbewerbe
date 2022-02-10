'''
Lies die Daten ein. Die erste Zeile geben an, wieviele Zeilen und
Spalten die folgende Matrix hat.
Speichere die Anzahl Zeilen in der Variablen rows.
Speichere die Anzahl Spalten in der Variablen cols.
Speichere die Matrix als Liste von Listen in der der Variablen grid.

'''


f = open('./daten.txt')
rows, cols = [int(x) for x in f.readline().split()]

grid = []
for i in range(rows):
    grid.append([int(x) for x in f.readline().split()])
f.close()


# Kontrolle

print("Anzahl Zeilen:", rows)
print("Anzahl Spalten", cols)
print(grid)
print(type(grid[0][0]))        # Elemente sollen vom Typ int sein


# Erwartete Ausgaben
'''
Anzahl Zeilen: 4
Anzahl Spalten 5
[[0, 0, 0, 0, 0], [1, 0, 0, 1, 1], [2, 2, 2, 1, 2], [2, 1, 1, 1, 2]]
<class 'int'>

'''



