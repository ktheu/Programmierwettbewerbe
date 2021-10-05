'''
Die Liste a besteht aus Koordinaten der Form [x,y] 
Erzeuge eine neue Liste b und speichere darin die
das Quadrat der Differenz:  (x-y)**2
'''

a = [[2, 1], [1, -1], [0, 3]]
b = []
for pos in a:
    b.append((pos[0]-pos[1])**2)

# Kontrolle
print(b)

'''
Erwartete Ausgabe:
[1, 4, 9]
'''