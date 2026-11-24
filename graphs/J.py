n, m = map(int, input().split())

ends = []

for _ in range(m):
    a, b = map(int, input().split())
    ends.append((a, b))

order = list(map(int, input().split()))

pos = [0] * (n + 1)

for i in range(n):
    pos[order[i]] = i

ans = "YES"

for a, b in ends:
    if pos[a] > pos[b]:
        ans = "NO"
        break

print(ans)