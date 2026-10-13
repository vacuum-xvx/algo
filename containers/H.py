import sys
from collections import deque

left = deque()
right = deque()
ans = []

n = int(sys.stdin.readline())

for _ in range(n):
    com = sys.stdin.readline().split()

    if com[0] == '+':
        right.append(int(com[1]))

    elif com[0] == '*':
        right.appendleft(int(com[1]))

    elif com[0] == '-':
        ans.append(str(left.popleft()))

    if len(left) < len(right):
        left.append(right.popleft())

sys.stdout.write('\n'.join(ans))