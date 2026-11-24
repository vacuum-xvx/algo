from collections import deque

n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]

a, b = map(int, input().split())
a -= 1
b -= 1

dist = [-1] * n
parent = [-1] * n

q = deque([a])
dist[a] = 0

while q:
    v = q.popleft()

    for u in range(n):
        if g[v][u] == 1 and dist[u] == -1:
            dist[u] = dist[v] + 1
            parent[u] = v
            q.append(u)

print(dist[b])

if dist[b] > 0:
    path = []
    v = b

    while v != -1:
        path.append(v + 1)
        v = parent[v]

    path.reverse()
    print(*path)