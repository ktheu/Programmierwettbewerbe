import random

a = """Es gingen zwei Parallelen \
ins Endlose hinaus \
zwei kerzengerade Seelen \
und aus solidem Haus \
Sie wollten sich nicht schneiden \
bis an ihr seliges Grab \
Das war nun einmal der beiden \
geheimer Stolz und Stab \
Doch als sie zehn Lichtjahre \
gewandert neben sich hin \
da wards dem einsamen Paare \
nicht irdisch mehr zu Sinn \
Warn sie noch Parallelen \
Sie wußtens selber nicht \
sie flossen nur wie zwei Seelen \
zusammen durch ewiges Licht \
Das ewige Licht durchdrang sie \
da wurden sie eins in ihm \
die Ewigkeit verschlang sie \
als wie zwei Seraphim"""


list = a.split(" ")

print("Länge der Liste: " + str(len(list)))
 

for x in range(1, 6):
    try:
        for x in range(1, 5):
            b = random.randint(1, 43)
            print(f"Die gewählte Zahl ist {b}. ")
            for i in range(1, 20):
                word = list[b - 1]
                print(str(b) + ") " + "Länge ist: " + str(len(list[b - 1])) + ", Wort ist: "+ word )
                b += len(list[b - 1])
                b += 1
    except IndexError:
        if word == "verschlang":
            print("Letztes Wort: verschlang\n")


'''
Hallo Alisha, ich habe mir dein erstes Programm angeschaut. Das ist wirklich sehr schön.
Das ist schon fortgeschrittene Technik, den Abbruch der Schleife mit einem IndexError durchzuführen!

Hier noch ein paar Anmerkungen:
1. list ist eine eingebaute Funktion in Python. Deswegen sollte man eine eigene Variable nie list nennen.
Hier macht es nichts, da du die list-Funktion anschließend nicht nutzt. Schreibe mal die Zeile
print(list("abc"))
vor deine Zuweisung list = a.split(" ") in dein Programm. Das Programm wird durchlaufen.
Dann schreibe die Zeile hinter deine Zuweisung: es kommt ein Fehler, die Funktion ist durch deine
Zuweisung nicht mehr verfügbar 

2. Mit 'for x in range(1,6)' willst du offenbar eine Schleife 5-mal durchlaufen. Das geht auch mit
'for x in range(5)'.

'''



