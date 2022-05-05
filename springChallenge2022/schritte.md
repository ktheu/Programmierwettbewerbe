```python
from collections import namedtuple
import math, sys
```

## Spring Challenge 2022

#### 01 

Copy Starter Code

#### 02 

- Funktion log einfügen
- Konstanten WIDTH und HEIGHT für die Spielfläche
- namedtuple Point und die basen als Point modellieren.
- eine Funktion spiegle, die einen Punkt an der Mitte spiegelt
- Variablen my_base und opp_base als Punkte
- Funktion distance für die Entfernung zwischen zwei Punkten
- Eine Variable debug, die die log-Ausgaben steuert.
- Eine Variable turn, für die Nummer des Durchgangs
 

Variablennamen
- p, p1, p2, ... für Punkte, pp für eine Liste mit Punkten
- e, e1, e2, ... für Entities, ee für eine Liste mit Entities



```python
def log(*x):
    print(*x, file=sys.stderr)
    
def spiegle(p):
    return Point(WIDTH-p.x, HEIGHT-p.y)

def distance(p1, p2):
    return math.hypot(p2.x-p1.x, p2.y-p1.y)

WIDTH, HEIGHT = 17630,  9000

Point = namedtuple('Point', 'x y')

my_base = Point(base_x, base_y)
opp_base = Point(my_base)

debug = True
turn = 0

# game loop
while True:
    turn +=1
    ....
```

Test


```python
if debug: log(f'turn: {turn}')

for i in range(heroes_per_player):
    h = my_heroes[i]

    if debug: 
        log(f'Pos {h.id}: {h.x} {h.y}')
```

Beobachtung: Die Koordinaten, die z.B. für turn 8 mit log ausgeben werden sind die, die man bei turn 7 auf dem Bild sieht.
log spiegelt die Situation zu Beginn des turns wieder, das Bild die Situation am Ende des turns.

#### 03

Die heros sollen sich zu Beginn in einen Anfangsposition begeben. Wir wählen geeignete startpoints. Falls wir nicht
links spielen, müssen wir die startpoints spiegeln


```python
links = True if my_base == Point(0,0) else False
startpoints = [Point(5500,1500),Point(4500,4500),Point(1500,5500)]
if not links:
    startpoints = [spiegle(p) for p in startpoints]
```

Test durch Spielen gegen sich selbst

#### 04

Sortieren der Monster nach threatlevels. Kontrolle durch ausgeben der threatlevels.



```python
def threatlevel(m):
    wd = 1000    # Gewicht für die Distanz
    dist = 1/distance(m,my_base)

    threat = wd * dist
    return threat


monsters = sorted(monsters,key = threatlevel, reverse = True)
if debug:
    for m in monsters:
        log(f'{m.id}:dist={distance(m,my_base):.0f} threat={threatlevel(m):.4f}')
```

#### Zwischenstand 01 - 04


```python
import sys
import math
from collections import namedtuple

def log(*x):
    print(*x, file=sys.stderr)
    
def spiegle(p):
    return Point(WIDTH-p.x, HEIGHT-p.y)

def distance(p1, p2):
    return math.hypot(p2.x-p1.x, p2.y-p1.y)


def threatlevel(m):
    wd = 1000
    dist = 1/distance(m,my_base)

    threat = wd * dist
    return threat

Entity = namedtuple('Entity', [
    'id', 'type', 'x', 'y', 'shield_life', 'is_controlled', 'health', 'vx', 'vy', 'near_base', 'threat_for'
])
Point = namedtuple('Point', 'x y')

TYPE_MONSTER = 0
TYPE_MY_HERO = 1
TYPE_OP_HERO = 2

WIDTH, HEIGHT = 17630,  9000

base_x, base_y = [int(i) for i in input().split()]
heroes_per_player = int(input())

my_base = Point(base_x, base_y)
opp_base, opp_base_y = spiegle(my_base)

links = True if my_base == Point(0,0) else False
startpoints = [Point(5500,1500),Point(4500,4500),Point(1500,5500)]
if not links:
    startpoints = [spiegle(p) for p in startpoints]

debug = True
turn = 0
 
# game loop
while True:
    turn+=1
    
    my_health, my_mana = [int(j) for j in input().split()]
    enemy_health, enemy_mana = [int(j) for j in input().split()]
    entity_count = int(input())  # Amount of heros and monsters you can see

    monsters = []
    my_heroes = []
    opp_heroes = []
    for i in range(entity_count):
        _id, _type, x, y, shield_life, is_controlled, health, vx, vy, near_base, threat_for = [int(j) for j in input().split()]
        entity = Entity(
            _id,            # _id: Unique identifier
            _type,          # _type: 0=monster, 1=your hero, 2=opponent hero
            x, y,           # x,y: Position of this entity
            shield_life,    # shield_life: Ignore for this league; Count down until shield spell fades
            is_controlled,  # is_controlled: Ignore for this league; Equals 1 when this entity is under a control spell
            health,         # health: Remaining health of this monster
            vx, vy,         # vx,vy: Trajectory of this monster
            near_base,      # near_base: 0=monster with no target yet, 1=monster targeting a base
            threat_for      # threat_for: Given this monster's trajectory, is it a threat to 1=your base, 2=your opponent's base, 0=neither
        )
        
        if _type == TYPE_MONSTER:
            monsters.append(entity)
        elif _type == TYPE_MY_HERO:
            my_heroes.append(entity)
        elif _type == TYPE_OP_HERO:
            opp_heroes.append(entity)

    if debug: log(f'turn: {turn}')

    monsters = sorted(monsters,key = threatlevel, reverse = True)
    if debug:
        for m in monsters:
            log(f'{m.id}:dist={distance(m,my_base):.0f} threat={threatlevel(m):.4f}')
          
  
    for i in range(heroes_per_player):
        h = my_heroes[i]

        if debug: 
            log(f'Pos {h.id}: {h.x} {h.y}')
    
        target = None
        if monsters:
             
            target = monsters[i % len(monsters)]

        if target:
            print(f'MOVE {target.x} {target.y}')
        else:
            print(f'MOVE {startpoints[i].x} {startpoints[i].y}')
```
