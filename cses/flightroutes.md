### Flight Routes

```
#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pi;
typedef pair<long long, int> pli;

vector<pi> adj[100001];
int cnt[100001];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m, k;
    cin >> n >> m >> k;

    for (int i = 0; i < m; i++) {
        int a, b, c;
        cin >> a >> b >> c;
        adj[a].push_back({b, c});
    }

    priority_queue<pli, vector<pli>, greater<pli>> q;
    q.push({0, 1});

    while (!q.empty()) {
        auto [d, u] = q.top();
        q.pop();

        cnt[u]++;

        if (u == n) {
            cout << d << " ";
            if (cnt[u] == k)
                break;
        }

        if (cnt[u] <= k) {
            for (auto [v, c] : adj[u]) {
                q.push({d + c, v});
            }
        }
    }
    return 0;
}
```