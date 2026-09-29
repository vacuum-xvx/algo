n, k = map(int, input().split())

wires = [int(input()) for _ in range(n)]

def cut_equals(check, k):
    count = 0
    for wire in wires:
        count += wire // check
    return count >= k

l, r = 0, 10 ** 7 + 1

# 1 -> 0

for _ in range(100):
    mid = (l + r) // 2
    if mid == 0:
        break
    if cut_equals(mid, k):
        l = mid
    else:
        r = mid

print(l)