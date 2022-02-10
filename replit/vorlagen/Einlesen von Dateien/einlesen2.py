'''
Die erste Zeile besteht aus 2 Zahlen. Sie geben an, 
wieviele Farben und wieviele Zahlen folgen.

3 5
rot
grün
gelb
10
20
30
40
50
'''

f = open('daten2.txt')
anz1, anz2 = [int(x) for x in f.readline().split()]

farben = []
zahlen = []
for i in range(anz1):
    farben.append(f.readline().strip())

for i in range(anz2):
    zahlen.append(int(f.readline()))
f.close()

print('Anzahl Farben:',anz1)
print('Anzahl Zahlen:',anz2)

print(farben, zahlen)