## Zum Winde verweht

40\. Bundeswettbewerb Informatik - Junioraufgabe 1

[Aufgabenstellung](aufgabenstellung.png) - [Beispieldaten](beispieldaten.md) - [Lösungshinweise](./zumWindeVerweht.pdf)

Hinweise zu den Beispieldaten: Jede Datei beschreibt einen Landkreis und enthält

-   in der ersten Zeile die Anzahl n der Häuser in dem Landkreis und die
    Anzahl m der Windräder in dem Landkreis,
-   in den weiteren n Zeilen jeweils die Positionen der Häuser (als x-
    und y-Koordinate, in Meter) und anschließend
-   in den weiteren m Zeilen jeweils die Positionen der Windräder (auch
    als x- und y-Koordinate, in Meter).

#### Python

```
import math

'''
Eine Position modellieren wir als eine Liste [x,y]
'''

def entfernung(pos1, pos2):
    '''
    pos1, pos2: Positionen, d.h. Listen [x,y]
    returns: die Entfernung zwischen pos1 und pos2 nach dem Satz von
    Pythagoras.
    '''
    return math.sqrt((pos1[0]-pos2[0])**2 + (pos1[1]-pos2[1])**2)


def minimal_entfernung(pos, posListe):
    '''
    pos: Position, d.h. Liste [x,y]
    posListe: Liste mit Positionen
    returns: minimale Entfernung von pos zu einer Position aus posListe
    '''
    return min([entfernung(pos, x) for x in posListe])


nr = 1
f = open('./beispieldaten/landkreis'+str(nr)+'.txt', encoding='utf-8')

haeuser = []    # Positionen der Häuser
masten = []     # Positionen der Masten

anz_haus, anz_mast = [int(x) for x in f.readline().split()]
for i in range(anz_haus):
    haeuser.append([int(k) for k in f.readline().split()])
for i in range(anz_mast):
    masten.append([int(k) for k in f.readline().split()])


print('landkreis', nr)
for m in masten:
    print(
        f'Mast an Position {m} darf Hoehe {minimal_entfernung(m,haeuser)/10:.2f} Meter haben')

```

Ausgabe:

```
landkreis 1
Mast an Position [1242, -593] darf Hoehe 48.52 Meter haben
Mast an Position [-1223, -1479] darf Hoehe 158.98 Meter haben
Mast an Position [1720, 401] darf Hoehe 72.41 Meter haben
```

```
landkreis 2
Mast an Position [359, 20] darf Hoehe 115.16 Meter haben
Mast an Position [2, -773] darf Hoehe 201.25 Meter haben
Mast an Position [315, -213] darf Hoehe 138.85 Meter haben
Mast an Position [-629, -532] darf Hoehe 209.12 Meter haben
Mast an Position [97, -69] darf Hoehe 132.01 Meter haben
Mast an Position [-392, -418] darf Hoehe 186.16 Meter haben
Mast an Position [87, -384] darf Hoehe 161.68 Meter haben
Mast an Position [-597, 612] darf Hoehe 133.30 Meter haben
Mast an Position [-13, -32] darf Hoehe 133.54 Meter haben
Mast an Position [-57, 49] darf Hoehe 128.77 Meter haben
Mast an Position [276, 292] darf Hoehe 91.78 Meter haben
Mast an Position [156, 55] darf Hoehe 118.28 Meter haben
Mast an Position [-423, -93] darf Hoehe 161.95 Meter haben
Mast an Position [202, -219] darf Hoehe 142.39 Meter haben
Mast an Position [-340, -343] darf Hoehe 177.04 Meter haben
```

```
landkreis 3
Mast an Position [0, 0] darf Hoehe 451.57 Meter haben
Mast an Position [180, 570] darf Hoehe 393.79 Meter haben
Mast an Position [360, 1140] darf Hoehe 336.70 Meter haben
Mast an Position [540, 1710] darf Hoehe 280.74 Meter haben
Mast an Position [360, -120] darf Hoehe 444.62 Meter haben
Mast an Position [540, 450] darf Hoehe 385.71 Meter haben
Mast an Position [720, 1020] darf Hoehe 327.11 Meter haben
Mast an Position [900, 1590] darf Hoehe 269.02 Meter haben
Mast an Position [720, -240] darf Hoehe 440.84 Meter haben
Mast an Position [900, 330] darf Hoehe 381.25 Meter haben
Mast an Position [1080, 900] darf Hoehe 321.73 Meter haben
Mast an Position [1260, 1470] darf Hoehe 262.32 Meter haben
Mast an Position [1080, -360] darf Hoehe 440.31 Meter haben
Mast an Position [1260, 210] darf Hoehe 380.54 Meter haben
Mast an Position [1440, 780] darf Hoehe 320.78 Meter haben
Mast an Position [1620, 1350] darf Hoehe 261.02 Meter haben
```

```
landkreis 4
Mast an Position [-4147, 8575] darf Hoehe 0.00 Meter haben
Mast an Position [-6453, 14307] darf Hoehe 383.81 Meter haben
Mast an Position [-8370, 5831] darf Hoehe 262.45 Meter haben
Mast an Position [13045, -5404] darf Hoehe 233.99 Meter haben
Mast an Position [-8361, 8131] darf Hoehe 296.19 Meter haben
Mast an Position [-6963, -371] darf Hoehe 71.76 Meter haben
Mast an Position [9772, -3239] darf Hoehe 181.41 Meter haben
Mast an Position [-5102, -1726] darf Hoehe 235.40 Meter haben
Mast an Position [13454, 11822] darf Hoehe 343.11 Meter haben
Mast an Position [-7427, 1720] darf Hoehe 177.90 Meter haben
Mast an Position [-7816, 12396] darf Hoehe 449.16 Meter haben
Mast an Position [-11095, 603] darf Hoehe 408.03 Meter haben
Mast an Position [8314, 16301] darf Hoehe 317.95 Meter haben
Mast an Position [15283, -2961] darf Hoehe 221.29 Meter haben
Mast an Position [7082, 18552] darf Hoehe 520.12 Meter haben
Mast an Position [16743, 2687] darf Hoehe 394.71 Meter haben
Mast an Position [17511, -730] darf Hoehe 433.25 Meter haben
Mast an Position [-10767, 12860] darf Hoehe 703.83 Meter haben
Mast an Position [1508, -8030] darf Hoehe 168.42 Meter haben
Mast an Position [-7767, 982] darf Hoehe 201.27 Meter haben
Mast an Position [1277, -11294] darf Hoehe 139.16 Meter haben
Mast an Position [-8724, 3575] darf Hoehe 348.99 Meter haben
Mast an Position [7033, -7766] darf Hoehe 297.91 Meter haben
Mast an Position [2720, -10910] darf Hoehe 110.23 Meter haben
Mast an Position [20589, 7265] darf Hoehe 813.60 Meter haben
Mast an Position [-3214, 15263] darf Hoehe 236.19 Meter haben
Mast an Position [6887, 17263] darf Hoehe 391.94 Meter haben
Mast an Position [-3944, 13584] darf Hoehe 125.78 Meter haben
Mast an Position [6576, 15697] darf Hoehe 241.01 Meter haben
Mast an Position [-12074, 5974] darf Hoehe 625.40 Meter haben
```
