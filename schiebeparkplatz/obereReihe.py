import doctest
def obereReihe(s):
    '''
    s: String mit zwei großen Buchstaben c1 und c2, c1 kommt im Alphabet vor c2
    returns: Liste mit den großen Buchstaben des Alphabet von c1 bis c2 (einschließlich)

    >>> obereReihe('A G')
    ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    >>> obereReihe('A A')
    ['A']

    >>> obereReihe('G K')
    ['G', 'H', 'I', 'J', 'K']

    '''
    c1, c2 = s.split()
    return [chr(k) for k in range(ord(c1), ord(c2)+1)]  

def untereReihe(sList,anzahlPlaetze):
    '''
    sList: Liste mit den Daten für die untere Reihe, 
    'H 2' bedeutet, dass ein Fahrzeug mit der Kennung 'H' auf den Plätzen 2 und 3 steht.
    returns: Tuple mit der Belegung der unteren Reihe, leere Plätze werden durch '.' ersetzt
    Jedes Fahrzeug belegt genau zwei Plätze.

    >>> untereReihe(['H 2', 'I 5'],7)
    ('.', '.', 'H', 'H', '.', 'I', 'I')

    >>> untereReihe(['B 1', 'E 4', 'J 8'],11)   
    ('.', 'B', 'B', '.', 'E', 'E', '.', '.', 'J', 'J', '.')

    >>> untereReihe(['A 0', 'B 2'],4)
    ('A', 'A', 'B', 'B')

    '''
    a = ['.']*anzahlPlaetze
    for s in sList:
        c, k = s.split()
        k = int(k)
        a[k] = c
        a[k+1] = c
    return tuple(a)

def showParkplatz(s, sList):
    '''
    s: String mit zwei großen Buchstaben c1 und c2, c1 kommt im Alphabet vor c2
    sList: Liste mit den Daten für die untere Reihe

    returns: None, gibt den Parkplatz mit zwei Zeilen auf der Konsole aus

    >>> showParkplatz('A G',['H 2', 'I 5'])
    A B C D E F G
    . . H H . I I

    >>> showParkplatz('A N',['O 1', 'P 3', 'Q 6', 'R 10'])
    A B C D E F G H I J K L M N
    . O O P P . Q Q . . R R . .

    >>> showParkplatz('A N',['O 1', 'P 4', 'Q 8', 'R 10', 'S 12'])
    A B C D E F G H I J K L M N
    . O O . P P . . Q Q R R S S

    '''
    oben = obereReihe(s)
    s1 = ' '.join(oben)
    s2 = ' '.join(untereReihe(sList,len(oben)))
    print(s1)
    print(s2)


