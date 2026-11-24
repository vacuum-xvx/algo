from collections import deque

n = int(input())
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

moves = [
    (2, 1), (2, -1), (-2, 1), (-2, -1),
    (1, 2), (1, -2), (-1, 2), (-1, -2)
]

dist = [[-1] * (n + 1) for _ in range(n + 1)]
parent = {}

q = deque([(x1, y1)])
dist[x1][y1] = 0

while q:
    x, y = q.popleft()

    if (x, y) == (x2, y2):
        break

    for dx, dy in moves:
        nx = x + dx
        ny = y + dy

        if 1 <= nx <= n and 1 <= ny <= n:
            if dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                parent[(nx, ny)] = (x, y)
                q.append((nx, ny))

path = []
v = (x2, y2)

while v != (x1, y1):
    path.append(v)
    v = parent[v]

path.append((x1, y1))
path.reverse()

print(dist[x2][y2])

for x, y in path:
    print(x, y)