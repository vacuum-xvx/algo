a, b, c, d = map(int, input().split())

def f(x):
    return a*x**3 + b*x**2 + c*x + d

l, r = -10000, 10000

for _ in range(100):
    m = (l + r) / 2

    if f(l) * f(m) <= 0:
        r = m
    else:
        l = m

print(m)