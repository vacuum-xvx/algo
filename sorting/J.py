import sys

lines = [line.strip() for line in sys.stdin if line.strip() != '']
n = len(lines)

for i in range(n):
    for j in range(n - 1 - i):
        a, b = lines[j], lines[j + 1]
        if a + b < b + a:
            lines[j], lines[j + 1] = lines[j + 1], lines[j]

print(''.join(lines))