def nextstates(state):
    '''
    state = tuple mit der Belegung der unteren Reihe
    returns: Liste mit den Folgezuständen, die durch eine Bewegung EINES Fahrzeugs entstehen

    Die Sortierung beim Testen ist wichtig, da die Reihenfolge der Folgezustände nicht festgelegt ist.

    >>> sorted(nextstates(('.', '.', 'H', 'H', '.', 'I', 'I')))
    [('.', '.', '.', 'H', 'H', 'I', 'I'), ('.', '.', 'H', 'H', 'I', 'I', '.'),\
 ('.', 'H', 'H', '.', '.', 'I', 'I'), ('H', 'H', '.', '.', '.', 'I', 'I')]


    >>> sorted(nextstates(('.', 'A', 'A', 'B', 'B', '.', '.')))
    [('.', 'A', 'A', '.', '.', 'B', 'B'), ('.', 'A', 'A', '.', 'B', 'B', '.'), ('A', 'A', '.', 'B', 'B', '.', '.')]


    >>> sorted(nextstates(('.', 'O', 'O', 'P', 'P', '.', 'Q', 'Q', '.', '.', 'R', 'R', '.', '.')))
    [('.', 'O', 'O', '.', 'P', 'P', 'Q', 'Q', '.', '.', 'R', 'R', '.', '.'),\
 ('.', 'O', 'O', 'P', 'P', '.', '.', '.', 'Q', 'Q', 'R', 'R', '.', '.'),\
 ('.', 'O', 'O', 'P', 'P', '.', '.', 'Q', 'Q', '.', 'R', 'R', '.', '.'),\
 ('.', 'O', 'O', 'P', 'P', '.', 'Q', 'Q', '.', '.', '.', '.', 'R', 'R'),\
 ('.', 'O', 'O', 'P', 'P', '.', 'Q', 'Q', '.', '.', '.', 'R', 'R', '.'),\
 ('.', 'O', 'O', 'P', 'P', '.', 'Q', 'Q', '.', 'R', 'R', '.', '.', '.'),\
 ('.', 'O', 'O', 'P', 'P', '.', 'Q', 'Q', 'R', 'R', '.', '.', '.', '.'),\
 ('.', 'O', 'O', 'P', 'P', 'Q', 'Q', '.', '.', '.', 'R', 'R', '.', '.'),\
 ('O', 'O', '.', 'P', 'P', '.', 'Q', 'Q', '.', '.', 'R', 'R', '.', '.')]
    
    
    '''
    tmp = []
    querwagen = {c for c in state if c!='.'}  # set mit allen Wagen, die quer stehen
    for c in querwagen:
        k = state.index(c)
        new_state = list(state)
        while k+2 < len(state) and state[k+2]=='.':   # solange rechts Platz ist
            new_state[k]='.'                          # verschiebe die beiden Zeichen in new_state                     
            new_state[k+2]=c                          # um eins nach rechts
            tmp.append(tuple(new_state))              # speichere den Zustand als möglichen Folgezustand
            k+=1
            
        k = state.index(c)                            
        new_state = list(state)
        while k-1 >= 0 and new_state[k-1]=='.':       # solange links Platz ist
            new_state[k-1]=c
            new_state[k+1]='.'
            tmp.append(tuple(new_state))
            k-=1
    return tmp

from collections import deque
def bfs(startstate, idx):
    '''
    startstate: Tuple, z.B: ('.', '.', 'H', 'H', '.', 'I', 'I')
    idx: index des Parkplatzes, der frei werden soll

    returns: (prev, state), wobei
        prev - dictionary das zu jedem state den vorgänger speichert
        state - der Zustand, in dem der Parkplatz frei ist

    >>> prev, state = bfs(('.', '.', 'H', 'H', '.', 'I', 'I'), 0)
    >>> state
    ('.', '.', 'H', 'H', '.', 'I', 'I')
    >>> len(prev)
    1

    >>> prev, state = bfs(('.', '.', 'H', 'H', '.', 'I', 'I'), 2)
    >>> state
    ('.', '.', '.', 'H', 'H', 'I', 'I')
    >>> len(prev)
    2
           
    
    '''
    frontier =  deque([startstate])
    prev = {startstate:None}
    if startstate[idx] == '.':         # ziel erreicht?
            return prev, startstate
    while frontier:
        state = frontier.popleft()
        for state1 in sorted(nextstates(state),key=(lambda s:(sum(x!=y for x,y in zip(s,state)),state) )):      # das sorted ist nur für einheitliche Tests
            if state1 not in prev:
                prev[state1] = state
                if state1[idx] == '.':     # ziel erreicht?
                    return prev, state1
                frontier.append(state1)

def reconstructPath(prev,goalstate):
    '''
    prev, goalstate: siehe bfs
    returns: Liste der Zustände von startstate bis goalstate

    >>> prev, state = bfs(('.', '.', 'H', 'H', '.', 'I', 'I'), 2)
    >>> reconstructPath(prev, state)
    [('.', '.', 'H', 'H', '.', 'I', 'I'), ('.', '.', '.', 'H', 'H', 'I', 'I')]

    '''
    state = goalstate
    path = []
    while state is not None:
        path.append(state)
        state = prev[state]        
    path.reverse()
    return path

