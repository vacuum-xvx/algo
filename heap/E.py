import heapq

n = int(input())
ls = list(map(int, input().split()))

heapq.heapify(ls)

total = 0

while n > 1:
    a = heapq.heappop(ls)
    b = heapq.heappop(ls)
    s = a + b
    total += s * 0.05
    heapq.heappush(ls, s)
    n -= 1

print(f'{total:.2f}')
