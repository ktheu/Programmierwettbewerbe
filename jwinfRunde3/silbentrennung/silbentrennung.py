def trennung(wort):

     

    # regel1: ein Wort kann zwischen zwei Konsonanten getrennt werden
    r1 = [0]*len(wort)
    for i in range(len(wort) - 1):
        if wort[i] in konsonanten and wort[i + 1] in konsonanten:
            r1[i] = 1
    print(r1)
            

    # regel2: erster und letzter Buchstabe eines Wortes dürfen nicht abgetrennt werden  
    r2 = [0]*len(wort)
    erster = 0
    while wort[erster] not in buchstaben:
        erster +=1
    letzter = len(wort)-1
    while wort[letzter] not in buchstaben:
        letzter -=1
    r2[erster] = -1
    r2[letzter-1] = -1
    print(r2)

    # regel3: bei drei aufeinanderfolgenden Konsonanten kann nur nach dem ersten Konsonanten getrennt werden
    r3 = [0]*len(wort)
    for i in range(len(wort)-2):
        if r3[i] != 0: continue
        if wort[i] in konsonanten and wort[i+1] in konsonanten and wort[i+2] in konsonanten:
            r3[i] = 1
            r3[i+1] = -1
            r3[i+2] = -1
    print(r3)

    # regel4: Ein Wort kann nach einem Vokal getrennt werden, falls nicht zwei Konsonanten folgen
    r4 = [0]*len(wort)
    for i in range(len(wort) - 2):
        if wort[i] in vokale:
            if (wort[i + 1] in vokale or wort[i + 2] in vokale):
               r4[i] = 1
            else:
               r4[i] = -1
    k = len(wort)-2           # vorletztes Zeichen
    if wort[k] in vokale and wort[k+1] in buchstaben: 
        r4[k] = 1
    print(r4)

    regeln = [r4,r3,r2,r1]
    r_gesamt = [0]*len(wort)
    for i in range(len(wort)-1):
        for r in regeln:
            if r[i] != 0:
                r_gesamt[i] = r[i]
                break
    print(r_gesamt)

    s = ''
    for i in range(len(wort)):
        s = s + wort[i]
        if r_gesamt[i] == 1:
            s = s + '-'
    print(s)


nr = '00'
f = open(f'beispieldaten/silben{nr}.txt',encoding='utf-8')
satz = f.readline()

f.close()
print(f'Beispiel silben{nr}:')

for wort in satz.split():
    trennstellen = alleRegeln(wort)
    print(getTrennung(wort, trennstellen),end=' ')

print()
print()

