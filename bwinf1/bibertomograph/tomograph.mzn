int: n;
array[1..n] of int: sp;
array[1..n] of int: ze;
array[1..2*n-1] of int: d1;
array[1..2*n-1] of int: d2;
array[1..n] of array[int] of int: spalten;
array[1..n] of array[int] of int: zeilen;
array[1..2*n-1] of array[int] of int: diagonals1;
array[1..2*n-1] of array[int] of int: diagonals2;

% ----- Decision variables -----
array[0..n*n-1] of var bool: x;

% ----- Constraints -----
% Spalten
constraint
    forall(i in 1..n)(
        sum(j in 1..n)( x[spalten[i][j]] ) = sp[i]
    );

% Zeilen
constraint
    forall(i in 1..n)(
        sum(j in 1..n)( x[zeilen[i][j]] ) = ze[i]
    );

% Diagonalen1 
constraint
    forall(i in 1..2*n-1)(
        sum(j in index_set(diagonals1[i]))( x[diagonals1[i][j]] ) = d1[i]
    );

% Diagonalen2
constraint
    forall(i in 1..2*n-1)(
        sum(j in index_set(diagonals2[i]))( x[diagonals2[i][j]] ) = d2[i]
    );

% ----- Solve -----
solve satisfy;

% ----- Output -----
output [ 
    if fix(x[r* n + c]) == 1 then "1 " else "0 " endif ++
    if c = n-1 then "\n" else "" endif
    | r in 0..n-1, c in 0..n-1
];
