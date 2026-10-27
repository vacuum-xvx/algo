import heapq

n = int(input())

heap = []
fish = []

for i in range(n):
    x = int(input())
    fish.append(x)

    t = max(1, 1000 - x)
    heapq.heappush(heap, (t, i))

current_time = 0
current_pos = 0

while True:
    t, pos = heapq.heappop(heap)

    if abs(pos - current_pos) > t - current_time:
        print(t)
        break

    current_time = t
    current_pos = pos

    fish[pos] += 1

    next_t = t + max(1, 1000 - fish[pos])
    heapq.heappush(heap, (next_t, pos))
