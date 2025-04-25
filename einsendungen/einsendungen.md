## Einsendungen

Hinweise zu Format und Inhalt der Einsendungen finden sich [hier](https://bwinf.de/bundeswettbewerb/tipps/#c5970)
Dort finden sich auch Beispiellösungen aus früheren Wettbewerben.

In der Regel haben die Einsendungen fünf Abschnitte: 


##### Kopf 

Junioraufgabe 1: Bücherregal <br>
Team-ID: 12345 <br>
Team-Name: MyTeam <br>
Bearbeiter/-innen dieser Aufgabe: Lena Müller, Malte Riedberg <br>
Datum: 10. November 2017

##### Lösungsidee

Hier sollen die wichtigsten Schritte beschrieben werden, die zur Lösung führen. 
Hier werden keine technische Details erwähnt, es sollten also keine Namen von 
verwendeten Funktionen etc. auftauchen. Dieser Absatz muss nicht lange sein,
aber er sollte die wichtigsten Ideen darstellen, die zur Lösung führen.

##### Umsetzung

Erster Satz: Die Lösungsidee wird in ein Programm der Sprache Python umgesetzt.
Dann sollten der Programmablauf und die wichtigsten Funktionen erläutert werden. 

##### Beispiele

Hier sollten die Ergebnisse für alle bwinf-Beispiele aufgelistet werden.
Es wird immer gerne gesehen, wenn weitere eigene Beispiele angefügt werden. 


##### Quellcode

Unbedingt darauf achten, dass der Quellcode gut dokumentiert ist. Sinnvolle Variablennamen
verwenden. Gegebenenfalls den Funktionen einen docstring mit Beispielen verpassen.
Zeilenkommentare werden gerne gesehen.

### Beispiel

Das Beispiel zeigt, wie eine Dokumentation mit einem Jupyter-Notebook aussehen kann.
Das Notebook wird über die Auswahl File-Print gedruckt. Als Ziel wird kein Drucker ausgewählt, sondern: als PDF speichern. Wenn Output-Zeilen oder Code-Zeilen lang sind, empfiehlt sich der Ausdruck im Querformat.
In der Vorschau kontrollieren wir, ob die Seitenvorschübe sinnvoll eingefügt sind.
Gegebenenfalls können wir in einer Markup-Zelle einen Seitenvorschub erzeugen mit:

```
<div style="page-break-after: always;"></div>
```

Hinweis: Bilder, die mit dem image-tag in das Notebook eingebettet sind, werden bei dieser Vorgehensweise
nicht ins PDF übernommen. Wenn wir Skizzen, die wir als Bild gespeichert haben, mit ins PDF aufnehmen wollen,
müssen wir diese Bilder mit einer Python-Anweisung im Notebook zeigen.

```
from IPython.display import Image, display               
display(Image(filename='skizze.png', width=600))
```

Den Output der Programme fügen wir in eine Markdown-Zelle ein. Damit die Ausgaben kein Fließtext werden, müssen wir sie in dreifache Backticks einschließen: \`\`\` 




[Notebook zur Dokumentation](buecherregal_docu.ipynb)

[Dokumentation als PDF](buecherregal_einsendung.pdf)


### Dateiformat

Abgegeben wird eine zip-Datei, z.B. *einsendung.zip* mit folgendem Inhalt. Die Beispieldaten werden
ggf um eigene Beispieldaten ergänzt.


```
Junioraufgabe1.pdf
Junioraufgabe2.pdf
Aufgabe2.pdf
Junioraufgabe1 (Ordner)
    junioraufgabe1.py
    beispieldaten1.txt ...                
Junioraufgabe2 (Ordner)
    junioraufgabe2.py
    beispieldaten1.txt ...  
Aufgabe2 (Ordner)
    aufgabe2.py
    beispieldaten1.txt ...  

```












