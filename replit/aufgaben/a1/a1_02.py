'''
Schreibe eine Funktion abstand, die den Abstand zwischen zwei
Koordinaten zurückgibt

'''
import math
def abstand(pos1, pos2):
    '''
    pos1: Koordinate in der Form [x, y] 
    pos2: wie pos1
    returns: abstand zwischen pos1 und pos2
    '''
    return math.sqrt((pos2[0]-pos1[0])**2 + (pos2[1]-pos1[1])**2)

print(abstand([0,0],[1,0]))
print(abstand([1,1],[1,2]))
print(abstand([0,1],[1,2]))

'''
Erwartete Ausgabe:
1.0
1.0
1.4142135623730951
'''
