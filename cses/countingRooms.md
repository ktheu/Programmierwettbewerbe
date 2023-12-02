### Counting Rooms

Python:
```
n, m = [int(x) for x in input().split()]
h = [1,-1,0,0]
v = [0,0,1,-1]
vis = [[False]*m for _ in range(n)]

def dfs(x, y):
    vis[x][y] = True
    stack = [(x, y)]
    while stack:
        x, y = stack.pop()
        for i in range(4):
            dx = x + h[i]
            dy = y + v[i]
            if 0 <= dx < n and 0 <= dy < m and not vis[dx][dy]:
                vis[dx][dy] = True
                stack.append((dx, dy))

for i in range(n):
    row = input()
    for j in range(m):
        if row[j] == '#':
            vis[i][j] = True
            
ans = 0
for i in range(n):
    for j in range(m):
        if not vis[i][j]:
            ans += 1
            dfs(i, j)

print(ans)
```

C++
```
#include <bits/stdc++.h>

using namespace std;

char c;
int n, m;
int h[] = {1, -1, 0, 0}, v[] = {0, 0, 1, -1};
bool vis[1000][1000];

void dfs(int x, int y) {
    vis[x][y] = true;
    for (int i = 0; i < 4; i++) {
        int dx = x + h[i], dy = y + v[i];
        if (0 <= dx && dx < n && 0 <= dy && dy < m && !vis[dx][dy])
            dfs(dx, dy);
    }
}

int main() {
    int ans = 0;
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> c;
            vis[i][j] = (c == '#');
        }
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (!vis[i][j]) {
                dfs(i, j);
                ans++;
            }
        }
    }
    cout << ans << endl;
}

```