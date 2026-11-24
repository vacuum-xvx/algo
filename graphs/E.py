n, m = map(int, input().split())
a = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    a[x].append(y)
    a[y].append(x)

visited = [False] * (n + 1)
components = []

for i in range(1, n + 1):
    if not visited[i]:
        component = []
        stack = [i]
        visited[i] = True
        while stack:
            v = stack.pop()
            component.append(v)
            for u in a[v]:
                if not visited[u]:
                    visited[u] = True
                    stack.append(u)
        components.append(component)

print(len(components))
for c in components:
    print(len(c))
    print(*c)