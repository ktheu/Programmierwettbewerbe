## Schnipsel

Meist ist der erste Kasten für Python und der zweite für C++.

#### Header 
```
#include <bits/stdc++.h>
using namespace std;
```

#### Input
```
from sys import stdin
#stdin = open("input.txt", "r")     
```

```
# Bei einigen älteren USACO-Problemen müssen Dateien geschrieben werden.
from sys import stdin, stdout
stdin = open("problem.in", "r")
stdout = open("problem.out", "w")
```
 



#### Infinity
```
inf = float('inf')
inf = 1<<59   # = 2 hoch 59 = eine sehr große Zahl - ist schneller als float('inf')
```

``` 
const int inf = 1e9;
const long long inf = 1e18;
```

#### Adjazenzliste erstellen.
```
n, m = map(int, stdin.readline().split())      
adj = [[] for i in range(n+1)]
for i in range(m):
    a, b, c = map(int, stdin.readline().split())  
    adj[a].append([b,c])
```

```
int n, m;
cin >> n >> m;
vector<pair<int, int>> adj[n + 1];
for (int i = 0; i < m; i++) {
    int a, b, c;
    cin >> a >> b >> c;
    adj[a].push_back({b, c});
}
```

#### Adjazenzmatrix erstellen.
```
inf = float('inf')
zeile = [inf for _ in range(n)]
adj = [zeile[:] for _ in range(n)]
for i in range(n): adj[i][i] = 0
for i in range(m):
    a, b, c = map(int, stdin.readline().split())
    a-=1
    b-=1
    adj[a][b] = adj[b][a]= c
```

```
long long adj[n][n];
for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
        if (i == j)
            adj[i][j] = 0;
        else
            adj[i][j] = inf;
    }
}

for (int i = 0; i < m; i++) {
    int a, b, c;
    cin >> a >> b >> c;
    a--;
    b--;
    adj[a][b] = c;
    adj[b][a] = c;
}
```

