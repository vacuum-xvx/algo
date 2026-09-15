class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_squared(self):
        return self.x ** 2 + self.y ** 2


if __name__ == '__main__':
    n = int(input())
    points = []

    for _ in range(n):
        x, y = map(int, input().split())
        points.append(Point(x, y))

    for i in range(n):
        for j in range(i + 1, n):
            if points[i].distance_squared() > points[j].distance_squared():
                points[i], points[j] = points[j], points[i]

    for p in points:
        print(p.x, p.y)
