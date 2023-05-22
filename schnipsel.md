## Schnipsel

### Infinity

Python
```Python
inf = float('inf')
inf = 1<<59   # = 2 hoch 59 = eine sehr große Zahl - ist schneller als float('inf')
```

C++
```Cpp
const int inf = 1e9;
const long long inf = 1e18;
```

### Adjazenzliste erstellen.

n = Anzahl der Knoten, m = Anzahl der Kanten

Python
```Python
n, m = [int(x) for x  in input().split()]      
adj = [[] for i in range(n+1)]
for i in range(m):
    a, b, c = [int(x) for x in input().split()]
    adj[a].append([b,c])
```

C++
```Cpp
int n, m;
cin >> n >> m;
vector<pair<int, int>> adj[n + 1];
for (int i = 0; i < m; i++) {
    int a, b, c;
    cin >> a >> b >> c;
    adj[a].push_back({b, c});
}
```

### Adjazenzmatrix erstellen.

n = Anzahl der Knoten, m = Anzahl der Kanten

Python
```Python
inf = float('inf')
zeile = [inf for _ in range(n)]
adj = [zeile[:] for _ in range(n)]
for i in range(n): adj[i][i] = 0
for i in range(m):
    a, b, c = [int(x) for x in input().split()]
    a-=1
    b-=1
    adj[a][b] = adj[b][a]= c
```

C++
```Cpp
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

