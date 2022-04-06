### Spring Challenge 2020

#### Wood 2

In Wood2 kontrolliert jeder Spieler einen pac. Es gibt Super-pellets. Die erste Aufgabe ist
es, den pac an die Position eine Super-Pellets zu moven.

Damit kommt man schon aus der Wood2 League heraus:

```
    best_x, best_y, best_value = 0, 0, 0

    for i in range(visible_pellet_count):
        # value: amount of points this pellet is worth
        x, y, value = [int(j) for j in input().split()]
        if value > best_value:
            best_value = value
            best_x = x
            best_y = y


    print(f"MOVE {0} {best_x} {best_y}")
```

#### Wood 1

Nun kontrolliert man bis zu 5 Pacs.
Die einfachste Idee: Jeder pac geht zu dem pellet, der ihm am nächsten ist, gemessen
an der manhatten-distance.

```
def nextPellet(pac,pellets):
    '''
    pac = (x,y,id)
    pellets = list of pellets (x,y,score)...
    returns: pellet, der pac am nähesten ist
    '''
    x0,y0,_ = pac
    best = None
    best_val = 10000
    for p in pellets:
        x,y,_ = p
        if manhatten(x0,y0,x,y)<best_val:
            best_val = manhatten(x0,y0,x,y)
            best = p
    return p

.....

    ausgabe = ""
    for pac in my_pacs:
        pellet = nextPellet(pac,pellets)
        pellets.remove(pellet)
        ausgabe += f"MOVE {pac[2]} {pellet[0]} {pellet[1]}|"

    print(ausgabe[:-1])
```

Diese Idee erweist sich als zu simpel. Man kommt damit noch nicht über wood1 hinaus. (Platz 31)
Man sieht immer wieder Situationen, in denen sich die pacs in eine Situation verbeisen und
dann nicht herauskommen. Wir suchen eine sehr einfache Lösung:

Wenn wir feststellen, dass ein pac nicht weiterkommt, soll er sich ein zufälliges anderes pellet
als ziel suchen. Dies reicht für Bronze

```
    ausgabe = ""
    for k,pac in enumerate(my_pacs):
        if my_pacs_prev and pac == my_pacs_prev[k]:
            pellet = random.choice(pellets)
        else:
            pellet = nextPellet(pac,pellets)
            pellets.remove(pellet)
        info =f'{pellet[0]} {pellet[1]}'
        ausgabe += f"MOVE {pac[2]} {pellet[0]} {pellet[1]} {info}|"

    my_pacs_prev = my_pacs[:]
```

#### Bronze

Es kommen neue Regeln dazu: die Kommandos Boost und Switch sind möglich. Man sieht nur noch
in gerader Richtung die pellets.
