'''
Einlesen der Daten und sortieren der Bücher-Daten

'''
f = open('./beispieldaten/buecherregal5.txt')
anz_figuren = int(f.readline())
anz_buecher = int(f.readline())
buecher = []
for i in range(anz_buecher):
    buecher.append(int(f.readline()))

# print('anz_figuren:', anz_figuren)
# print('anz_buecher:',anz_buecher)
print('Bücher =',buecher)
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
    if b - abschnitt_starthoehe <= 30:
        abschnitt.append(b)
    else:
        regal.append(abschnitt)
        abschnitt = [b]
        abschnitt_starthoehe = b
        
regal.append(abschnitt)

if (anz_figuren >= len(regal)-1):
    print('Eine Aufstellung mit',anz_figuren,'Figuren ist möglich:')

    aufstellung = []
    for abschnitt in regal:
        for b in abschnitt:
            aufstellung.append(b)
        aufstellung.append('Figur')

    print(*aufstellung[:-1])   
else:
    print('Eine Aufstellung mit',anz_figuren,'Figuren ist nicht möglich:')



 