def play_game(dice_num):
    pos = 0
    print(pos)
    pos += dice_num
    print(pos)
    while pos < 100:
        if pos == 6:
            pos = 27
            print(pos)
            pos += dice_num
        elif pos == 27:
            pos = 6
            print(pos)
            pos += dice_num
        elif pos == 14:
            pos = 19
            print(pos)
            pos += dice_num
        elif pos == 19:
            pos = 14
            print(pos)
            pos += dice_num
        elif pos == 33:
            pos = 38
            print(pos)
            pos += dice_num
        elif pos == 38:
            pos = 33
            print(pos)
            pos += dice_num
        elif pos == 31:
            pos = 42
            print(pos)
            pos += dice_num
        elif pos == 42:
            pos = 31
            print(pos)
            pos += dice_num
        elif pos == 21:
            pos = 53
            print(pos)
            pos += dice_num
        elif pos == 53:
            pos = 21
            print(pos)
            pos += dice_num
        elif pos == 51:
            pos = 59
            print(pos)
            pos += dice_num
        elif pos == 59:
            pos = 51
            print(pos)
            pos += dice_num
        elif pos == 46:
            pos = 62
            print(pos)
            pos += dice_num
        elif pos == 62:
            pos = 46
            print(pos)
            pos += dice_num
        elif pos == 70:
            pos = 76
            print(pos)
            pos += dice_num
        elif pos == 76:
            pos = 70
            print(pos)
            pos += dice_num
        elif pos == 68:
            pos = 80
            print(pos)
            pos += dice_num
        elif pos == 80:
            pos = 68
            print(pos)
            pos += dice_num
        elif pos == 65:
            pos = 85
            print(pos)
            pos += dice_num
        elif pos == 85:
            pos = 65
            print(pos)
            pos += dice_num
        elif pos == 57:
            pos = 96
            print(pos)
            pos += dice_num
        elif pos == 96:
            pos = 57
            print(pos)
            pos += dice_num
        elif pos == 92:
            pos = 98
            print(pos)
            pos += dice_num
        elif pos == 98:
            pos = 92
            print(pos)
            pos += dice_num
        else:
            pos += dice_num
        print(pos)
        if pos == 101:
            pos = 99
        if pos == 99 and dice_num == 3:
            print("3 makes it go forever")
            return
        if pos == 102:
            pos = 98
        if pos == 98 and dice_num == 4:
            print("4 makes it go forever")
            return
        if pos == 103:
            pos = 97
        if pos == 104:
            pos = 96
        if pos == 105:
            pos = 95
        if pos == 100:
            print(f"We can win if we roll {dice_num} always!\n")


play_game(1)
play_game(2)
play_game(3)
play_game(4)
play_game(5)
play_game(6)


''' 

Du hast für jedes Rutschen auf der Leiter eine eigene if-Anweisung. Das ist ok - aber mühsam. Es gibt
mehrere Arten, die Rutschmöglichkeiten zu verwalten, mit einem dictionary oder mit einer Liste von
Tupeln, also z.B.
leiter = {6:27, 14:19, ......}  oder
leiter = [(6,27), (14,19), ....]

Ich nehme an, dass du die einzelnen Würfelwerte ausprobiert hast und geschaut hast, wie weit man damit kommt und
dann am Ende die Bedingungen für die Schleifen bei den Werten 3 und 4 formuliert hast. 
Es könnte ja auch sein, dass eine Schleife weiter im Inneren des Spielfeldes entsteht. Das würde dein Programm in
der jetzigen Fassung nicht erkennen.

Für das aktuelle Spielfeld sind deine Ergebnisse aber richtig.
''' 
 