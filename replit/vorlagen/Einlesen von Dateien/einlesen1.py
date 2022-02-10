'''
Die erste Zahl ist die Anzahl der folgenden Datensätze.
Jede Zeile des Datensatzes besteht aus einer Zahl.

4
10
20
30
40
'''

f = open('daten1.txt')
anzahl = int(f.readline())

zahlen = []
for i in range(anzahl):
    zahlen.append(int(f.readline()))

f.close()

print(zahlen)