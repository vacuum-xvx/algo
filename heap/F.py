import heapq

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
a.sort()

heap = []

for t, d in a:
    if heap and heap[0] <= t:
        heapq.heappop(heap)

    heapq.heappush(heap, t + d)

print(len(heap))
