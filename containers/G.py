n = int(input())
trains = list(map(int, input().split()))

stack = []
need = 1

for train in trains:
    stack.append(train)

    while stack and stack[-1] == need:
        stack.pop()
        need += 1

if not stack:
    print("YES")
else:
    print("NO")
