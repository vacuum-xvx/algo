n, m = map(int, input().split())
mat = [[0] * n for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    mat[a - 1][b - 1] = 1
    mat[b - 1][a - 1] = 1

ok = True
for i in range(n):
    for j in range(n):
        if i != j and mat[i][j] == 0: # не диагональ и нет связи
            ok = False

print("YES" if ok else "NO")