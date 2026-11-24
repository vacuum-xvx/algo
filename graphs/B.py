n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

ist = []  # ист в вершину не входит (столб 0)
stok = []    # сток из вершины не выходит (строка 0)

for i in range(n):
    out = sum(a[i])
    in_v = sum(a[j][i] for j in range(n))
    if in_v == 0:
        ist.append(i + 1)
    if out == 0:
        stok.append(i + 1)

print(len(ist))
for v in ist:
    print(v)
print(len(stok))
for v in stok:
    print(v)