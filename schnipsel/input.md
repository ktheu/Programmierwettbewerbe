## Header, Input, Infinitiy


#### Header, typedefs und main
```
#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;

const ll inf = 1e18;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
}
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

```
from sys import stdin
a, b = map(int,stdin.readline().split())  
a, b = [int(x) for x in stdin.readline().split()]    # etwas langsamer
```

```
stdout.write()      # macht keinen Zeilenvorschub, manchmal Zeitvorteil zu print() 
```

C++:  Umleitung von stdin/stdout in eine Datei (mit Angabe des absoluten Pfads).
Dann wie gewohnt cin, cout benutzen.

``` 
freopen("C:\\Users\\khthe\\...\\Programmierwettbewerbe\\test.txt", "r", stdin);
freopen("C:\\Users\\khthe\\...\\Programmierwettbewerbe\\test.out", "w", stdout);
cin >> n >> q;
cout << n << " " << q << endl;

```

``` 
// Für ältere USACO-Aufgaben
freopen("swap.in", "r", stdin);
freopen("swap.out", "w", stdout);
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
 
```
// Array dist mit unendlich füllen
ll dist[100001]
memset(dist, 0x3f, sizeof(dist));
```




