import sys
sys.setrecursionlimit(100000)

n, s = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n

def dfs(v): # посетили - true, смотрим соседей и если не посещали - идем в них
    visited[v] = True
    for u in range(n):
        if mat[v][u] == 1 and not visited[u]:
            dfs(u)

dfs(s - 1) # индексы с 0
print(sum(visited))