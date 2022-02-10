'''
Lies die Datei daten.txt ein.
Speichere die Werte in der ersten Zeile in den Variablen anz_haus und anz_mast.
Speichere die Koordinaten der Häuser in eine Liste haeuser, die Koordinaten der Masten in einer Liste masten.
'''
# hier dein code
f = open('daten.txt')
anz_haus, anz_mast = [int(x) for x in f.readline().split()]
    
haeuser = []
masten = []

for i in range(anz_haus):
    haeuser.append([int(x) for x in f.readline().split()])

for i in range(anz_mast):
    masten.append([int(x) for x in f.readline().split()])

# Kontrolle
print("Anzahl Häuser: ",anz_haus)      
print("Anzahl Masten: ",anz_mast)   
print(haeuser)
print(masten)

'''
Erwartete Ausgabe:
Anzahl Häuser:  3
Anzahl Masten:  2
[[0, 0], [0, 1], [1, 1]]
[[1, 2], [-1, 2]]

'''