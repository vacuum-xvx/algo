n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

a.sort()

# < | >=
def first_equal(arr, x):
    l = -1
    r = len(arr)

    for _ in range(100):
        mid = (l + r) // 2

        if arr[mid] < x:
            l = mid
        else:
            r = mid

    return r

# <= | >
def first_higher(arr, x):
    l = -1
    r = len(arr)

    for _ in range(100):
        mid = (l + r) // 2

        if arr[mid] <= x:
            l = mid
        else:
            r = mid

    return r


for x in b:
    left = first_equal(a, x)
    right = first_higher(a, x)

    print(right - left, end=' ')