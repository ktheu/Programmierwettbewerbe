
def kollision(a,b,c,d,e,f,g,h):
    '''
    (a,b), (c,d) Koordinaten des 1. Rechtecks
    (e,f), (g,h) Koordinaten des 2. Rechtecks
    
    returns True, wenn das 1.Rechteck weder links noch rechts noch oberhalb noch
       unterhalb des 2. Rechtecks liegt. Dann liegt eine Kollision vor.
    '''
    links = max(a,c) <= min(e,g)
    rechts = max(e,g) <= min(a,c)
    oberhalb = max(f,h) <= min(b,d)
    unterhalb = max(b,d) <= min(f,h)
    return not (links or rechts or oberhalb or unterhalb)

f = open('eingabe2.txt')     # Die Eingabe in eine Liste von Strings einlesen
lines = [x.rstrip('\n') for x in f.readlines()]
N = len(lines)               # Anzahl Rechtecke

genehmigt = [True] * N       # alle Rechtecke werden vorläufig genehmigt.

rechtecke = []
for line in lines:
    a = [int(x) for x in line.split()]    # Ein Rechteck ist eine Liste aus 4 ints.
    rechtecke.append(a)

for i in range(1, N):
    a, b, c, d = rechtecke[i]
    for j in range(i):                          # Prüfe ob Kollision mit
        if genehmigt[j]:                        # schon genehmigten Rechtecken vorliegt
            e, f, g, h = rechtecke[j]
            if kollision(a,b,c,d,e,f,g,h):      # Falls Kollision 
                genehmigt[i] = False            # Genehmigung wird widerrufen
                break
            
for i in range(N):
    entscheidung = "genehmigt" if genehmigt[i] else "abgelehnt"
    print(*rechtecke[i], entscheidung)
            
            
    
    
 
