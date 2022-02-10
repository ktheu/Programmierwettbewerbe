## Trainingsaufgaben

---

A1

```
def func(a):
    '''
    a: Nicht leere Liste
    returns: eine neue Liste mit zwei Elementen: dem ersten und letzten Element von a.

    Tests:
    print(func([1,2,3,4])), print(func([1]))

    Erwartete Ausgaben:
    [1, 4], [1, 1]

    '''
    # your code here

```

---

A2

```
def func(a):
    a: Nicht leere Liste von ganzen Zahlen
    returns: nichts, löscht das größte Element in a.
             Wenn das größte Element mehrmals vorkommt, werden alle Vorkommen gelöscht.

    Tests:
    a = [1,4,4,3] .. [4,4,4,4]
    func(a)
    print(a)

    Erwartete Ausgabe:
    [1, 3] ..  []

    '''
    # your code here


```

---

A3

```
'''
Schreibe eine Funktion convert, die die Zeichen eines Strings nach
der folgenden Codierungstabelle umsetzt.

a -> c         A -> C
b -> d         B -> D
c -> e         C -> E
.    .         .    .
.    .         .    .
x -> z         X -> Z
y -> a         Y -> A
z -> b         Z -> B

Test:
print(convert('abcdwxyzABCDWXYZ'))

Erwartete Ausgabe:
defgzabcDEFGZABC

'''

def convert(s):
    '''
    s: String mit Buchstaben des englischen Alphabets (a-z,A-Z)
    returns: String mit der Umsetzung gemäß Codierungstabelle
    '''
    # your code here


```

---

A4

```
'''
Die Ausgabe soll beschreiben, wer wem den Ball zuwirft, wenn die
Wurfrichtung umgedreht wird.

Erwartete Ausgabe:

Michelangelo passes the ball to Leonardo
Donatello passes the ball to Raphael
Leonardo passes the ball to Donatello
Raphael passes the ball to Michelangelo
'''

data = ['Michelangelo passes the ball to Raphael',
        'Donatello passes the ball to Leonardo',
        'Leonardo passes the ball to Michelangelo',
        'Raphael passes the ball to Donatello']

# your code here


```

---

A5

```
data = ['00 00 01','00 01 10','00 11 00','10 11 01']

'''
Jede Spalte ist die Zahl der Uhrzeit im binären Format.
Z.B: 3 = 0011 (die Spalte über der 3)

00 00 01
00 01 10
00 11 00
10 11 01

Erwartete Ausgabe:

10:37:49
# your code here
'''


```
