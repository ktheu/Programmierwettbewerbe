### Building Roads

Python:
```
import sys
 
n, m = map(int, sys.stdin.readline().split())
 
visited = [False] * (n+1)
cc = [0] * (n+1)
adj = [[] for _ in range(n+1)]
 
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    adj[a].append(b)
    adj[b].append(a)
 
ccnum = 0
 
def dfs(u):
    stack = [u]
    while stack:
        u = stack.pop()
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                stack.append(v)
                cc[v] = ccnum
tmp = []
for u in range(1, n+1):
    if not visited[u]:
        ccnum += 1
        tmp.append(u)
        dfs(u)
        cc[u] = ccnum
 
print(ccnum-1)
for k in range(len(tmp)-1):

```

