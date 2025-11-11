### Dokumentation mit JupyterLab

Eine Vorlage dazu findet ihr [hier](https://github.com/ktheu/Programmierwettbewerbe/blob/master/einsendungen/einsendung_muster.ipynb).

Ein Beispiel-Video mit einer etwas älteren Vorlage findet ihr [hier](https://www.youtube.com/watch?v=bp3aTa3aTYw).

Wer Probleme bei der Installation von JupyterLab hat, kann auch die Online-Umgebung
[CodingLabs](https://codinglabs-projekt.de/) verwenden.


Beim Umwandeln ins PDF-Format müssen wir einige Dinge beachten:
Das Notebook wird über die Auswahl File-Print gedruckt. Als Ziel wird kein Drucker ausgewählt, sondern: als PDF speichern. Wenn Output-Zeilen oder Code-Zeilen lang sind, empfiehlt sich der Ausdruck im Querformat.
In der Vorschau kontrollieren wir, ob die Seitenvorschübe sinnvoll eingefügt sind.
Gegebenenfalls können wir in einer Markup-Zelle einen Seitenvorschub erzeugen mit:

```
<div style="page-break-after: always;"></div>
```

Hinweis: Bilder, die mit dem image-tag in das Notebook eingebettet sind, werden bei dieser Vorgehensweise
nicht ins PDF übernommen. Wenn wir Skizzen, die wir als Bild gespeichert haben, mit ins PDF aufnehmen wollen, müssen wir diese Bilder mit einer Python-Anweisung im Notebook zeigen.

```
from IPython.display import Image, display               
display(Image(filename='skizze.png', width=600))
```

Den Output der Programme fügen wir in eine Markdown-Zelle ein. Damit die Ausgaben kein Fließtext werden, müssen wir sie in dreifache Backticks einschließen: \`\`\` 


-----

**Beispiele** für die Dokumentation mit JupyterLab findet ihr unter *Programmierwettbewerbe* im Abschnitt
*Jugendwettbewerb Informatik Runde 3* oder direkt [hier](https://ktheu.github.io/Programmierwettbewerbe/jwinfRunde3/jwinfRunde3.html). Die Spiegelstriche **Doku-Notebook** führen jeweils zu einem  Jupyter-Notebook der Dokumentation.

