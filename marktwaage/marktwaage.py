def select(a, i, target, memo):
    '''
    a: Liste mit den Zahlen
    i: höchster Index Teilliste, bis zu der Werte genommen werden dürfen,
    um das target zu erreichen.
    target: die Zielsumme 

    returns: Liste mit der besten Annäherung an die Zielsumme

    gewünschter Wert: select(a,len(a)-1,target,memo)

    '''
    #print(f'select(a,{i},{target}) - Aufruf')
    teilsumme = sum(a[:i+1])
    if target <= -teilsumme:
        return [-x for x in a[:i+1]]
    if target >= teilsumme:
        return a[:i+1]

    if (i, target) in memo:
        #print(f'Nachschauen in memo {i}{target}')
        return list(memo[(i, target)])

    if i == -1:
        print(f'return []')
        return []

    l1 = select(a, i - 1, target - a[i], memo)  # a[i] wird mit + genommen
    l1.append(a[i])

    l2 = select(a, i - 1, target, memo)         # a[i] wird nicht genommen

    l3 = select(a, i - 1, target + a[i], memo)  # a[i] wird mit - genommen
    l3.append(-a[i])

    auswahl = [l1, l2, l3]

    t1 = sum(l1)
    t2 = sum(l2)
    t3 = sum(l3)

    vergleich = [(abs(t1-target), len(l1)), (abs(t2-target),
                                             len(l2)), (abs(t3-target), len(l3))]
    mindiff = min(vergleich)
    index = vergleich.index(mindiff)

    memo[(i, target)] = tuple(auswahl[index])
    #print(f'select(a,{i},{target}) - {auswahl[index]}')
    return auswahl[index]


f = open('beispieldaten/gewichtsstuecke5.txt')
anz = int(f.readline())

gewichte = []
for i in range(anz):
    g, n = [int(x) for x in f.readline().split()]
    for i in range(n):
        gewichte.append(g)


print('Gegenstand - links - rechts - Differenz')
for gegenstand in range(10, 10001, 10):
    memo = dict()

    a = select(gewichte.copy(), len(gewichte)-1, gegenstand, memo)
    for x in a.copy():
        if x in a and -x in a:
            a.remove(x)
            a.remove(-x)

    links = [-x for x in a if x < 0]
    rechts = [x for x in a if x > 0]

    print(f'{gegenstand} - {links} - {rechts} - {gegenstand+sum(links) -sum(rechts)}')
