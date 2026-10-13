from collections import deque

n, k = map(int, input().split())
arr = list(map(int, input().split()))
queue = deque()

for item in range(n):
    # Удаляем элементы из стека, которые больше текущего элемента,
    # чтобы не упасть с ошибкой проверяем что стек не пуст
    while queue and arr[queue[-1]] > arr[item]:
        queue.pop()

    queue.append(item)

    # Удаляем элементы из стека, которые не входят в текущий диапазон окна
    while queue and queue[0] <= item - k:
            queue.popleft()

    # После достижения размера окна k, выводим минимальный элемент в текущем окне
    # На всех итерациях после этой будет выводиться мин элемент, тк
    # Окно сдвигается (+1 вправо -1 влево)
    if item >= k - 1:
        print(arr[queue[0]], end='\n')