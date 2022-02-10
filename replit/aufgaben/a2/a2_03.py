def istMinimum(a,k):
    '''
    a: Liste mit Zahlen
    k: gültiger Index für a
    returns: True, wenn a[k] Minimum in a ist
    '''
    return a[k] == min(a)


# Kontrolle
a = [1,2,0,1,2,3,0]
print(istMinimum(a, 0))
print(istMinimum(a, 2))
print(istMinimum(a, 6))

'''
Erwartete Ausgabe:
False
True
True
'''