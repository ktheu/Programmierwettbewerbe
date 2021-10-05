## Parallelen


38\. Jugendwettbewerb Informatik - J1

[Aufgabenstellung](./aufgabenstellung.png) - 
[Lösungshinweise](./parallelen_loesung.pdf) -
[Beispieldaten](./beispieldaten.md)


#### Python

```
import re

f = open('./beispieldaten/parallelen.txt',encoding='utf-8')
daten = [s.strip() for s in f.readlines() if len(s.strip()) > 0]    # ohne Leerzeilen

laengeGedicht = len(daten)
print('Das Gedicht hat {} Zeilen.'.format(laengeGedicht))

regex = r'[^a-zA-ZßäüöÄÜÖ\s]'    # kein deutscher Buchstabe oder whitesplace
daten = [re.sub(regex,'',s).strip() for s in daten]

ersteHaelfte = [daten[i] for i in range(len(daten)//2)]

worte1 = []
for zeile in ersteHaelfte:
    worte1.extend(zeile.split())

worte = []
for zeile in daten:
    worte.extend(zeile.split())

def doit(worte,i):
  print('----- start mit wortnr = {}'.format(i))
  n = len(worte)
  wort = worte[i]
  print('nr = {}, wort = {}, laenge = {}'.format(i,wort,len(wort)))
  while i+len(wort) < len(worte):
    i = i + len(wort)
    wort = worte[i]
    print('nr = {}, wort = {}, laenge = {}'.format(i,wort,len(wort)))
  return wort

for i in range(len(worte1)):
  s = doit(worte,i)
  print(s)
```

Ausgabe:

