'''
Die erste Zeile ist die Anzahl der folgenden Datensätze.
Jeder folgende Datensatz ist eine Koordinate bestehend aus 2 Zahlen.

4
4 5
3 8
1 2
3 -2
'''

f = open('daten3.txt')
anzahl = int(f.readline())
daten = []

for i in range(anzahl):
    daten.append([int(x) for x in f.readline().split()])
f.close()

print("Anzahl Koordinaten:", anzahl)
print(daten)