## [CSES ProblemSet](https://cses.fi/)


### Graphen

---

#### Counting Rooms  
Hier wird nach der Anzahl der connected components in einem grid gefragt.

Wir starten von jedem nicht besuchten Knoten ein dfs und zählen, wie oft wir starten müssen um alle Knoten zu besuchen. Python schafft nur mit der nicht-rekursiven Implementation von dfs das Zeitlimit.

---

#### Labyrinth 
In einem grid soll ein kürzester Weg von A nach B angegeben werden.

Wir starten von A ein bfs. Falls wir B erreichen, rekonstruieren wir mit pre den Pfad von B zurück nach A.

---

#### Building Roads

Es soll herausgefunden werden, wieviele Straßen gebaut werden müssen, damit alle Städte erreichbar sind. Die zu bauenden Straßen
sollen aufgezählt werden.

Es geht darum, die connected components zu finden und dann beliebige Verbindungen zwischen den connected components aufzuzählen.

Wir starten von jedem nicht besuchten Knoten ein dfs und vermerken bei jedem Knoten, welche cc-Nummer er hat.
Bei jedem neuen dfs-Start erhöhen wir die cc-Nummer um 1. Wir können uns beispielsweise jeweils den ersten Knoten merken,
der die nächste cc-Nummer erhält und dann alle gemerkten Knoten verbinden.

----

#### Message Route

In einem Netzwerk soll herausgefunden werden, ob es einen Weg von 1 nach n gibt. Wenn ja, soll ein kürzester Weg
ausgegeben werden.

Wir starten bfs von Knoten 1 und suchen Knoten n.

-----


#### Building Teams

Es soll herausgefunden werden, ob ein Freundschaftsgraph bipartite ist (d.h. sich aufteilen lässt in 2 Knotenmengen, so dass
innerhalb jeder Knotenmengen keine Verbindung vorhanden ist).

Von jedem nicht besuchten Knoten starten wir ein bfs und wechseln für die Nachbarn die Partition. Falls wir auf 
einen Widerspruch stoßen, ist der Graph nicht bipartite. 

----

#### Round Trip

In einem Straßennetz soll eine Rundtour gefunden werden, die durch mindestens 2 andere Städte geht.

Wir starten von jedem nicht-besuchten Knoten ein dfs und merken uns jeweils den Vorgänger.
Wenn wir bei der Untersuchung der Nachbarn eine Knoten finden, den wir schon besucht haben und
der nicht der Vorgänger ist, haben wir einen gesuchten Kreis gefunden.

Rekursiv:  dfs(u) beantwortet die Frage: gibt es von u aus einen Weg
zu einem schon besuchten Knoten, der nicht über pre[u] verläuft? Wir beantworten diese Frage, indem wir
sie allen Nachbarknoten stellen, ausgenommen pre[u].


----

#### Monsters

In einem Labyrinth sollen wir zu einem Ausgang finden, ohne dass uns eines der Monster erreichen kann.

Wir starten zunächst ein bfs mit allen Monster-Positionen in der Startqueue um die kürzesten Entfernungen
der freien Positionen zu den Monstern zu ermitteln. Dann starten wir ein bfs von unserer Startposition und
prüfen, ob es einen Weg zu einem Ausgang gibt, so dass wir jeweils vor einem Monster auf den Wegpositionen sind.

----

#### Shortest Route 1
Es soll die kürzeste Entfernung von 1 zu allen anderen Knoten berechnet werden. 

Dijkstra: wir setzen dist des Startknotens auf 0, alle anderen auf unendlich. 
Den Heap initialisieren wir mit Startknoten und Distanz 0.
Solange der Heap nicht leer ist 
holen wir das erste nicht-besuchte Element u und markieren es als besucht.
Wenn sich ein Nachbar v von u verbessert, fügen wir v mit der besseren
Distanz in den Heap ein.

----


#### Shortest Route 2
Gegeben ist ein Graph mit Distanzen. Es sollen viele verschiedene Anfragen zu 
den kürzesten Entfernungen zwischen zwei Städten beantwortet werden.

Floyd-Warshall: Initialisiere Distanzmatrix mit den Kosten der gegebenen Wege, 0 in 
der Diagonalen und INF sonst. Schrittweise wird der kürzeste Weg berechnet, wenn
man als Zwischenknoten die Knoten 1...k benutzen darf.

----


#### High Score
In einem gerichteten, gewichteten Graphen, der negative Gewichte enthalten darf, suchen wir
den längsten Weg von 1 nach n. Wir müssen auch erkennen, ob der Weg durch einen Kreis beliebig lang werden kann.