```
Das Gedicht hat 20 Zeilen.
----- start mit wortnr = 0
nr = 0, wort = Es, laenge = 2
nr = 2, wort = zwei, laenge = 4
nr = 6, wort = hinaus, laenge = 6
nr = 12, wort = solidem, laenge = 7
nr = 19, wort = bis, laenge = 3
nr = 22, wort = seliges, laenge = 7
nr = 29, wort = beiden, laenge = 6
nr = 35, wort = als, laenge = 3
nr = 38, wort = Lichtjahre, laenge = 10
nr = 48, wort = nicht, laenge = 5
nr = 53, wort = Warn, laenge = 4
nr = 57, wort = Sie, laenge = 3
nr = 60, wort = nicht, laenge = 5
nr = 65, wort = zwei, laenge = 4
nr = 69, wort = ewiges, laenge = 6
nr = 75, wort = sie, laenge = 3
nr = 78, wort = sie, laenge = 3
nr = 81, wort = ihm, laenge = 3
nr = 84, wort = verschlang, laenge = 10
verschlang
----- start mit wortnr = 1
nr = 1, wort = gingen, laenge = 6
nr = 7, wort = zwei, laenge = 4
nr = 11, wort = aus, laenge = 3
nr = 14, wort = Sie, laenge = 3
nr = 17, wort = nicht, laenge = 5
nr = 22, wort = seliges, laenge = 7
nr = 29, wort = beiden, laenge = 6
nr = 35, wort = als, laenge = 3
nr = 38, wort = Lichtjahre, laenge = 10
nr = 48, wort = nicht, laenge = 5
nr = 53, wort = Warn, laenge = 4
nr = 57, wort = Sie, laenge = 3
nr = 60, wort = nicht, laenge = 5
nr = 65, wort = zwei, laenge = 4
nr = 69, wort = ewiges, laenge = 6
nr = 75, wort = sie, laenge = 3
nr = 78, wort = sie, laenge = 3
nr = 81, wort = ihm, laenge = 3
nr = 84, wort = verschlang, laenge = 10
verschlang
----- start mit wortnr = 2
nr = 2, wort = zwei, laenge = 4
nr = 6, wort = hinaus, laenge = 6
nr = 12, wort = solidem, laenge = 7
nr = 19, wort = bis, laenge = 3
nr = 22, wort = seliges, laenge = 7
nr = 29, wort = beiden, laenge = 6
nr = 35, wort = als, laenge = 3
nr = 38, wort = Lichtjahre, laenge = 10
nr = 48, wort = nicht, laenge = 5
nr = 53, wort = Warn, laenge = 4
nr = 57, wort = Sie, laenge = 3
nr = 60, wort = nicht, laenge = 5
nr = 65, wort = zwei, laenge = 4
nr = 69, wort = ewiges, laenge = 6
nr = 75, wort = sie, laenge = 3
nr = 78, wort = sie, laenge = 3
nr = 81, wort = ihm, laenge = 3
nr = 84, wort = verschlang, laenge = 10
verschlang
----- start mit wortnr = 3
nr = 3, wort = Parallelen, laenge = 10
nr = 13, wort = Haus, laenge = 4
nr = 17, wort = nicht, laenge = 5
nr = 22, wort = seliges, laenge = 7
nr = 29, wort = beiden, laenge = 6
nr = 35, wort = als, laenge = 3
nr = 38, wort = Lichtjahre, laenge = 10
nr = 48, wort = nicht, laenge = 5
nr = 53, wort = Warn, laenge = 4
nr = 57, wort = Sie, laenge = 3
nr = 60, wort = nicht, laenge = 5
nr = 65, wort = zwei, laenge = 4
nr = 69, wort = ewiges, laenge = 6
nr = 75, wort = sie, laenge = 3
nr = 78, wort = sie, laenge = 3
nr = 81, wort = ihm, laenge = 3
nr = 84, wort = verschlang, laenge = 10
verschlang
----- start mit wortnr = 4
nr = 4, wort = ins, laenge = 3
nr = 7, wort = zwei, laenge = 4
nr = 11, wort = aus, laenge = 3
nr = 14, wort = Sie, laenge = 3
nr = 17, wort = nicht, laenge = 5
nr = 22, wort = seliges, laenge = 7
nr = 29, wort = beiden, laenge = 6
nr = 35, wort = als, laenge = 3
nr = 38, wort = Lichtjahre, laenge = 10
nr = 48, wort = nicht, laenge = 5
nr = 53, wort = Warn, laenge = 4
nr = 57, wort = Sie, laenge = 3
nr = 60, wort = nicht, laenge = 5
nr = 65, wort = zwei, laenge = 4
nr = 69, wort = ewiges, laenge = 6
nr = 75, wort = sie, laenge = 3
nr = 78, wort = sie, laenge = 3
nr = 81, wort = ihm, laenge = 3
nr = 84, wort = verschlang, laenge = 10
verschlang
----- start mit wortnr = 5
nr = 5, wort = Endlose, laenge = 7
nr = 12, wort = solidem, laenge = 7
nr = 19, wort = bis, laenge = 3
nr = 22, wort = seliges, laenge = 7
nr = 29, wort = beiden, laenge = 6
nr = 35, wort = als, laenge = 3
nr = 38, wort = Lichtjahre, laenge = 10
nr = 48, wort = nicht, laenge = 5
nr = 53, wort = Warn, laenge = 4
nr = 57, wort = Sie, laenge = 3
nr = 60, wort = nicht, laenge = 5
nr = 65, wort = zwei, laenge = 4
nr = 69, wort = ewiges, laenge = 6
nr = 75, wort = sie, laenge = 3
nr = 78, wort = sie, laenge = 3
nr = 81, wort = ihm, laenge = 3
nr = 84, wort = verschlang, laenge = 10
verschlang
----- start mit wortnr = 6
nr = 6, wort = hinaus, laenge = 6
nr = 12, wort = solidem, laenge = 7
nr = 19, wort = bis, laenge = 3
nr = 22, wort = seliges, laenge = 7
nr = 29, wort = beiden, laenge = 6
nr = 35, wort = als, laenge = 3
nr = 38, wort = Lichtjahre, laenge = 10
nr = 48, wort = nicht, laenge = 5
nr = 53, wort = Warn, laenge = 4
nr = 57, wort = Sie, laenge = 3
nr = 60, wort = nicht, laenge = 5
nr = 65, wort = zwei, laenge = 4
nr = 69, wort = ewiges, laenge = 6
nr = 75, wort = sie, laenge = 3
nr = 78, wort = sie, laenge = 3
nr = 81, wort = ihm, laenge = 3
nr = 84, wort = verschlang, laenge = 10
verschlang
----- start mit wortnr = 7
nr = 7, wort = zwei, laenge = 4
nr = 11, wort = aus, laenge = 3
nr = 14, wort = Sie, laenge = 3
nr = 17, wort = nicht, laenge = 5
nr = 22, wort = seliges, laenge = 7
nr = 29, wort = beiden, laenge = 6
nr = 35, wort = als, laenge = 3
nr = 38, wort = Lichtjahre, laenge = 10
nr = 48, wort = nicht, laenge = 5
nr = 53, wort = Warn, laenge = 4
nr = 57, wort = Sie, laenge = 3
nr = 60, wort = nicht, laenge = 5
nr = 65, wort = zwei, laenge = 4
nr = 69, wort = ewiges, laenge = 6
nr = 75, wort = sie, laenge = 3
nr = 78, wort = sie, laenge = 3
nr = 81, wort = ihm, laenge = 3
nr = 84, wort = verschlang, laenge = 10
verschlang
----- start mit wortnr = 8
nr = 8, wort = kerzengerade, laenge = 12
nr = 20, wort = an, laenge = 2
nr = 22, wort = seliges, laenge = 7
nr = 29, wort = beiden, laenge = 6
nr = 35, wort = als, laenge = 3
nr = 38, wort = Lichtjahre, laenge = 10
nr = 48, wort = nicht, laenge = 5
nr = 53, wort = Warn, laenge = 4
nr = 57, wort = Sie, laenge = 3
nr = 60, wort = nicht, laenge = 5
nr = 65, wort = zwei, laenge = 4
nr = 69, wort = ewiges, laenge = 6
nr = 75, wort = sie, laenge = 3
nr = 78, wort = sie, laenge = 3
nr = 81, wort = ihm, laenge = 3
nr = 84, wort = verschlang, laenge = 10
verschlang
----- start mit wortnr = 9
nr = 9, wort = Seelen, laenge = 6
nr = 15, wort = wollten, laenge = 7
nr = 22, wort = seliges, laenge = 7
nr = 29, wort = beiden, laenge = 6
nr = 35, wort = als, laenge = 3
nr = 38, wort = Lichtjahre, laenge = 10
nr = 48, wort = nicht, laenge = 5
nr = 53, wort = Warn, laenge = 4
nr = 57, wort = Sie, laenge = 3
nr = 60, wort = nicht, laenge = 5
nr = 65, wort = zwei, laenge = 4
nr = 69, wort = ewiges, laenge = 6
nr = 75, wort = sie, laenge = 3
nr = 78, wort = sie, laenge = 3
nr = 81, wort = ihm, laenge = 3
nr = 84, wort = verschlang, laenge = 10
verschlang
----- start mit wortnr = 10
nr = 10, wort = und, laenge = 3
nr = 13, wort = Haus, laenge = 4
nr = 17, wort = nicht, laenge = 5
nr = 22, wort = seliges, laenge = 7
nr = 29, wort = beiden, laenge = 6
nr = 35, wort = als, laenge = 3
nr = 38, wort = Lichtjahre, laenge = 10
nr = 48, wort = nicht, laenge = 5
nr = 53, wort = Warn, laenge = 4
nr = 57, wort = Sie, laenge = 3
nr = 60, wort = nicht, laenge = 5
nr = 65, wort = zwei, laenge = 4
nr = 69, wort = ewiges, laenge = 6
nr = 75, wort = sie, laenge = 3
nr = 78, wort = sie, laenge = 3
nr = 81, wort = ihm, laenge = 3
nr = 84, wort = verschlang, laenge = 10
verschlang
----- start mit wortnr = 11
nr = 11, wort = aus, laenge = 3
nr = 14, wort = Sie, laenge = 3
nr = 17, wort = nicht, laenge = 5
nr = 22, wort = seliges, laenge = 7
nr = 29, wort = beiden, laenge = 6
nr = 35, wort = als, laenge = 3
nr = 38, wort = Lichtjahre, laenge = 10
nr = 48, wort = nicht, laenge = 5
nr = 53, wort = Warn, laenge = 4
nr = 57, wort = Sie, laenge = 3
nr = 60, wort = nicht, laenge = 5
nr = 65, wort = zwei, laenge = 4
nr = 69, wort = ewiges, laenge = 6
nr = 75, wort = sie, laenge = 3
nr = 78, wort = sie, laenge = 3
nr = 81, wort = ihm, laenge = 3
nr = 84, wort = verschlang, laenge = 10
verschlang
----- start mit wortnr = 12
nr = 12, wort = solidem, laenge = 7
nr = 19, wort = bis, laenge = 3
nr = 22, wort = seliges, laenge = 7
nr = 29, wort = beiden, laenge = 6
nr = 35, wort = als, laenge = 3
nr = 38, wort = Lichtjahre, laenge = 10
nr = 48, wort = nicht, laenge = 5
nr = 53, wort = Warn, laenge = 4
nr = 57, wort = Sie, laenge = 3
nr = 60, wort = nicht, laenge = 5
nr = 65, wort = zwei, laenge = 4
nr = 69, wort = ewiges, laenge = 6
nr = 75, wort = sie, laenge = 3
nr = 78, wort = sie, laenge = 3
nr = 81, wort = ihm, laenge = 3
nr = 84, wort = verschlang, laenge = 10
verschlang
----- start mit wortnr = 13
nr = 13, wort = Haus, laenge = 4
nr = 17, wort = nicht, laenge = 5
nr = 22, wort = seliges, laenge = 7
nr = 29, wort = beiden, laenge = 6
nr = 35, wort = als, laenge = 3
nr = 38, wort = Lichtjahre, laenge = 10
nr = 48, wort = nicht, laenge = 5
nr = 53, wort = Warn, laenge = 4
nr = 57, wort = Sie, laenge = 3
nr = 60, wort = nicht, laenge = 5
nr = 65, wort = zwei, laenge = 4
nr = 69, wort = ewiges, laenge = 6
nr = 75, wort = sie, laenge = 3
nr = 78, wort = sie, laenge = 3
nr = 81, wort = ihm, laenge = 3
nr = 84, wort = verschlang, laenge = 10
verschlang
----- start mit wortnr = 14
nr = 14, wort = Sie, laenge = 3
nr = 17, wort = nicht, laenge = 5
nr = 22, wort = seliges, laenge = 7
nr = 29, wort = beiden, laenge = 6
nr = 35, wort = als, laenge = 3
nr = 38, wort = Lichtjahre, laenge = 10
nr = 48, wort = nicht, laenge = 5
nr = 53, wort = Warn, laenge = 4
nr = 57, wort = Sie, laenge = 3
nr = 60, wort = nicht, laenge = 5
nr = 65, wort = zwei, laenge = 4
nr = 69, wort = ewiges, laenge = 6
nr = 75, wort = sie, laenge = 3
nr = 78, wort = sie, laenge = 3
nr = 81, wort = ihm, laenge = 3
nr = 84, wort = verschlang, laenge = 10
verschlang
----- start mit wortnr = 15
nr = 15, wort = wollten, laenge = 7
nr = 22, wort = seliges, laenge = 7
nr = 29, wort = beiden, laenge = 6
nr = 35, wort = als, laenge = 3
nr = 38, wort = Lichtjahre, laenge = 10
nr = 48, wort = nicht, laenge = 5
nr = 53, wort = Warn, laenge = 4
nr = 57, wort = Sie, laenge = 3
nr = 60, wort = nicht, laenge = 5
nr = 65, wort = zwei, laenge = 4
nr = 69, wort = ewiges, laenge = 6
nr = 75, wort = sie, laenge = 3
nr = 78, wort = sie, laenge = 3
nr = 81, wort = ihm, laenge = 3
nr = 84, wort = verschlang, laenge = 10
verschlang
----- start mit wortnr = 16
nr = 16, wort = sich, laenge = 4
nr = 20, wort = an, laenge = 2
nr = 22, wort = seliges, laenge = 7
nr = 29, wort = beiden, laenge = 6
nr = 35, wort = als, laenge = 3
nr = 38, wort = Lichtjahre, laenge = 10
nr = 48, wort = nicht, laenge = 5
nr = 53, wort = Warn, laenge = 4
nr = 57, wort = Sie, laenge = 3
nr = 60, wort = nicht, laenge = 5
nr = 65, wort = zwei, laenge = 4
nr = 69, wort = ewiges, laenge = 6
nr = 75, wort = sie, laenge = 3
nr = 78, wort = sie, laenge = 3
nr = 81, wort = ihm, laenge = 3
nr = 84, wort = verschlang, laenge = 10
verschlang
----- start mit wortnr = 17
nr = 17, wort = nicht, laenge = 5
nr = 22, wort = seliges, laenge = 7
nr = 29, wort = beiden, laenge = 6
nr = 35, wort = als, laenge = 3
nr = 38, wort = Lichtjahre, laenge = 10
nr = 48, wort = nicht, laenge = 5
nr = 53, wort = Warn, laenge = 4
nr = 57, wort = Sie, laenge = 3
nr = 60, wort = nicht, laenge = 5
nr = 65, wort = zwei, laenge = 4
nr = 69, wort = ewiges, laenge = 6
nr = 75, wort = sie, laenge = 3
nr = 78, wort = sie, laenge = 3
nr = 81, wort = ihm, laenge = 3
nr = 84, wort = verschlang, laenge = 10
verschlang
----- start mit wortnr = 18
nr = 18, wort = schneiden, laenge = 9
nr = 27, wort = einmal, laenge = 6
nr = 33, wort = Stab, laenge = 4
nr = 37, wort = zehn, laenge = 4
nr = 41, wort = sich, laenge = 4
nr = 45, wort = dem, laenge = 3
nr = 48, wort = nicht, laenge = 5
nr = 53, wort = Warn, laenge = 4
nr = 57, wort = Sie, laenge = 3
nr = 60, wort = nicht, laenge = 5
nr = 65, wort = zwei, laenge = 4
nr = 69, wort = ewiges, laenge = 6
nr = 75, wort = sie, laenge = 3
nr = 78, wort = sie, laenge = 3
nr = 81, wort = ihm, laenge = 3
nr = 84, wort = verschlang, laenge = 10
verschlang
----- start mit wortnr = 19
nr = 19, wort = bis, laenge = 3
nr = 22, wort = seliges, laenge = 7
nr = 29, wort = beiden, laenge = 6
nr = 35, wort = als, laenge = 3
nr = 38, wort = Lichtjahre, laenge = 10
nr = 48, wort = nicht, laenge = 5
nr = 53, wort = Warn, laenge = 4
nr = 57, wort = Sie, laenge = 3
nr = 60, wort = nicht, laenge = 5
nr = 65, wort = zwei, laenge = 4
nr = 69, wort = ewiges, laenge = 6
nr = 75, wort = sie, laenge = 3
nr = 78, wort = sie, laenge = 3
nr = 81, wort = ihm, laenge = 3
nr = 84, wort = verschlang, laenge = 10
verschlang
----- start mit wortnr = 20
nr = 20, wort = an, laenge = 2
nr = 22, wort = seliges, laenge = 7
nr = 29, wort = beiden, laenge = 6
nr = 35, wort = als, laenge = 3
nr = 38, wort = Lichtjahre, laenge = 10
nr = 48, wort = nicht, laenge = 5
nr = 53, wort = Warn, laenge = 4
nr = 57, wort = Sie, laenge = 3
nr = 60, wort = nicht, laenge = 5
nr = 65, wort = zwei, laenge = 4
nr = 69, wort = ewiges, laenge = 6
nr = 75, wort = sie, laenge = 3
nr = 78, wort = sie, laenge = 3
nr = 81, wort = ihm, laenge = 3
nr = 84, wort = verschlang, laenge = 10
verschlang
----- start mit wortnr = 21
nr = 21, wort = ihr, laenge = 3
nr = 24, wort = Das, laenge = 3
nr = 27, wort = einmal, laenge = 6
nr = 33, wort = Stab, laenge = 4
nr = 37, wort = zehn, laenge = 4
nr = 41, wort = sich, laenge = 4
nr = 45, wort = dem, laenge = 3
nr = 48, wort = nicht, laenge = 5
nr = 53, wort = Warn, laenge = 4
nr = 57, wort = Sie, laenge = 3
nr = 60, wort = nicht, laenge = 5
nr = 65, wort = zwei, laenge = 4
nr = 69, wort = ewiges, laenge = 6
nr = 75, wort = sie, laenge = 3
nr = 78, wort = sie, laenge = 3
nr = 81, wort = ihm, laenge = 3
nr = 84, wort = verschlang, laenge = 10
verschlang
----- start mit wortnr = 22
nr = 22, wort = seliges, laenge = 7
nr = 29, wort = beiden, laenge = 6
nr = 35, wort = als, laenge = 3
nr = 38, wort = Lichtjahre, laenge = 10
nr = 48, wort = nicht, laenge = 5
nr = 53, wort = Warn, laenge = 4
nr = 57, wort = Sie, laenge = 3
nr = 60, wort = nicht, laenge = 5
nr = 65, wort = zwei, laenge = 4
nr = 69, wort = ewiges, laenge = 6
nr = 75, wort = sie, laenge = 3
nr = 78, wort = sie, laenge = 3
nr = 81, wort = ihm, laenge = 3
nr = 84, wort = verschlang, laenge = 10
verschlang
----- start mit wortnr = 23
nr = 23, wort = Grab, laenge = 4
nr = 27, wort = einmal, laenge = 6
nr = 33, wort = Stab, laenge = 4
nr = 37, wort = zehn, laenge = 4
nr = 41, wort = sich, laenge = 4
nr = 45, wort = dem, laenge = 3
nr = 48, wort = nicht, laenge = 5
nr = 53, wort = Warn, laenge = 4
nr = 57, wort = Sie, laenge = 3
nr = 60, wort = nicht, laenge = 5
nr = 65, wort = zwei, laenge = 4
nr = 69, wort = ewiges, laenge = 6
nr = 75, wort = sie, laenge = 3
nr = 78, wort = sie, laenge = 3
nr = 81, wort = ihm, laenge = 3
nr = 84, wort = verschlang, laenge = 10
verschlang
----- start mit wortnr = 24
nr = 24, wort = Das, laenge = 3
nr = 27, wort = einmal, laenge = 6
nr = 33, wort = Stab, laenge = 4
nr = 37, wort = zehn, laenge = 4
nr = 41, wort = sich, laenge = 4
nr = 45, wort = dem, laenge = 3
nr = 48, wort = nicht, laenge = 5
nr = 53, wort = Warn, laenge = 4
nr = 57, wort = Sie, laenge = 3
nr = 60, wort = nicht, laenge = 5
nr = 65, wort = zwei, laenge = 4
nr = 69, wort = ewiges, laenge = 6
nr = 75, wort = sie, laenge = 3
nr = 78, wort = sie, laenge = 3
nr = 81, wort = ihm, laenge = 3
nr = 84, wort = verschlang, laenge = 10
verschlang
----- start mit wortnr = 25
nr = 25, wort = war, laenge = 3
nr = 28, wort = der, laenge = 3
nr = 31, wort = Stolz, laenge = 5
nr = 36, wort = sie, laenge = 3
nr = 39, wort = gewandert, laenge = 9
nr = 48, wort = nicht, laenge = 5
nr = 53, wort = Warn, laenge = 4
nr = 57, wort = Sie, laenge = 3
nr = 60, wort = nicht, laenge = 5
nr = 65, wort = zwei, laenge = 4
nr = 69, wort = ewiges, laenge = 6
nr = 75, wort = sie, laenge = 3
nr = 78, wort = sie, laenge = 3
nr = 81, wort = ihm, laenge = 3
nr = 84, wort = verschlang, laenge = 10
verschlang
----- start mit wortnr = 26
nr = 26, wort = nun, laenge = 3
nr = 29, wort = beiden, laenge = 6
nr = 35, wort = als, laenge = 3
nr = 38, wort = Lichtjahre, laenge = 10
nr = 48, wort = nicht, laenge = 5
nr = 53, wort = Warn, laenge = 4
nr = 57, wort = Sie, laenge = 3
nr = 60, wort = nicht, laenge = 5
nr = 65, wort = zwei, laenge = 4
nr = 69, wort = ewiges, laenge = 6
nr = 75, wort = sie, laenge = 3
nr = 78, wort = sie, laenge = 3
nr = 81, wort = ihm, laenge = 3
nr = 84, wort = verschlang, laenge = 10
verschlang
----- start mit wortnr = 27
nr = 27, wort = einmal, laenge = 6
nr = 33, wort = Stab, laenge = 4
nr = 37, wort = zehn, laenge = 4
nr = 41, wort = sich, laenge = 4
nr = 45, wort = dem, laenge = 3
nr = 48, wort = nicht, laenge = 5
nr = 53, wort = Warn, laenge = 4
nr = 57, wort = Sie, laenge = 3
nr = 60, wort = nicht, laenge = 5
nr = 65, wort = zwei, laenge = 4
nr = 69, wort = ewiges, laenge = 6
nr = 75, wort = sie, laenge = 3
nr = 78, wort = sie, laenge = 3
nr = 81, wort = ihm, laenge = 3
nr = 84, wort = verschlang, laenge = 10
verschlang
----- start mit wortnr = 28
nr = 28, wort = der, laenge = 3
nr = 31, wort = Stolz, laenge = 5
nr = 36, wort = sie, laenge = 3
nr = 39, wort = gewandert, laenge = 9
nr = 48, wort = nicht, laenge = 5
nr = 53, wort = Warn, laenge = 4
nr = 57, wort = Sie, laenge = 3
nr = 60, wort = nicht, laenge = 5
nr = 65, wort = zwei, laenge = 4
nr = 69, wort = ewiges, laenge = 6
nr = 75, wort = sie, laenge = 3
nr = 78, wort = sie, laenge = 3
nr = 81, wort = ihm, laenge = 3
nr = 84, wort = verschlang, laenge = 10
verschlang
----- start mit wortnr = 29
nr = 29, wort = beiden, laenge = 6
nr = 35, wort = als, laenge = 3
nr = 38, wort = Lichtjahre, laenge = 10
nr = 48, wort = nicht, laenge = 5
nr = 53, wort = Warn, laenge = 4
nr = 57, wort = Sie, laenge = 3
nr = 60, wort = nicht, laenge = 5
nr = 65, wort = zwei, laenge = 4
nr = 69, wort = ewiges, laenge = 6
nr = 75, wort = sie, laenge = 3
nr = 78, wort = sie, laenge = 3
nr = 81, wort = ihm, laenge = 3
nr = 84, wort = verschlang, laenge = 10
verschlang
----- start mit wortnr = 30
nr = 30, wort = geheimer, laenge = 8
nr = 38, wort = Lichtjahre, laenge = 10
nr = 48, wort = nicht, laenge = 5
nr = 53, wort = Warn, laenge = 4
nr = 57, wort = Sie, laenge = 3
nr = 60, wort = nicht, laenge = 5
nr = 65, wort = zwei, laenge = 4
nr = 69, wort = ewiges, laenge = 6
nr = 75, wort = sie, laenge = 3
nr = 78, wort = sie, laenge = 3
nr = 81, wort = ihm, laenge = 3
nr = 84, wort = verschlang, laenge = 10
verschlang
----- start mit wortnr = 31
nr = 31, wort = Stolz, laenge = 5
nr = 36, wort = sie, laenge = 3
nr = 39, wort = gewandert, laenge = 9
nr = 48, wort = nicht, laenge = 5
nr = 53, wort = Warn, laenge = 4
nr = 57, wort = Sie, laenge = 3
nr = 60, wort = nicht, laenge = 5
nr = 65, wort = zwei, laenge = 4
nr = 69, wort = ewiges, laenge = 6
nr = 75, wort = sie, laenge = 3
nr = 78, wort = sie, laenge = 3
nr = 81, wort = ihm, laenge = 3
nr = 84, wort = verschlang, laenge = 10
verschlang
----- start mit wortnr = 32
nr = 32, wort = und, laenge = 3
nr = 35, wort = als, laenge = 3
nr = 38, wort = Lichtjahre, laenge = 10
nr = 48, wort = nicht, laenge = 5
nr = 53, wort = Warn, laenge = 4
nr = 57, wort = Sie, laenge = 3
nr = 60, wort = nicht, laenge = 5
nr = 65, wort = zwei, laenge = 4
nr = 69, wort = ewiges, laenge = 6
nr = 75, wort = sie, laenge = 3
nr = 78, wort = sie, laenge = 3
nr = 81, wort = ihm, laenge = 3
nr = 84, wort = verschlang, laenge = 10
verschlang
----- start mit wortnr = 33
nr = 33, wort = Stab, laenge = 4
nr = 37, wort = zehn, laenge = 4
nr = 41, wort = sich, laenge = 4
nr = 45, wort = dem, laenge = 3
nr = 48, wort = nicht, laenge = 5
nr = 53, wort = Warn, laenge = 4
nr = 57, wort = Sie, laenge = 3
nr = 60, wort = nicht, laenge = 5
nr = 65, wort = zwei, laenge = 4
nr = 69, wort = ewiges, laenge = 6
nr = 75, wort = sie, laenge = 3
nr = 78, wort = sie, laenge = 3
nr = 81, wort = ihm, laenge = 3
nr = 84, wort = verschlang, laenge = 10
verschlang
----- start mit wortnr = 34
nr = 34, wort = Doch, laenge = 4
nr = 38, wort = Lichtjahre, laenge = 10
nr = 48, wort = nicht, laenge = 5
nr = 53, wort = Warn, laenge = 4
nr = 57, wort = Sie, laenge = 3
nr = 60, wort = nicht, laenge = 5
nr = 65, wort = zwei, laenge = 4
nr = 69, wort = ewiges, laenge = 6
nr = 75, wort = sie, laenge = 3
nr = 78, wort = sie, laenge = 3
nr = 81, wort = ihm, laenge = 3
nr = 84, wort = verschlang, laenge = 10
verschlang
----- start mit wortnr = 35
nr = 35, wort = als, laenge = 3
nr = 38, wort = Lichtjahre, laenge = 10
nr = 48, wort = nicht, laenge = 5
nr = 53, wort = Warn, laenge = 4
nr = 57, wort = Sie, laenge = 3
nr = 60, wort = nicht, laenge = 5
nr = 65, wort = zwei, laenge = 4
nr = 69, wort = ewiges, laenge = 6
nr = 75, wort = sie, laenge = 3
nr = 78, wort = sie, laenge = 3
nr = 81, wort = ihm, laenge = 3
nr = 84, wort = verschlang, laenge = 10
verschlang
----- start mit wortnr = 36
nr = 36, wort = sie, laenge = 3
nr = 39, wort = gewandert, laenge = 9
nr = 48, wort = nicht, laenge = 5
nr = 53, wort = Warn, laenge = 4
nr = 57, wort = Sie, laenge = 3
nr = 60, wort = nicht, laenge = 5
nr = 65, wort = zwei, laenge = 4
nr = 69, wort = ewiges, laenge = 6
nr = 75, wort = sie, laenge = 3
nr = 78, wort = sie, laenge = 3
nr = 81, wort = ihm, laenge = 3
nr = 84, wort = verschlang, laenge = 10
verschlang
----- start mit wortnr = 37
nr = 37, wort = zehn, laenge = 4
nr = 41, wort = sich, laenge = 4
nr = 45, wort = dem, laenge = 3
nr = 48, wort = nicht, laenge = 5
nr = 53, wort = Warn, laenge = 4
nr = 57, wort = Sie, laenge = 3
nr = 60, wort = nicht, laenge = 5
nr = 65, wort = zwei, laenge = 4
nr = 69, wort = ewiges, laenge = 6
nr = 75, wort = sie, laenge = 3
nr = 78, wort = sie, laenge = 3
nr = 81, wort = ihm, laenge = 3
nr = 84, wort = verschlang, laenge = 10
verschlang
----- start mit wortnr = 38
nr = 38, wort = Lichtjahre, laenge = 10
nr = 48, wort = nicht, laenge = 5
nr = 53, wort = Warn, laenge = 4
nr = 57, wort = Sie, laenge = 3
nr = 60, wort = nicht, laenge = 5
nr = 65, wort = zwei, laenge = 4
nr = 69, wort = ewiges, laenge = 6
nr = 75, wort = sie, laenge = 3
nr = 78, wort = sie, laenge = 3
nr = 81, wort = ihm, laenge = 3
nr = 84, wort = verschlang, laenge = 10
verschlang
----- start mit wortnr = 39
nr = 39, wort = gewandert, laenge = 9
nr = 48, wort = nicht, laenge = 5
nr = 53, wort = Warn, laenge = 4
nr = 57, wort = Sie, laenge = 3
nr = 60, wort = nicht, laenge = 5
nr = 65, wort = zwei, laenge = 4
nr = 69, wort = ewiges, laenge = 6
nr = 75, wort = sie, laenge = 3
nr = 78, wort = sie, laenge = 3
nr = 81, wort = ihm, laenge = 3
nr = 84, wort = verschlang, laenge = 10
verschlang
----- start mit wortnr = 40
nr = 40, wort = neben, laenge = 5
nr = 45, wort = dem, laenge = 3
nr = 48, wort = nicht, laenge = 5
nr = 53, wort = Warn, laenge = 4
nr = 57, wort = Sie, laenge = 3
nr = 60, wort = nicht, laenge = 5
nr = 65, wort = zwei, laenge = 4
nr = 69, wort = ewiges, laenge = 6
nr = 75, wort = sie, laenge = 3
nr = 78, wort = sie, laenge = 3
nr = 81, wort = ihm, laenge = 3
nr = 84, wort = verschlang, laenge = 10
verschlang
----- start mit wortnr = 41
nr = 41, wort = sich, laenge = 4
nr = 45, wort = dem, laenge = 3
nr = 48, wort = nicht, laenge = 5
nr = 53, wort = Warn, laenge = 4
nr = 57, wort = Sie, laenge = 3
nr = 60, wort = nicht, laenge = 5
nr = 65, wort = zwei, laenge = 4
nr = 69, wort = ewiges, laenge = 6
nr = 75, wort = sie, laenge = 3
nr = 78, wort = sie, laenge = 3
nr = 81, wort = ihm, laenge = 3
nr = 84, wort = verschlang, laenge = 10
verschlang
----- start mit wortnr = 42
nr = 42, wort = hin, laenge = 3
nr = 45, wort = dem, laenge = 3
nr = 48, wort = nicht, laenge = 5
nr = 53, wort = Warn, laenge = 4
nr = 57, wort = Sie, laenge = 3
nr = 60, wort = nicht, laenge = 5
nr = 65, wort = zwei, laenge = 4
nr = 69, wort = ewiges, laenge = 6
nr = 75, wort = sie, laenge = 3
nr = 78, wort = sie, laenge = 3
nr = 81, wort = ihm, laenge = 3
nr = 84, wort = verschlang, laenge = 10
verschlang
```