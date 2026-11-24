import sys
sys.setrecursionlimit(100000)

n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]

color = [0] * n # 0 белая, 1 серая, 2 чёрная
cycle = False

def dfs(v):
    global cycle
    color[v] = 1
    for u in range(n):
        if mat[v][u] == 1:
            if color[u] == 0:
                dfs(u)
            elif color[u] == 1:
                cycle = True
    color[v] = 2

for v in range(n):
    if color[v] == 0:
        dfs(v)

print(1 if cycle else 0)