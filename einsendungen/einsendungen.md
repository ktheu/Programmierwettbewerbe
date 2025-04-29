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
Hier werden keine technische Details erläutert. Es dürfen aber, wenn es für die Beschreibung nützlich ist, 
abkürzende Variablennamen verwendet werden. 

##### Umsetzung

Erster Satz: Die Lösungsidee wird in ein Programm der Sprache Python umgesetzt.
Dann sollten der Programmablauf und die wichtigsten Funktionen erläutert werden. 

##### Beispiele

Hier sollten die Ergebnisse für alle bwinf-Beispiele aufgelistet werden.
Es wird immer gerne gesehen, wenn weitere eigene Beispiele angefügt werden. Die
Ausgabe wird in dreifache Backticks eingeschlossen

```
Beispieldatei: beispiel0.txt
Anzahl: 23
```


##### Quellcode

Unbedingt darauf achten, dass der Quellcode gut dokumentiert ist. Sinnvolle Variablennamen
verwenden. Gegebenenfalls den Funktionen einen docstring mit Beispielen verpassen.
Zeilenkommentare werden gerne gesehen.

### Dokumentation mit JupyterLab

Wir können die Dokumentation auch mit JupyterLab erstellen. Die Notebooks sind gut dafür
geeignet, Texte, Bilder, Code und Programmausgaben in einem Dokument zusammenzufassen.

Nur beim Umwandeln ins PDF-Format müssen wir einige Dinge beachten:
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



### Dateiformat

Abgegeben wird eine zip-Datei, z.B. *einsendung.zip* mit folgendem Inhalt. Die Beispieldaten werden
ggf um eigene Beispieldaten ergänzt.


```
Junioraufgabe1.pdf
Junioraufgabe2.pdf
Aufgabe2.pdf
Junioraufgabe1 (Ordner)
    junioraufgabe1.py
    beispieldaten (Ordner)
        beispieldaten1.txt     
        beispieldaten2.txt  
        ...  

Junioraufgabe2 (Ordner)
    junioraufgabe2.py
    beispieldaten (Ordner)
        beispieldaten1.txt     
        beispieldaten2.txt  
        ...  
Aufgabe2 (Ordner)
    aufgabe2.py
    beispieldaten (Ordner)
        beispieldaten1.txt     
        beispieldaten2.txt  

```












