### Road Reparation

```
#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pi;

bool vis[100001];

int main() {
    int n, m;
    cin >> n >> m;

    vector<pi> adj[n + 1];
    for (int i = 0; i < m; i++) {
        int a, b, c;
        cin >> a >> b >> c;
        adj[a].push_back({b, c});
        adj[b].push_back({a, c});
    }

    priority_queue<pi, vector<pi>, greater<pi>> heap;

    long long summe = 0;
    heap.push({0, 1});
    int count = 0;

    while (!heap.empty()) {
        auto [cost, u] = heap.top();
        heap.pop();

        if (vis[u]) continue;

        vis[u] = true;
        summe += cost;
        count++;

        for (auto [v, cost] : adj[u]) {
            if (vis[v]) continue;
            heap.push({cost, v});
        }
    }

    if (count != n) {
        cout << "IMPOSSIBLE";
    } else {
        cout << summe;
    }
    return 0;
}

```