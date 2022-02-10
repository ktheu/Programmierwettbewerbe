'''
In der ersten Zeile stehen die Anzahl Zeilen und die Anzahl Spalten
der folgenden Matrix aus Zahlen.

3 5
1 0 1 3 1
0 0 1 1 2
2 1 1 2 1
'''

f = open('./daten4.txt')
rows, cols = [int(x) for x in f.readline().split()]

matrix = []
for i in range(rows):
    matrix.append([int(x) for x in f.readline().split()])
f.close()

print("Anzahl Zeilen:", rows)
print("Anzahl Spalten", cols)
print(matrix)

# print("Zeile 1, Spalte 4: ",grid[0][3])

# print("Die Elemente der 1. Zeile:")
# for x in grid[0]:
#     print(x, end=' ')
# print()

# print("Die Elemente der 4. Spalte:")
# for k in range(len(grid)):
#     print(grid[k][3])
# print()