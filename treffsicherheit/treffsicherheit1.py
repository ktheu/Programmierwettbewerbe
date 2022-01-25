k = 4
f = open('./beispieldaten/praeferenzen'+str(k)+'.txt')

'''
Den Kalender modellieren wir als eine Liste von (Zeilen-)Listen
In der Liste bestBewertung merken wir uns für jede Person die  
beste Bewertung, die die Person für einen Termin vergeben hat.
'''
kalender = []
bestBewertung = []

rows, cols = [int(x) for x in f.readline().split()]
for i in range(rows):
    zeilenListe = [int(x) for x in f.readline().split()]
    kalender.append(zeilenListe)
    bestBewertung.append(min(zeilenListe))


'''
In der Liste aenderungen merken wir uns für jede Spalte (d.h. für jeden
Termin), wie häufig dieser Termin nicht der beste Termin für die
beteiligten Personen ist. 
'''
aenderungen = []   

for j in range(cols):                            # für jeden Termin
    anz = 0                                      # Anzahl Personen, für die der Termin nicht optimal ist
    for i in range(rows):                        # für jede Person                     
        if kalender[i][j] > bestBewertung[i]:    # Kalendereintrag schlechter als bester Termin?
            anz+=1                            
            
    aenderungen.append(anz)

'''
best = index der Spalte, für die die wenigsten Änderungen nötig sind.
Termin mit index 0 ist der 1. Termin, daher in der Ausgabe best+1
'''
best = aenderungen.index(min(aenderungen))    
print(f'Kalender {k}: Fuer Termin {best+1} benoetigt man {aenderungen[best]} Aenderungen.')


 

 
 


 
