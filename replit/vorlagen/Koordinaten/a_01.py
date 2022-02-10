'''
Lies die Daten aus daten.txt in eine Liste *punkte*
von Koordinaten [x,y] ein.
Die erste Zahl ist die Anzahl der folgenden Koordinaten.

'''
f = open('daten.txt')
anzahl = int(f.readline())
punkte = []
for i in range(anzahl):
    pos = [int(x) for x in f.readline().split()]
    punkte.append(pos)

# Kontrolle 
print(punkte)

'''
Erwartete Ausgabe:
[[2, 0], [1, 1], [2, 1], [3, 3]]
'''