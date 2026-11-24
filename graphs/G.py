n, m = map(int, input().split())

g = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

visited = set()

def dfs(v):
    visited.add(v)

    for u in g[v]:
        if u not in visited:
            dfs(u)

dfs(1)

if m == n - 1 and len(visited) == n:
    print("YES")
else:
    print("NO")