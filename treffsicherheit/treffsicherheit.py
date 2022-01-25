k = 5
f = open('./beispieldaten/praeferenzen'+str(k)+'.txt')

'''
Den Kalender modellieren wir als eine Liste von (Zeilen-)Listen

'''
kalender = []
rows, cols = [int(x) for x in f.readline().split()]
for i in range(rows):
    kalender.append([int(x) for x in f.readline().split()])

def istMinimum(a,k):
    '''
    a: Liste mit Zahlen
    k: gültiger Index für a
    returns: True, wenn a[k] Minimum in a ist
    '''
    return a[k] == min(a)


'''
In der Liste aenderungen merken wir uns für jede Spalte (d.h. für jeden
Termin), wie häufig dieser Termin nicht der beste Termin für die
beteiligten Personen ist. 
'''
aenderungen = []   

for j in range(cols):
    anz = 0
    for i in range(rows):
        if not istMinimum(kalender[i],j):    # kalender[i] = Termine für die i-te Person
            anz+=1
            
    aenderungen.append(anz)

'''
best = index der Spalte, für die die wenigsten Änderungen nötig sind.
Termin mit index 0 ist der 1. Termin, daher in der Ausgabe best+1
'''
best = aenderungen.index(min(aenderungen))   # index der Spalte, für die die wenigsten Änderungen nötig sind.
print(f'Kalender {k}: Fuer Termin {best+1} benoetigt man {aenderungen[best]} Aenderungen.')


 

 
 


 
