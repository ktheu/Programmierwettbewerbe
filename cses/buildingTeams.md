### Building Teams

```Cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> adj[100001];
bool vis[100001];
int team[100001];

bool bfs(int u0) {
    queue<int> q;
    q.push(u0);
    team[u0] = 1;
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        vis[u] = true;
        for (int v : adj[u]) {
            if (vis[v] && team[v] == team[u])
                return false;
            else {
                if (!vis[v]) {
                    q.push(v);
                    team[v] = 3 - team[u];
                }
            }
        }
    }
    return true;
}

int main() {
    int n, m;
    cin >> n >> m;

    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    for (int u = 1; u <= n; u++) {
        if (!vis[u]) {
            if (!bfs(u)) {
                cout << "IMPOSSIBLE" << endl;
                return 0;
            }
        }
    }

    for (int u = 1; u <= n; u++)
        cout << team[u] << " ";
    cout << endl;
}
```