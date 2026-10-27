import sys
import heapq

data = sys.stdin.read().split()
heap = []
res = []
pos = 0
while pos < len(data):
    line = data[pos]
    if line == 'ADD':
        heapq.heappush(heap, int(data[pos + 1]))
        pos += 2
    elif line == 'EXTRACT':
        res.append(str(heapq.heappop(heap)) if heap else 'CANNOT')
        pos += 1
    else:
        heap = []
        pos += 1

print('\n'.join(res))
