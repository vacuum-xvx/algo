n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def nearest(arr, x):
    l = -1
    r = len(arr)

    while r - l > 1:
        m = (l + r) // 2
        if arr[m] < x:
            l = m
        else:
            r = m

    if l == -1:
        return arr[r]

    if r == len(arr):
        return arr[l]

    if x - arr[l] <= arr[r] - x:
        return arr[l]
    else:
        return arr[r]

for x in b:
    print(nearest(a, x))