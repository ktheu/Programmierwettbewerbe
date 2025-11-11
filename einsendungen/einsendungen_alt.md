## Einsendungen

Auf den bwinf-Seiten Hinweise zu

- Form und Inhalt der Einsendungen [hier](https://bwinf.de/bundeswettbewerb/einsenden/)
- Vorlagen für die Dokumentationen [hier](https://bwinf.de/bundeswettbewerb/teilnehmen/vorlagen/)


### Dokumentation

Ich wiederhole hier die Hinweise aus den Vorlagen. Die Dokumentation soll in etwa folgendem Aufbau haben:

##### Kopf 

Junioraufgabe 1: Bücherregal <br>
Team-ID: 12345 <br>
Team-Name: MyTeam <br>
Bearbeiter/-innen dieser Aufgabe: Lena Müller, Malte Riedberg <br>
Datum: 10. November 2017

##### Lösungsidee

Die Idee der Lösung sollte hieraus vollkommen ersichtlich werden, ohne dass auf die eigentliche Implementierung Bezug genommen wird.

##### Umsetzung

Hier wird kurz erläutert, wie die Lösungsidee im Programm tatsächlich umgesetzt wurde. Hier können auch Implementierungsdetails erwähnt werden. Es muss nicht auf jede Einzelheit des Programms eingegangen werden, sondern nur auf die wichtigsten Aspekte, die für das Verständnis der Lösung notwendig sind.


##### Werkzeuge

Dokumentiere alle von dir verwendeten Werkzeuge. Das können Libraries, ILP-Solver, KI (z.B. ChatGPT-5, GitHub Copilot v1.100, ...) und Ähnliches sein. Zusätzlich zur Nennung solltest du hier auch deine Vorgehensweise dokumentieren: : Beschreibe, für welche Teile deiner Bearbeitung du welche Tools verwendet hast und wie du dabei vorgegangen bist (Arbeitsschritte, gemachte Anpassungen, ...).
Wenn du keine Werkzeuge verwendet hast, kannst du in diesen Abschnitt zumindest hinschreiben, welche Entwicklungsumgebung du benutzt hast (z.B. VSCode, PyCharm, JupyterLab, Thonny, Blockly-Umgebung).

##### Beispiele

Hier sollten die Ergebnisse für alle bwinf-Beispiele aufgelistet werden.
Es wird immer gerne gesehen, wenn weitere eigene Beispiele angefügt werden. Dieser Abschnitt darf auf keinen Fall fehlen!

##### Quellcode

Unbedingt darauf achten, dass der Quellcode gut dokumentiert ist. Sinnvolle Variablennamen
verwenden. Gegebenenfalls den Funktionen einen docstring mit Beispielen verpassen.
Zeilenkommentare werden gerne gesehen. Wenn das Programm sehr lang ist, sollten die unwichtigen Teile hier nicht abgedruckt werden. Dieser Teil sollte nicht mehr als 2–3 Seiten umfassen, maximal 10.


------

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

------



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












