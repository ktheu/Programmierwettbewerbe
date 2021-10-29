## Dokumentation zur Aufgabe Buecherregal

### Lösungsidee

Die Bücher werden nach Höhen sortiert in einer Liste gespeichert.
Dann werden daraus Abschnitte = (Teillisten) mit Büchern gebildet, die
eine Höhendifferenz <= 3cm haben. Ist die Anzahl der verfügbaren Figuren
mindestens so groß wie die Anzahl der Abschnitte - 1,
so ist eine Aufstellung möglich.

### Umsetzung

Die Lösungsidee wird in ein Programm der Sprache Python umgesetzt.
Die Höhen der Bücher sind in mm angegeben. Wir lesen die Höhen in eine Liste buecher ein.
Wir erläutern die Umsetzung an einem einfachen Beispiel:

```
buecher = [50,10,60,90,100,110,70]
```

Mit

```
buecher.sort()
```

erhalten wir eine nach Höhe sortierte Bücherliste:

```
[10,50,60,70,90,100,110]
```

Wir intialisieren eine Liste _abschnitt_ für den aktuellen Abschnitt und eine Liste _regal_
für die Liste aller Abschnitte und setzen die Höhe des ersten Abschnitts auf die Höhe des ersten
Elements der sortierten Liste _buecher_

```
regal = []                                # eine Liste mit abschnitten
abschnitt = []                            # der aktuelle abschnitt
abschnitt_starthoehe = buecher[0]         # starthöhe des aktuellen abschnitts
```

Jetzt gehen wir durch die Liste _buecher_ und fügen Bücherhöhen zu den Abschnitten hinzu oder bilden
neue Abschnitte, wenn die Höhe eines Buches > 30 + Starthöhe des Abschnitts ist.

```
for b in buecher:
    if b - abschnitt_starthoehe <= 30:    # wenn Buchhöhe - starthoehe des abschnitts < 3cm
        abschnitt.append(b)               #   dann kommt das Buch in den abschnitt
    else:
        regal.append(abschnitt)           # sonst wird der bisherige abschnitt abgeschlossen und dem regal zugefügt
        abschnitt = [b]                   # ein neuer Abschnitt mit dem aktuellen Buch wird eröffnet
        abschnitt_starthoehe = b          # dieses erste Buch des Abschnitt bestimmt die starthoehe
```

Im Beispiel hat die Liste _regal_ die folgende Gestalt:

```
[[10], [50, 60, 70], [90, 100, 110]]
```

Jetzt überprüfen wir, ob die Anzahl der verfügbaren Figuren mindestens so groß
ist wie len(regal)-1. Dann ist eine Aufstellung möglich. Die Aufstellung
speichern wir in einer Liste _aufstellung_. Im Beispiel hat _aufstellung_ die
folgende Gestalt:

```
[10, 'Figur', 50, 60, 70, 'Figur', 90, 100, 110, 'Figur']
```

Die letzte Figur können wir weglassen und mit dem \*-Operator im print-Befehl
erhalten wir die folgende Aufstellung:

```
10 Figur 50 60 70 Figur 90 100 110
```

### Beispiele

Unser Programm liefert für die Beispieldaten folgende Ergebnisse:

```
# buecherregal1.txt
Eine Aufstellung mit 4 Figuren ist möglich:
168 170 Figur 202 211 229 Figur 233 254 260 Figur 272 Figur 306 307
```

```
# buecherregal2.txt
Eine Aufstellung mit 2 Figuren ist möglich:
169 175 Figur 203 209 210 229 Figur 235
```

```
# buecherregal3.txt
Eine Aufstellung mit 2 Figuren ist nicht möglich
```

```
# buecherregal4.txt
Eine Aufstellung mit 4 Figuren ist möglich:
160 160 161 161 162 165 165 166 167 167 167 169 170 170 171 173 173 174 174 177 180 182 183 184 184 185 185 187 188 189 190 Figur 196 197 197 199 200 201 202 206 207 207 211 212 212 214 215 216 217 218 219 224 225 Figur 233 235 237 238 238 239 240 240 240 245 246 246 247 253 254 256 258 259 259 261 Figur 264 266 266 267 268 270 270 272 274 275 276 277 278 279 286 286 287 288 289 290 293 293 Figur 295 296 300 301 303 304

```
