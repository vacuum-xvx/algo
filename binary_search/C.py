c = float(input())

def f(x):
    return x**2 + x**0.5

l, r = 0, 100_000

for _ in range(100):
    m = (l + r) / 2

    if f(m) < c:
        l = m
    else:
        r = m

print(m)