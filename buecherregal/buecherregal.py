def aufteilung(nr):
  
    f = open('./beispieldaten/buecherregal'+str(nr)+'.txt')

    anzFiguren = int(f.readline())
    anzBuecher = int(f.readline())

    a = [int(x) for x in f.readlines()]    # Liste mit den Bücherhöhen
    a.sort()

    regal = []
    
    abschnitt = []
    abschnitt.append(a[0])

    for i in range(1,len(a)):
        if a[i] - abschnitt[0] <= 30:
            abschnitt.append(a[i])
        else:
            regal.append(abschnitt)
            abschnitt = []
            abschnitt.append(a[i])
            
    regal.append(abschnitt)

    check = "möglich" if len(regal) <= anzFiguren+1 else "unmöglich"
    
    print(f'Beispiel {nr}:')
    print(f'Für die {anzBuecher} Bücher sind {anzFiguren} Figuren verfügbar.')
    print(f'Aufteilung {check}. Es werden {len(regal)-1} Figuren benötigt.')

    print(f"Mögliche Aufteilung mit {len(regal)-1} Figuren: ")
    for i in range(len(regal)-1):
        print(*regal[i])
        print('Figur')
    print(*regal[-1])
         
    print()

for i in range(1,7):
    aufteilung(i)

 