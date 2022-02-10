'''
Einlesen der Daten und sortieren der Bücher-Liste
'''
f = open('./beispieldaten/buecherregal6.txt')
#f = open('./beispieldaten/daten.txt')
anz_figuren = int(f.readline())
anz_buecher = int(f.readline())
buecher = []
for i in range(anz_buecher):
    buecher.append(int(f.readline()))
f.close()

#print('Bücher =',buecher)
buecher.sort()

'''
abschnitt = jeweils eine Liste von Bücherhöhen die zwischen zwei Figuren
stehen, deren Höhenunterschied also <= 3 ist.
'''
regal = []                                # eine Liste mit abschnitten     
abschnitt = []                            # der aktuelle abschnitt                 
abschnitt_starthoehe = buecher[0]         # starthöhe des aktuellen abschnitts

for b in buecher:
    if b - abschnitt_starthoehe <= 30:    # wenn Buchhöhe - starthoehe des abschnitts < 3cm
        abschnitt.append(b)               #   dann kommt das Buch in den abschnitt
    else:
        regal.append(abschnitt)           # sonst wird der bisherige abschnitt abgeschlossen und dem regal zugefügt
        abschnitt = [b]                   # ein neuer Abschnitt mit dem aktuellen Buch wird eröffnet
        abschnitt_starthoehe = b          # dieses erste Buch des Abschnitt bestimmt die starthoehe
        
regal.append(abschnitt)                   # der letzte abschnitt wird dem regal hinzugefügt

#print(regal)

if (anz_figuren >= len(regal)-1):         # man benötigt soviel figuren wie anzahl abschnitte-1
    print('Eine Aufstellung mit',anz_figuren,'Figuren ist möglich:')

    aufstellung = []                      # Liste für die Reihe der Bücher und Figuren
    for abschnitt in regal:              
        for b in abschnitt:
            aufstellung.append(b)
        aufstellung.append('Figur')       # nach jedem Abschnitt wird eine Figur plaziert

    #print(aufstellung)

    print(*aufstellung[:-1])              # die Figur nach dem letzten Abschnitt ist nicht nötig
else:
    print('Eine Aufstellung mit',anz_figuren,'Figuren ist nicht möglich')



 