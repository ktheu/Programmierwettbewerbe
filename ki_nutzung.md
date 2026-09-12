## Leitfaden zur KI-Nutzung bei den Bwinf-Informatik-Wettbewerben

### Bwinf 

Bwinf schreibt in den FAQ zur KI-Nutzung:

In den ersten beiden Runden darfst du KI-Tools wie ChatGPT oder CoPilot nutzen; sie können dir beim Verstehen, Nachdenken oder Programmieren helfen. Wichtig ist nur: Du solltest selbst verstehen, was du einreichst, und deine Lösungen eigenständig entwickeln. Künstliche Intelligenz ist ein Werkzeug, das die bereits verfügbaren Werkzeuge ergänzt.


### Zusätzliche Hinweise

> Eine Lösung zu **verstehen** ist viel leichter, als sie zu **finden**.

Lässt du dir eine Lösung erklären, hast du sie in zehn Minuten verstanden – und fühlst dich, als hättest du es selbst gekonnt. Geübt hast du aber nur das Verstehen.

#### Die wichtigste Regel: Erst die Idee, dann die KI

**Bevor du die KI das erste Mal zur Lösung befragst, schreibst du deine Lösungsidee in drei bis fünf Sätzen auf** – in normalem Deutsch, ohne Code. Diese **Ideenskizze** gibst du mit ab.

Danach darfst du die KI als Werkzeug benutzen. Wie weit, hängt von deiner Klassenstufe ab.



#### Die vier Phasen einer Aufgabe

| Phase | Was du tust | bis Klasse 10 | Klasse 11 und 12 |
|---|---|---|---|
| **1. Verstehen** | Aufgabe und Eingabeformat begreifen | ✅ erlaubt – frag, was etwas **bedeutet**, nicht wie man es **löst** | ✅ genauso |
| **2. Idee finden** | den Lösungsweg entwickeln | ❌ **ohne KI** | ❌ **ohne KI** |
| **3. Umsetzen** | die eigene Idee programmieren | ✅ nur **Einzelfragen** zu Python und Bibliotheken – **keine fertigen Funktionen** | ✅ auch **ganze Hilfsfunktionen** (Einlesen, Zeichnen, Testdaten erzeugen), sobald die Ideenskizze steht |
| **4. Prüfen** | Testfälle, Sonderfälle, Fehlersuche | ✅ erlaubt – aber erst nach deiner **eigenen** Testliste | ✅ genauso |

**Warum bis Klasse 10 strenger?**

* Junioraufgaben sind so kurz, dass es kaum „Handwerk" gibt. Wer sich Funktionen schreiben lässt, hat schnell die ganze Aufgabe gelöst.

#### Beispiel-Prompts

##### ✅ Erlaubt

**Phase 1 – Verstehen**

* *„In der Datei steht `8b Freitag 13 19 15`. Laut Aufgabe sind das Klasse, Tag, Beginn, Ende
  und Größe. Habe ich das richtig gelesen?"*
* *„Beschreibe mir in eigenen Worten, was in dieser Aufgabe gefragt ist. Verrate mir keinen
  Lösungsweg."*
* *„Was bedeutet ‚gegen den Uhrzeigersinn' bei den Eckpunkten eines Vielecks?"*

**Phase 3 – Umsetzen** (alle Klassenstufen)

* *„Wie zerlege ich in Python eine Zeile an den Leerzeichen?"*
* *„Wie zeichne ich mit matplotlib einen waagerechten Balken?"*
* *„Mein Programm liefert 86 statt 60. Stelle mir Fragen, die mir helfen, den Fehler selbst zu
  finden – nenne mir nicht die Lösung."*

**Phase 3 – Umsetzen** (nur Klasse 11 und 12)

* *„Schreibe eine Funktion, die Dateien in diesem Format einliest: [Format]. Halte den Code
  einfach, ich muss ihn verstehen können."*
* *„Schreibe ein Programm, das zufällige Testdateien in diesem Format erzeugt."*

**Phase 4 – Prüfen**

* *„Hier ist meine Lösungsidee. Welche Sonderfälle könnten sie zu Fall bringen? Nenne nur die
  Fälle, nicht wie man sie behandelt."*
* *„Ist mein Code an irgendeiner Stelle unnötig kompliziert?"*

##### ❌ Nicht erlaubt

| Prompt | Was du verlierst |
|---|---|
| *„Schreib mir ein Programm, das diese Aufgabe löst."* | Alles – und du merkst es nicht, weil das Programm funktioniert. |
| *„Welchen Algorithmus nimmt man für dieses Problem?"* | Genau den Gedanken, um den es in der Aufgabe geht. |
| *„Ich komme nicht weiter, gib mir einen Tipp."* | Ein guter Tipp *ist* meistens schon die halbe Lösung. |
| *„Schreib mir den Code und erklär ihn mir dann."* | Fühlt sich gründlich an, ist aber besonders tückisch: Am Ende verstehst du die Lösung, hast aber nie geübt, eine zu finden. |
| *„Schreib mir die Dokumentation."* | Deinen besten Selbsttest: Beim Erklären merkst du, was du nicht verstanden hast. |
| *„Mach meinen Code professioneller."* | Du reichst Code ein, den du nicht mehr erklären kannst. |
| bis Klasse 10: *„Schreib mir eine Funktion, die die Datei einliest."* | Das bisschen Handwerk, an dem du bei einer Junioraufgabe das Programmieren übst. |


#### Abgabe

Bwinf hat [Vorlagen für die Abgabe](https://bwinf.de/bundeswettbewerb/teilnehmen/vorlagen/) bereitgestellt. Sie gliedert sich in 5 Abschnitte:
- Lösungsidee  
- Umsetzung  
- Werkzeuge 
- Beispiele  
- Quellcode

Die oben erwähnte Ideenskizze gehört in den Abschnitt Lösungsidee. Im Abschnitt Werkzeuge solltest du ein **Prompt-Protokoll** einfügen: Darin listest du auf, in welcher Phase du welche Prompts an die KI gestellt hast und (in Kurzform) was du mit der Antwort angefangen hast. 


