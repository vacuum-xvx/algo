n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

ok = True
for i in range(n):
    if a[i][i] != 0: # петля - нельзя в простом
        ok = False
    for j in range(i + 1, n):
        if a[i][j] != a[j][i]: # нет симм
            ok = False

print("YES" if ok else "NO")