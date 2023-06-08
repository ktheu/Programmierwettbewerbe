### Planet Cycles

```
#include <bits/stdc++.h>
using namespace std;

int adj[200001];
bool vis[200001];
int ans[200001];

int main(void) {
    int n;

    cin >> n;
    for (int i = 1; i <= n; i++) {
        cin >> adj[i];
    }

    for (int i = 1; i <= n; i++) {
        if (vis[i]) continue;
        int j = i;
        queue<int> path;
        while (!vis[j]) {
            vis[j] = true;
            path.push(j);
            j = adj[j];
        }
        path.push(j);

        int pathlen = path.size() - 1 + ans[path.back()];
        int d = 1;

        while (!path.empty()) {
            if (path.front() == path.back()) d = 0;
            ans[path.front()] = pathlen;
            path.pop();
            pathlen -= d;
        }
    }

    for (int i = 1; i <= n; i++) {
        cout << ans[i] << " ";
    }
}
```