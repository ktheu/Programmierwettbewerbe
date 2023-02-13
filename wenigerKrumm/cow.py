# data1 = 'GGH'
# data2 = '2 3 3'
input()
data1 = input()
data2 = input()

sH = data1.count('H')
sG = data1.count('G')

vorkommen = {'H': sH, 'G': sG}
 

breed = list(data1)
ende = [int(i)-1 for i in data2.split()]    # 0-indexd

def check(tup):
    i, j = tup    # index of the two leader cows
    if data1[i] == data1[j]: return False
    leaders = [data1[i], data1[j]]
    breeds = [vorkommen[c] for c in leaders]
    bereiche = [data1[i:ende[i]+1],data1[j:ende[j]+1]]

    b0 = bereiche[0].count(leaders[0]) == vorkommen[leaders[0]]
    c0 = i < j <= ende[i]
    b1 = bereiche[1].count(leaders[1]) == vorkommen[leaders[1]]
    c1 = j < i <= ende[j]

    if (b0 or c0) and (b1 or c1):
        return True

 
import itertools as it
zaehl = 0
for tup in it.combinations(range(len(data1)),2):
    if check(tup):
        zaehl += 1

print(zaehl)




   