def schiebeAnweisung(state1, state2):
    '''
    state1, state2: zwei benachbarte Zustände
    returns: Anweisung, wie die Wagen zu schieben sind.

    >>> schiebeAnweisung(('.', '.', 'H', 'H', '.', 'I', 'I'), ('.', '.', '.', 'H', 'H', 'I', 'I'))
    'H: 1 nach rechts'


    >>> schiebeAnweisung(('.', '.', 'H', 'H', '.', 'I', 'I'), ('H', 'H', '.', '.', '.', 'I', 'I'))
    'H: 2 nach links'

    >>> schiebeAnweisung(('H', 'H', '.', '.', '.', 'I', 'I'),('H', 'H', 'I', 'I', '.', '.', '.'))
    'I: 3 nach links'
    
    '''
    querwagen = {c for c in state1 if c!='.'}
    for c in querwagen:
        i1 = state1.index(c)
        i2 = state2.index(c)
        if i1 > i2:
            return f'{c}: {i1-i2} nach links' 
        if i1 < i2:
            return f'{c}: {i2-i1} nach rechts' 

def schiebeParkplatz(s,sList):
    '''
    s - String  siehe obereReihe
    sList - Liste von Strings, siehe untereReihe

    Die Ausgabe sollte ungefähr wie unten aussehen. Das genaue Aussehen ist nicht wichtig und
    wird nicht getestet.

    >>> schiebeParkplatz('A G',['H 2','I 5'])
    A : 
    B : 
    C : H: 1 nach rechts
    D : H: 1 nach links
    E :
    F : H: 1 nach links  I: 2 nach links
    G : I: 1 nach links


    >>> schiebeParkplatz('A N',['O 1','P 3','Q 6','R 10'])
    A : 
    B : P: 1 nach rechts  O: 1 nach rechts  
    C : O: 1 nach links
    D : P: 1 nach rechts
    E : Q: 2 nach rechts  P: 3 nach rechts
    F :
    G : Q: 2 nach rechts
    H : Q: 2 nach rechts
    I :
    J :
    K : R: 2 nach rechts
    L : R: 2 nach rechts
    M :
    N : 

    '''
    oben = obereReihe(s)
    anzahlPlaetze = len(oben)
    startstate = untereReihe(sList,anzahlPlaetze)
    for i, c in enumerate(oben):
        print(c,end=': ')
        prev, state = bfs(startstate, i)
        path = reconstructPath(prev, state)
        for state1, state2 in zip(path[:-1], path[1:]):
            print(schiebeAnweisung(state1, state2),end= '  ')
        print()
   
 
# doctest.run_docstring_examples(obereReihe,globals())
# doctest.run_docstring_examples(untereReihe,globals())
#doctest.run_docstring_examples(showParkplatz,globals())
doctest.run_docstring_examples(nextstates,globals())
doctest.run_docstring_examples(bfs,globals())
doctest.run_docstring_examples(reconstructPath,globals())
doctest.run_docstring_examples(schiebeAnweisung,globals())

#print(sorted(nextstates(('.', 'A', 'A', 'B', 'B', '.', '.'))))

#prev, state = bfs(('.', 'O', 'O', 'P', 'P', '.', 'Q', 'Q', '.', '.', 'R', 'R', '.', '.'), 4)
#print(reconstructPath(prev, state))
schiebeParkplatz('A G',['H 2','I 5']) # input 0
#schiebeParkplatz('A N',['O 1','P 3','Q 6','R 10'])  # input 1
#schiebeParkplatz('A N',['O 2','P 5','Q 7','R 9', 'S 12'])  # input 2
#schiebeParkplatz('A N',['O 1','P 4','Q 8','R 10', 'S 12']) # input 3
#schiebeParkplatz('A P',['Q 0','R 2','S 6','T 10', 'U 13']) # input 4
#schiebeParkplatz('A O',['P 2', 'Q 4','R 8','S 12']) # input 5
'''



'''