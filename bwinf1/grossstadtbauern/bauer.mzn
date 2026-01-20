int: m;
enum Gemuese;
array[1..m, Gemuese] of bool: gericht; 


% Erste Zeile: keine Verschiebung
constraint
  forall(i in 0..3)(
    plan[1,3*i+1] = plan[1,3*i+2] /\
    plan[1,3*i+2] = plan[1,3*i+3]
  );

% Zweite Zeile: +1
% mod 12 nimmt die Werte von 0..11 an. Mit +1 erhalten
% wir den Bereich 1..12
constraint
  forall(i in 0..3)(
    plan[2,((3*i+1) mod 12)+1] =
    plan[2,((3*i+2) mod 12)+1] /\
    plan[2,((3*i+2) mod 12)+1] =
    plan[2,((3*i+3) mod 12)+1]
  );

% Dritte Zeile: +2
constraint
  forall(i in 0..3)(
    plan[3,((3*i+2) mod 12)+1] =
    plan[3,((3*i+3) mod 12)+1] /\
    plan[3,((3*i+3) mod 12)+1] =
    plan[3,((3*i+4) mod 12)+1]
  );

% Decision Variablen ------------------------------------

% gekocht[g,j] = Gericht g wird in Monat j gekocht (boolean)
array[1..m, 1..12] of var bool: gekocht;

% plan[i, m] = g - In Anlage i wird im Monat m das Gemüse g angebaut
array[1..3, 1..12] of var Gemuese: plan;

constraint
  forall(g in 1..m, j in 1..12) (    % für jedes gericht g  und jedes monat j
    gekocht[g,j] <->                 % g wird genau dann im monat j gekocht 
      forall(v in Gemuese where gericht[g,v]) (   % wenn für jedes gemüse v, das in gericht g enthalten ist
        exists(i in 1..3)(plan[i,j] = v)          % eine anlage i existiert, die in monat j gemüse v anbaut
      )
  );
  
 
% Zielfunktion: maximiere Zahl der Gerichte, die mindestens einmal gekocht werden
% Summe aller gerichte g, für die ein monat j existiert, in dem das gericht g gekocht wird
solve maximize sum(g in 1..m)( bool2int( exists(j in 1..12)(gekocht[g,j]) ) );  

constraint plan[1,1] = 27;
constraint plan[2,1] = 28;
constraint plan[3,1] = 40;

output[
  "Es koennen " ++
  show(sum(g in 1..m)( bool2int( exists(j in 1..12)(gekocht[g,j])))) ++
  " Gerichte gekocht werden.\n\n"
]
++
[
  show(plan[r,c]) ++ " " ++
  if c = 12 then "\n" else "" endif
  | r in 1..3, c in 1..12
];

