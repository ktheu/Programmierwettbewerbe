'''
Alles mit Listen, die Leiter wird mit if-else hard-codiert.
'''

wurf = 4

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

    if pos == 6: pos = 27
    elif pos == 27: pos = 6
    elif pos == 14: pos = 19
    elif pos == 19: pos = 14
    elif pos == 21: pos = 53
    elif pos == 53: pos = 21
    elif pos == 31: pos = 42
    elif pos == 42: pos = 31
    elif pos == 33: pos = 38
    elif pos == 38: pos = 33
    elif pos == 46: pos = 62
    elif pos == 62: pos = 46
    elif pos == 51: pos = 59
    elif pos == 59: pos = 51
    elif pos == 57: pos = 96
    elif pos == 96: pos = 57
    elif pos == 65: pos = 85
    elif pos == 85: pos = 65      
    elif pos == 68: pos = 80
    elif pos == 80: pos = 68
    elif pos == 70: pos = 76
    elif pos == 76: pos = 60
    elif pos == 92: pos = 98
    elif pos == 98: pos = 92
    if besucht[pos]:
        print(f'{pos} wird doppelt besucht. Mit {wurf} kommt man mit nicht ans Ziel')
        break   
    zaehl+=1
    besucht[pos]=True

 
