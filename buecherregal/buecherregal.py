nr = 1
f = open('./beispieldaten/buecherregal'+str(nr)+'.txt')

anz_figuren = int(f.readline())
anz_buecher = int(f.readline())

buecher = []           # Liste mit den Büchern

for i in range(anz_buecher):
    buecher.append(int(f.readline()))

buecher.sort()

regal = []             # die Aufstellung von Büchern und Figuren
zaehl = 0              # Anzahl aufgestellter Figuren
print(f'Bücherregal {nr}:')

i = 0                  # Anfang des Abschnitts
j = 0                  # aktuelles Buch
while j < len(buecher):                # solange noch nicht am Ende der Bücherliste
    if buecher[j] - buecher[i] <= 30:  # passt aktuelles Buch noch in den Abschnitt?
        regal.append(buecher[j])       # Buch in den Abschnitt
    else:
        regal.append('\nFigur')          # Abschnittsende, setzen der Figur
        regal.append(buecher[j])       # aktuelles Buch ist Beginn des nächsten Abschnitts
        zaehl += 1                     # Erhöhe Anzahl aufgestellter Figuren
        i = j          # Anfang des Abschnitts wird das aktuelle Buch
    j = j + 1          # ein Buch weiter in der Liste
 

if zaehl <= anz_figuren:               # Anzahl verwendeter Figuren <= Anzahl verfügbare Figuren?
    print(f'Aufteilung mit {anz_figuren} Figuren ist möglich.')
    for x in regal:
        print(x,end= ' ')
else: 
    print(f'Aufteilung mit {anz_figuren} Figuren ist nicht möglich.')
 


