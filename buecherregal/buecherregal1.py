nr = 1
f = open('./beispieldaten/buecherregal'+str(nr)+'.txt')

anz_figuren = int(f.readline())
anz_buecher = int(f.readline())

buecher = []           # Liste mit den Büchern

for i in range(anz_buecher):
    buecher.append(int(f.readline()))

buecher.sort()
zaehl = 0              # Anzahl aufgestellter Figuren
print(f'Aufstellung für Bücherregal {nr}:')

i = 0                  # Anfang des Abschnitts
j = 0                  # aktuelles Buch
while j < len(buecher):                # solange noch nicht am Ende der Bücherliste
    if buecher[j] - buecher[i] <= 30:  # passt aktuelles Buch noch in den Abschnitt?
        print(buecher[j],end=' ')      # Buch in den Abschnitt
    else:
        print('Figur')                 # Abschnittsende, setzen der Figur
        print(buecher[j],end=' ')      # aktuelles Buch ist Beginn des nächsten Abschnitts
        zaehl += 1                     # Erhöhe Anzahl aufgestellter Figuren
        i = j          # Anfang des Abschnitts wird das aktuelle Buch
    j = j + 1          # ein Buch weiter in der Liste
print()

if zaehl <= anz_figuren:               # Anzahl verwendeter Figuren <= Anzahl verfügbare Figuren?
    print(f'Aufteilung mit {anz_figuren} Figuren ist möglich.')
else: 
    print(f'Aufteilung mit {anz_figuren} Figuren ist nicht möglich.')
 


