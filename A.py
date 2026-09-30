n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

def binary_search(arr, target):
    left, right = -1, len(arr)
    while right - left > 1:
        mid = (left + right) // 2
        if arr[mid] == target:
            return 'YES'
        elif arr[mid] < target:
            left = mid
        else:
            right = mid
    return 'NO'

for x in b:
    print(binary_search(a, x))