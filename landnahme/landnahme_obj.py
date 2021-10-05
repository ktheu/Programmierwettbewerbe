class Rechteck:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.genehmigt = True

    def __str__(self):
        return f'{self.x1} {self.y1} {self.x2} {self.y2}' 
 
    def linksVon(self, other):
        return max(self.x1, self.x2) <= min(other.x1, other.x2)

    def unterhalbVon(self, other):
        return max(self.y1, self.y2) <= min(other.y1, other.y2)

    def kollidiertMit(self, other):
        return not (self.linksVon(other) or other.linksVon(self)
                    or self.unterhalbVon(other) or other.unterhalbVon(self))


f = open('eingabe2.txt')    # Die Eingabe in eine Liste von Strings einlesen
lines = [x.rstrip('\n') for x in f.readlines()]
N = len(lines)

rechtecke = []              # Eine Liste mit Rechteck-Objekten
for line in lines:
    a = [int(x) for x in line.split()]
    rechtecke.append(Rechteck(a[0],a[1],a[2],a[3]))

for i in range(1, N):
    r1 = rechtecke[i]
    for j in range(i):
        r2 = rechtecke[j]                           # Prüfe ob Kollision mit
        if r2.genehmigt and r1.kollidiertMit(r2):   # schon genehmigten Rechtecken vorliegt
            r1.genehmigt = False
            break;

for r in rechtecke:
    entscheidung = "genehmigt" if r.genehmigt else "abgelehnt"
    print(r, entscheidung)
