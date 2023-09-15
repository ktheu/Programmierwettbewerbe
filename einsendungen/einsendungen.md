## Einsendungen

Hinweise zu Format und Inhalt der Einsendungen finden sich [hier](https://bwinf.de/bundeswettbewerb/tipps/#c5970)
Dort finden sich auch Beispiellösungen aus früheren Wettbewerben.

### Beispiel

Das Beispiel zeigt, wie eine Dokumentation mit einem Jupyter-Notebook aussehen kann.
Das fertige Notebook wird dazu im PDF-Format ausgedruckt. 
Ein Seitenvorschub beim pdf-Druck wird erzeugt durch eine Markup-Zelle mit:

```
<div style="page-break-after: always;"></div>
```

[Notebook zur Dokumentation](buecherregal_docu.ipynb)

[Dokumentation als PDF](buecherregal_einsendung.pdf)
 

Falls im Browser ein Markdown-Viewer und ein pdf-Drucker installiert ist, kann die Dokumentation auch mit
Markdown erstellt werden. Markdown-Dateien haben die Endung .md .

Einfache Markdown-Vorlage

```
# Junioraufgabe 1: Bücherregal

### Team-ID: 12345

### Team-Name: MyTeam

### Bearbeiter/-innen dieser Aufgabe: Lena Müller, Malte Riedberg

Datum: 10. November 2017

### Lösungsidee

Hier sollen die wichtigsten Schritte beschrieben werden, die zur Lösung führen. 
Hier werden keine technische Details erwähnt, es sollten also keine Namen von 
verwendeten Funktionen etc. auftauchen. Dieser Absatz muss nicht lange sein,
aber er sollte die wichtigsten Ideen darstellen, die für die Lösung führen.

### Umsetzung

Erster Satz: Die Lösungsidee wird in ein Programm der Sprache Python umgesetzt.
Dann sollten der Programmablauf und die wichtigsten Funktionen erläutert werden. 

### Beispiele

Hier sollten die Ergebnisse für alle bwinf-Beispiele aufgelistet werden.
Es wird immer gerne gesehen, wenn weitere eigene Beispiele angefügt werden. 


### Quellcode

Unbedingt darauf achten, dass der Quellcode gut dokumentiert ist. Sinnvolle Variablennamen
verwenden, den Funktionen einen docstring verpassen, am besten mit Beispielen.
Sinnvolle Abschnitte mit Kommentaren, gegebenfalls Zeilenkommentare verwenden.



```

Code-Beispiele oder Ausgaben in drei Backticks einschließen: ```

Ein Seitenvorschub beim pdf-Druck wird erzeugt durch:

```
<div style="page-break-after: always;"></div>
```





