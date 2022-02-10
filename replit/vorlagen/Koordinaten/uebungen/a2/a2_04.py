def minIndex(a):
    '''
    a: Liste mit Zahlen
    returns: Index k, so dass a[k] das Minimum von a ist
    '''
    return a.index(min(a))

print(minIndex([2,3,1,4,3,2,1]))
print(minIndex([2,3,1,4,3,2,0]))

'''
Erwartete Ausgabe:
2
6

'''