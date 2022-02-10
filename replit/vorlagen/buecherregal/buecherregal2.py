'''
Einlesen der Daten und sortieren der Bücher-Daten

'''
f = open('daten.txt')
anz_figuren = int(f.readline())
anz_buecher = int(f.readline())
buecher = []
for i in range(anz_buecher):
    buecher.append(int(f.readline()))

print('anz_figuren:', anz_figuren)
print('anz_buecher:',anz_buecher)
buecher.sort()

'''
abschnitt jeweils eine Liste von Büchern die zwischen zwei Figuren
stehen, deren Höhenunterschied also <= 3 ist.

regal = eine Liste der abschnitte

'''
regal = []
abschnitt = []                        
abschnitt_starthoehe = buecher[0]

for b in buecher:
    if b - abschnitt_starthoehe <= 3:
        abschnitt.append(b)
    else:
        regal.append(abschnitt)
        abschnitt = [b]
        abschnitt_starthoehe = b
        
regal.append(abschnitt)
print(regal)


 