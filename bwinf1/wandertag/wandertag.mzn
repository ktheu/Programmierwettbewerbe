int: beispiel;
int: n;
int: k = 3;

array[1..n] of int: L;
array[1..n] of int: R;

set of int: POINTS = { L[i] | i in 1..n };
int: m = card(POINTS);
array[1..m] of int: P = sort(POINTS);

array[1..m] of var bool: use_point;
array[1..n] of var bool: covered;

array[1..n] of set of int: valid =
[
    { j | j in 1..m where L[i] <= P[j] /\ P[j] <= R[i] }
    | i in 1..n
];

constraint sum(use_point) = k;

constraint
forall(i in 1..n)(
    covered[i] -> sum(j in valid[i])(bool2int(use_point[j])) >= 1
);

solve maximize sum(covered);

output [
    "Beispiel: ", show(beispiel), "\n",
    "Gewählte Punkte: ",
    show([ P[j] | j in 1..m where fix(use_point[j]) = true ]),
    "\nAbgedeckte Intervalle: ", show(sum(covered)), " von ", show(n), "\n"
];