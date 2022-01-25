import math
'''
Eine Position modellieren wir als eine Liste [x,y]
'''


def entfernung(pos1, pos2):
    '''
    pos1, pos2: Positionen, d.h. Listen [x,y]
    returns: die Entfernung zwischen pos1 und pos2 nach dem Satz von
    Pythagoras.
    '''
    return math.sqrt((pos1[0]-pos2[0])**2 + (pos1[1]-pos2[1])**2)


def minimal_entfernung(pos, posListe):
    ''' 
    pos: Position, d.h. Liste [x,y]
    posListe: Liste mit Positionen
    returns: minimale Entfernung von pos zu einer Position aus posListe
    '''
    return min([entfernung(pos, x) for x in posListe])


nr = 4
f = open('./beispieldaten/landkreis'+str(nr)+'.txt', encoding='utf-8')

haeuser = []    # Positionen der Häuser
masten = []     # Positionen der Masten

anz_haus, anz_mast = [int(x) for x in f.readline().split()]
for i in range(anz_haus):
    haeuser.append([int(k) for k in f.readline().split()])
for i in range(anz_mast):
    masten.append([int(k) for k in f.readline().split()])


print('landkreis', nr)
for m in masten:
    print(
        f'Mast an Position {m} darf Hoehe {minimal_entfernung(m,haeuser)/10:.2f} Meter haben')