Bellman-Ford: Wir multiplizieren die Gewichte mit -1, dann müssen wir den kürzesten Weg finden. Die Distanz zum Startknoten
initialisieren wir mit 0, alle anderen mit unendlich. Wir gehen n-1 mal alle Kanten durch und schauen, ob sich was verbessern lässt (relaxieren).
Wir gehen nochmal n-1 mal alle Kanten durch und schauen, ob sich was verbessern lässt,
setzen aber das Ergebnis der Relaxation sofort auf -inf. In dist[n] steht dann entweder -inf oder die Distanz des kürzesten Wegs.

----

#### Cycle Finding
In einem gerichteten Graphen soll ein negativer Kreis gefunden werden und ggf. ausgegeben werden. 

Bellman-Ford: Wir gehen n-1 mal alle Kanten durch und schauen, ob sich was verbessern lässt und merken uns jeweils den Vorgängerknoten, der für die Verbesserung verantwortlich ist. 
Dann gehen wir noch einmal durch alle Kanten durch. Wenn sich etwas verbessern lässt, gibt es einen negativen Kreis.
Der verbesserte Knoten muss aber nicht auf dem Kreis liegen. Deswegen gehen wir n-1 prev-Schritte zurück zu einem Knoten vc. 
Der ist mit Sicherheit in dem negativen Kreis. Von dort gehen wir weiter solange zurück, bis wir wieder auf vc stoßen. 
Alternativ könnten wir von vc auch solange zurückgehen, bis wir auf einen Knoten stoßen, den wir schonmal gesehen haben.

----

#### Flight Routes

Wir gehen vor wie bei Dijkstra aber ohne dist-Array und wir berücksichtigen nicht, ob wir einen Knoten schon einmal besucht haben. Immer wenn wir aus dem heap eine Verbindung zu einem Knoten erhalten, setzen wir cnt für diesen Knoten um 1 nach oben. Wenn der Knoten das Ziel ist, geben wir die Kosten aus. Statt zu prüfen, ob wir einen Knoten schon besucht haben prüfen wir nur, ob wir <= k mal bei dem Knoten waren. Wenn dies der Fall ist, stopfen wir alle Nachbarverbindungen in den heap.


#### Longest Flight Route

Gesucht ist der längste Pfad in einem DAG zwischen den Knoten 1 und n. 

Wir berechnen die maximale Anzahl dist von Knoten zwischen einem beliebigen Knoten und dem Zielknoten. Wir initialisieren diese Werte mit 0, für den Zielknoten mit 1. Dann gehen wir mit dfs rekursiv durch den Graphen. Die Werte der Nachbarn nutzen wir, um für den aktuellen Knoten den längsten Pfad zu finden. Wenn dist[1] am Ende immer noch auf 0 steht, gibt es keine Verbindung,
ansonsten ermitteln wir mit nex-Schritten den längsten Pfad zu n.

----

#### Planet Queries 1
 

Von jedem Planeten kann man zu genau einem weiteren Planeten springen (functional graph). Auf welchem Planeten landet man nach k Sprüngen. Es sind viele queries zu beantworten.

Wir verwenden binary lifting (binary jumping). Wir berechnen den 2^k-ten Sprung für jeden Planeten.
Daraus ermitteln wir dann die Ergebnisse der Abfragen.

----

#### Planet Cycles

In einem funktionalen Graph werden die Längen der Wege gesucht, bis sich ein Knoten wiederholt.
So ein Graph besteht aus Komponenten, die jeweils aus einem Kreis und ggf mehreren Zubringern besteht.

Für jeden nicht besuchten Knoten:
Wir gehen solange, bis wir einen besuchten Knoten gefunden haben und merken uns den path dorthin. Den schon besuchten
Knoten fügen wir ans Ende des paths noch hinzu. Für den ersten Knoten des Pfads ist die Antwort dann len(path)-1.
Wir entfernen jeweils das erste Element des Pfads, die Antwort veringert sich dann um 1, es sei denn, der neue
Anfangsknoten stimmt mit dem Endknoten überein. Dann haben alle restlichen Knoten die Antwort: Kreislänge.
Wenn wir bei einem Zubringer starten, müssen wir die Antwort des schon besuchten Knotens noch hinzuzählen. Das können wir auch am Anfang machen, weil diese Längen mit 0 initialisiert sind.

----

#### Road Reparation

Es wird die billigste Möglichkeit gesucht, alle Städte mit neuen Straßen zu verbinden. Gesucht ist also ein MST.

Jarnik-Prim: Gehe von einem Knoten aus und füge immer wieder einen neuen Knoten entlang der leichtesten Kante hinzu.
Wenn wir einen Knoten gewählt haben, fügen wir alle Kanten zu noch nicht besuchten Knoten dem Heap hinzu.

