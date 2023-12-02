### Labyrinth

Python:
```
from collections import deque
import sys

def bfs(sx, sy):
    global ans
    vis[sx][sy] = True
    Q = deque([(sx, sy)])
    while Q:
        x, y = Q.popleft()
        if x == ex and y == ey:
            return "YES"

        for i in range(4):
            dx = x + h[i]
            dy = y + v[i]
            if 0 <= dx < n and 0 <= dy < m and not vis[dx][dy]:
                if i == 0:
                    pre[dx][dy] = 'D'
                elif i == 1:
                    pre[dx][dy] = 'U'
                elif i == 2:
                    pre[dx][dy] = 'R'
                elif i == 3:
                    pre[dx][dy] = 'L'
                vis[dx][dy] = True
                Q.append((dx, dy))
    return "NO"

n, m = map(int, sys.stdin.readline().split())
grid =  sys.stdin.read().split()

h = [1,-1,0,0]
v = [0,0,1,-1]
vis = [[False]*1000 for _ in range(1000)]
pre = [[None]*1000 for _ in range(1000)]

for i in range(n):
    for j in range(m):
        if grid[i][j] == '#':
            vis[i][j] = True
        if grid[i][j] == 'A':
            sx,sy = i,j
        if grid[i][j] == 'B':
            ex,ey = i,j

ans = bfs(sx, sy)
print(ans)
if ans == 'NO':
    exit()

path = []
while not (ex == sx and ey == sy):
    path.append(pre[ex][ey])
    if pre[ex][ey] == 'D':
        ex -= 1
    elif pre[ex][ey] == 'U':
        ex += 1
    elif pre[ex][ey] == 'R':
        ey -= 1
    elif pre[ex][ey] == 'L':
        ey += 1

print(len(path))
print(''.join(path)[::-1])

```

C++
```
#include <bits/stdc++.h>

using namespace std;

const int h[] = {1, -1, 0, 0}, v[] = {0, 0, 1, -1};
bool vis[1000][1000];
char pre[1000][1000];

int n, m, sx, sy, ex, ey;

queue<pair<int, int>> Q;
string ans;

void bfs(int sx, int sy) {
    vis[sx][sy] = true;
    Q.push({sx, sy});
    while (!Q.empty()) {
        pair<int, int> P = Q.front();
        Q.pop();
        auto [x, y] = P;
        if (x == ex && y == ey) {
            ans = "YES";
            return;
        }
        for (int i = 0; i < 4; i++) {
            int dx = x + h[i];
            int dy = y + v[i];
            if (0 <= dx && dx < n && 0 <= dy && dy < m && !vis[dx][dy]) {
                if (i == 0)
                    pre[dx][dy] = 'D';
                else if (i == 1)
                    pre[dx][dy] = 'U';
                else if (i == 2)
                    pre[dx][dy] = 'R';
                else if (i == 3)
                    pre[dx][dy] = 'L';
                vis[dx][dy] = true;
                Q.push({dx, dy});
            }
        }
    }
    ans = "NO";
}

int main() {
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        string row;
        cin >> row;
        for (int j = 0; j < m; j++) {
            char c = row[j];
            if (c == '#')
                vis[i][j] = true;
            else if (c == 'A') {
                sx = i;
                sy = j;
            } else if (c == 'B') {
                ex = i;
                ey = j;
            }
        }
    }

    bfs(sx, sy);

    cout << ans << endl;

    if (ans == "NO") return 0;

    vector<char> path;
    while (!(sx == ex && sy == ey)) {
        path.push_back(pre[ex][ey]);
        if (pre[ex][ey] == 'D')
            ex--;
        else if (pre[ex][ey] == 'U')
            ex++;
        else if (pre[ex][ey] == 'R')
            ey--;
        else if (pre[ex][ey] == 'L')
            ey++;
    }

    reverse(path.begin(), path.end());

    cout << path.size() << endl;
    for (auto c : path) cout << c;
    cout << endl;
}

```