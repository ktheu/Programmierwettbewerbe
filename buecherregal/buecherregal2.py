
nr = 5
f = open('./beispieldaten/buecherregal'+str(nr)+'.txt')

anzFiguren = int(f.readline())
anzBuecher = int(f.readline())

a = [int(x) for x in f.readlines()]    # Liste mit den Bücherhöhen

a.sort()

i = j = 0
figur = 0

while j < len(a):
    if a[j]-a[i] <= 30:
        print(a[j], end=' ')
        j = j+1
    else:
        print('Figur', end=' ')
        figur += 1
        i = j
print()
if figur <= anzFiguren:
    print(f'Aufteilung mit {anzFiguren} Figuren möglich')
else:
    print(f'Aufteilung mit {anzFiguren} Figuren nicht möglich')
