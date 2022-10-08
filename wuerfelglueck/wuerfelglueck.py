import random


class Spieler:
    def __init__(self, wuerfel=[1, 2, 3, 4, 5, 6]):
        self.lauf = [0]
        self.wuerfel = wuerfel

    def anzahlDraussen(self):
        return 4 - len(self.lauf)

    def startFrei(self):
        return 0 not in self.lauf

    def aufStart(self):
        self.lauf.append(0)

    def mussVomStartZiehen(self):
        return 0 in self.lauf and self.anzahlDraussen() > 1

    def kannZiehenVonUm(self, k, w):
        return k <= 39 and k + w <= 43 and k + w not in self.lauf

    def zieheVonUm(self, k, w):
        self.lauf.remove(k)
        self.lauf.append(k+w)

    def fertig(self):
        return sorted(self.lauf) == [40, 41, 42, 43]

    def reset(self):
        self.lauf = [0]

    def reihenfolge(self):
        tmp = [x for x in self.lauf if x < 40]
        tmp.sort(reverse=True)
        if 0 in tmp and self.anzahlDraussen() > 0:
            tmp.remove(0)
            tmp = [0]+tmp
        return tmp

    def zieheUm(self, w):
        # print('zieheUm', w)
        if w == 6 and self.startFrei() and self.anzahlDraussen() > 0:
            self.aufStart()
        else:
            for k in self.reihenfolge():
                if self.kannZiehenVonUm(k, w):
                    self.zieheVonUm(k, w)
                    break

    def wuerfle(self):
        return random.choice(self.wuerfel)

    def ziehe(self):
        w = self.wuerfle()
        self.zieheUm(w)

        while w == 6 and not self.fertig():
            w = self.wuerfle()
            self.zieheUm(w)

    def schmeisse(self, s1):
        for i in range(20):
            if i in self.lauf and i+20 in s1.lauf:
                s1.lauf.remove(i+20)
        for i in range(20, 40):
            if i in self.lauf and i-20 in s1.lauf:
                s1.lauf.remove(i-20)

    def stuck(self):
        if self.anzahlDraussen() > 0 and 6 in self.wuerfel:
            return False
        for x in self.reihenfolge():
            for k in self.wuerfel:
                if self.kannZiehenVonUm(x, k):
                    return False

        return True

    def __repr__(self):
        return str(self.lauf)


def spiel(s0, s1):

    while not (s0.fertig() or s1.fertig()):
        if s0.stuck() and s1.stuck():
            return -1
        s0.ziehe()
        s0.schmeisse(s1)
        s1.ziehe()
        s1.schmeisse(s0)
    if s0.fertig():
        return 0
    else:
        return 1


def match(w0, w1, anzahl):
    s0 = Spieler(w0)
    s1 = Spieler(w1)
    g0 = g1 = g2 = 0
    for i in range(anzahl):
        s0.reset()
        s1.reset()
        erg = spiel(s0, s1)
        if erg == 0:
            g0 += 1
        elif erg == 1:
            g1 += 1
        else:
            g2 += 1

    for i in range(anzahl):
        s0.reset()
        s1.reset()
        erg = spiel(s1, s0)
        if erg == 0:
            g1 += 1
        elif erg == 1:
            g0 += 1
        else:
            g2 += 1
    return g0, g1, g2


nr = 0
f = open('./beispieldaten/wuerfel'+str(nr)+'.txt')
anz = int(f.readline())
wuerfel = []
for i in range(anz):
    zeile = [int(x) for x in f.readline().split()]
    wuerfel.append(zeile[1:])

print('Wuerfel', nr)
print('==========')
for i in range(anz):
    print('Würfel:', wuerfel[i])
    siege = 0
    for j in range(anz):

        if j != i:

            w0, w1 = wuerfel[i], wuerfel[j]
            g0, g1, g2 = match(w0, w1, 200)
            if g0 > g1:
                siege += 1
            print(g0, g1, g2, w1)
    print('Siege:', siege)
    print('------------------------')
