import sys
import heapq

data = sys.stdin.read().split()
heap = []
out = []
pos = 0
while pos < len(data):
    cmd = data[pos]
    if cmd == 'ADD':
        heapq.heappush(heap, -int(data[pos + 1]))
        pos += 2
    elif cmd == 'EXTRACT':
        out.append(str(-heapq.heappop(heap)) if heap else 'CANNOT')
        pos += 1
    else:
        heap = []
        pos += 1

print('\n'.join(out))
