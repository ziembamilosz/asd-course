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


class ConvexHull:

    def __init__(self, points):
        self.points = points

    def orientation(self, p, q, r):
        return (q.y - p.y) * (r.x - q.x) - (r.y - q.y) * (q.x - p.x)

    def get_next_index(self, p):
        return (self.points.index(p) + 1) % len(self.points)

    def find_polygon(self):
        start = min(self.points)
        p = start
        polygon = [p]
        while True:
            q = self.points[self.get_next_index(p)]
            for r in self.points:
                if self.orientation(p, r, q) < 0:
                    q = r
            p = q
            if p == start:
                break
            polygon.append(q)
        return polygon

    def find_polygon_v2(self):
        start = min(self.points)
        p = start
        polygon = [p]
        while True:
            q = self.points[self.get_next_index(p)]
            for r in self.points:
                if self.orientation(p, r, q) == 0:
                    if p.x < q.x < r.x and p.y == q.y == r.y:
                        q = r
                    elif p.y > q.y > r.y and p.x == q.x == r.x:
                        q = r
                elif self.orientation(p, r, q) < 0:
                    q = r
            p = q
            if p == start:
                break
            polygon.append(p)
        return polygon


p1 = [(0, 3), (0, 0), (0, 1), (3, 0), (3, 3)]
p2 = [(0, 3), (0, 1), (0, 0), (3, 0), (3, 3)]
p3 = [(2, 2), (4, 3), (5, 4), (0, 3), (0, 2), (0, 0), (2, 1), (2, 0), (4, 0)]
points1 = [Point(x, y) for x, y in p1]
points2 = [Point(x, y) for x, y in p2]
points3 = [Point(x, y) for x, y in p3]

# c = ConvexHull(points1)
# r = c.find_polygon()
# print('v1:', r)
# c = ConvexHull(points1)
# r = c.find_polygon_v2()
# print('v2:', r)
#
# print()
#
# c = ConvexHull(points2)
# r = c.find_polygon()
# print('v1:', r)
# c = ConvexHull(points2)
# r = c.find_polygon_v2()
# print('v2:', r)
#
# print()

c = ConvexHull(points3)
r = c.find_polygon()
print(r)
c = ConvexHull(points3)
r = c.find_polygon_v2()
print(r)
