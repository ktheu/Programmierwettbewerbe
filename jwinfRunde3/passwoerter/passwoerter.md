## Passwörter

39\. Bundeswettbewerb Informatik - Junioraufgabe 1

[Aufgabenstellung](passwoerter.pdf) -  [Lösungshinweise](passwoerter_loesung.pdf) 


#### Python

```
import random as r
def pw():
    anzahlSilben = r.randint(5,7)        # [5,7]

    typen = ['CV','VC','CVC','N']
    a = []
    lasttyp = None
    for i in range(anzahlSilben):
        typ = typen[r.randint(0,3)]
        if typ == 'N' and lasttyp == 'N': typ = 'CV'
        a.append(typ)
        lasttyp = typ
        
    V = list('aeiou') 
    C = list('bcdfglmnprstvxz') + ['sch','ch']
    N = [str(x) for x in range(1,100)]

    at = list(''.join(a))
    pw = ""
    for x in at:
        if x == 'V':
            pw += V[r.randint(0,len(V)-1)]
        elif x == 'C':
            pw += C[r.randint(0,len(C)-1)]
        elif x == 'N':
            pw += N[r.randint(0,len(N)-1)]

    return pw
                
for i in range(30):
    print(pw())
```

Ausgabe:

```
tucfasdifemmevvec
bomdecpubtutgofi
in56pitafulschaspa
cep37sotusub
ri16sool74picup
sche60zov2chobot
62chuchicuvbudubzid
3luchgovezveip
umsum99ut77
oschi65toucnazmez
ubchoxuaridza
50schive62damen
timach91lofich65ed
os38gop58ge
xaevippecnelsu
ef56ceratzu63ma
cugobdolichsche
cauzfi17li
totgur59zuvetim
efgad62epmutpeztusch
85ceclelepacdivoch
toap18zedu
sorog25zizi
85fe37admoos
81rovixrievfe
culpa80xo35
79dozocecnap20
53schuesch75nun7eg
todixboim90
madeschugis51le16
```