import time

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return bool(other.x == self.x and other.y == self.y)

    def __lt__(self, other):
        return bool(self.x <= other.x and self.y <= other.y)

    def __gt__(self, other):
        return bool(self.x > other.x and self.y > other.y)

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return f'({self.x}, {self.y})'


class Triangle:

    def __init__(self, points):
        self.points = points

    def distance(self, i, j):
        return ((self.points[i].x - self.points[j].x) ** 2 +
                (self.points[i].y - self.points[j].y) ** 2) ** 0.5

    def cost(self, i, j, k):
        return self.distance(i, j) + self.distance(j, k) + self.distance(i, k)

    def recursive(self, i, j):
        if j < i + 2:
            return 0
        cost = float('inf')
        for k in range(i + 1, j):
            cost = min(cost, self.recursive(i, k) + self.recursive(k, j) + self.cost(i, k, j))
        return cost

    def dynamic(self, n):
        if n < 3:
            return 0

        table = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            j = 0
            for k in range(i, n):
                if k < j + 2:
                    table[j][k] = 0
                else:
                    table[j][k] = 100000
                    for l in range(j + 1, k):
                        cost =  table[j][l] + table[l][k] + self.cost(j, k, l)
                        if table[j][k] > cost:
                            table[j][k] = cost
                j += 1
        return table[0][-1]


p1 = [[0, 0], [1, 0], [2, 1], [1, 2], [0, 2]]
p2 = [[0, 0], [4, 0], [5, 4], [4, 5], [2, 5], [1, 4], [0, 3], [0, 2]]
points1 = [Point(entry[0], entry[1]) for entry in p1]
points2 = [Point(entry[0], entry[1]) for entry in p2]

t = Triangle(points1)

t_start = time.perf_counter()
r = t.recursive(0, len(points1)-1)
t_stop = time.perf_counter()
print("Czas obliczeń rekurencyjnej wersji:", "{:.7f}".format(t_stop - t_start))
print('Koszt:', r)
print()
t_start = time.perf_counter()
r = t.dynamic(len(points1))
t_stop = time.perf_counter()
print("Czas obliczeń dynamicznej wersji:", "{:.7f}".format(t_stop - t_start))
print('Koszt:', r)
print()
print('-------------------------------------------------------------')
print()

t = Triangle(points2)

t_start = time.perf_counter()
r = t.recursive(0, len(points2)-1)
t_stop = time.perf_counter()
print("Czas obliczeń rekurencyjnej wersji:", "{:.7f}".format(t_stop - t_start))
print('Koszt:', r)
print()
t_start = time.perf_counter()
r = t.dynamic(len(points2))
t_stop = time.perf_counter()
print("Czas obliczeń dynamicznej wersji:", "{:.7f}".format(t_stop - t_start))
print('Koszt:', r)
