### Shortest Route 1

```cpp
#include <bits/stdc++.h>
using namespace std;

const long long INF = 1e18;
vector<pair<int, int>> adj[100001];
long long dist[100001];
bool vis[100001];

int main() {
    int n, m;
    cin >> n >> m;

    for (int i = 1; i < n + 1; i++) {
        dist[i] = INF;
    }
    dist[1] = 0;

    for (int i = 0; i < m; i++) {
        int a, b, c;
        cin >> a >> b >> c;
        adj[a].push_back({b, c});
    }

    priority_queue<pair<long long, int>> q;
    q.push({0, 1});  // Startknoten 1 hat Distanz 0 zu sich selbst

    while (!q.empty()) {
        auto [d, u] = q.top();
        q.pop();
        if (vis[u]) continue;
        vis[u] = true;
        for (auto [v, c] : adj[u]) {
            if (dist[v] > dist[u] + c) {
                dist[v] = dist[u] + c;
                q.push({-dist[v], v});
            }
        }
    }

    for (int i = 1; i < n + 1; i++) {
        cout << dist[i] << " ";
    }
    return 0;
}
```