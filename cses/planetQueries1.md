### Planet Queries 1

```
#include <bits/stdc++.h>
using namespace std;

int nxt[200001][30];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, q;
    cin >> n >> q;
    for (int i = 1; i < n + 1; i++)
        cin >> nxt[i][0];

    for (int k = 1; k <= 29; k++)
        for (int i = 1; i < n + 1; i++)
            nxt[i][k] = nxt[nxt[i][k - 1]][k - 1];

    int x, k;
    for (int i = 0; i < q; i++) {
        cin >> x >> k;
        for (int j = 0; j <= 29; j++) {
            if (k & (1 << j))
                x = nxt[x][j];
        }
        cout << x << '\n';
    }
}
```