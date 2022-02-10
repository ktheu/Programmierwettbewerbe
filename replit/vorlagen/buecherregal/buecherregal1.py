'''
Einlesen der Daten und sortieren der Bücher-Daten

'''
f = open('./beispieldaten/buecherregal1.txt')
anz_figuren = int(f.readline())
anz_buecher = int(f.readline())
buecher = []
for i in range(anz_buecher):
    buecher.append(int(f.readline()))

print('anz_figuren:', anz_figuren)
print('anz_buecher:',anz_buecher)
buecher.sort()
print(buecher)