'''
Die leiter wird nicht mit einer Liste sondern mit einem Dictionary modelliert.
'''


f = open('leiter.txt')
anz = int(f.readline())
leiter = {}

for i in range(anz):
    zeile = f.readline().strip()
    x,y = zeile.split('-')
    x,y = int(x), int(y)
    leiter[x] = y
    leiter[y] = x

wurf = 6

anzahl = 0
besucht = [False]*100

pos = 0
zaehl = 0
while pos < 100 and zaehl < 120:
    
    pos+=wurf
    anzahl +=1
    if pos == 100:
        print(f'Mit {wurf} kommt man mit {anzahl} Würfen ans Ziel')
        break
    elif pos > 100:
        zuviel = pos-100
        pos = 100-zuviel
        print(f'Beim {anzahl}-ten Wurf zurück auf {pos}')

    if pos in leiter:
        pos = leiter[pos]

    if besucht[pos]:
        print(f'{pos} wird doppelt besucht. Mit {wurf} kommt man mit nicht ans Ziel')
        break   
    zaehl+=1
    besucht[pos]=True
