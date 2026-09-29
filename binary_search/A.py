n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return 'YES'
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return 'NO'

for x in b:
    print(binary_search(a, x))