import math

def abstandZumUrsprung(pos):
    '''
    pos: Koordinate als Liste [x,y]
    returns: abstand von pos zum Ursprung [0,0]
    '''

    return math.sqrt(pos[0]**2 + pos[1]**2)

# Kontrolle
print(abstandZumUrsprung([2,0]))
print(abstandZumUrsprung([1,1]))

'''
Erwartete Ausgabe:
2.0
1.4142135623730951
'''


def abstaendeZumUrsprung(a):
    '''
    a: Liste mit Koordinaten der Form [x,y]
    returns: Liste mit den Abständen der Koordinaten zum Ursprung
    '''
    return [abstandZumUrsprung(b) for b in a]

# Kontrolle
a = [[2, 0], [1, 1], [2, 1], [3, 3]]
print(abstaendeZumUrsprung(a))

'''
Erwartete Ausgabe:
[2.0, 1.4142135623730951, 2.23606797749979, 4.242640687119285]
'''

def groessterAbstandZumUrsprung(a):
    '''
    a: Liste mit Koordinaten der Form [x,y]
    returns: eine Koordinate aus a mit dem größten Abstand zum Ursprung
    '''
    b = abstaendeZumUrsprung(a)
    maxAbstand = max(b)
    index_maxAbstand = b.index(maxAbstand)
    return a[index_maxAbstand]

# Kontrolle
a = [[2, 0], [1, 1], [4, 3], [2, 5], [2, 1]]
print(groessterAbstandZumUrsprung(a))
 
'''
Erwartete Ausgabe:
[2, 5]
'''
