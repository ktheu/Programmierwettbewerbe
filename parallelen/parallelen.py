import re

f = open('./beispieldaten/parallelen.txt',encoding='utf-8')
daten = [s.strip() for s in f.readlines() if len(s.strip()) > 0]    # ohne Leerzeilen

laengeGedicht = len(daten)
print('Das Gedicht hat {} Zeilen.'.format(laengeGedicht))

regex = r'[^a-zA-ZßäüöÄÜÖ\s]'    # kein deutscher Buchstabe oder whitesplace
daten = [re.sub(regex,'',s).strip() for s in daten]

ersteHaelfte = [daten[i] for i in range(len(daten)//2)]

worte1 = []
for zeile in ersteHaelfte:
    worte1.extend(zeile.split())

worte = []
for zeile in daten:
    worte.extend(zeile.split())

def doit(worte,i):
  print('----- start mit wortnr = {}'.format(i))
  n = len(worte)
  wort = worte[i]
  print('nr = {}, wort = {}, laenge = {}'.format(i,wort,len(wort)))
  while i+len(wort) < len(worte):
    i = i + len(wort)
    wort = worte[i]
    print('nr = {}, wort = {}, laenge = {}'.format(i,wort,len(wort)))
  return wort

for i in range(len(worte1)):
  s = doit(worte,i)
  print(s)