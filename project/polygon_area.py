import math

class Vertex:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    
    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def angle(self, other):
        x = self.x - other.x
        y = self.y - other.y
        angle = math.atan2(y, x)
        if angle <= 0:
            angle += 2 * math.pi

        return angle

    def __lt__(self, other):
        angle1 = self.angle(Vertex(0, 0))
        angle2 = other.angle(Vertex(0, 0))

        if angle1 < angle2:
            return True

        if angle1 == angle2 and Vertex(0, 0).distance(self) < Vertex(0, 0).distance(other):
            return True

        return False

"""
Сортировка набора вершин в порядке обхода по часовой стрелке.

vertices: Список вершин многоугольника, перечисленных по часовой стрелке.
"""
def sortPointsClockwise(vertices: list[Vertex]):
    center = Vertex(sum([v.x for v in vertices]) / len(vertices), sum([v.y for v in vertices]) / len(vertices))
    normalized_vertices = vertices.copy()
    for point in normalized_vertices:
        point.x -= center.x
        point.y -= center.y

    normalized_vertices.sort(reverse=True)
    for point in normalized_vertices:
        point.x += center.x
        point.y += center.y

    return normalized_vertices

"""
Площадь простого плоского многоугольника по формуле шнурования.

vertices: Список вершин многоугольника, перечисленных по часовой стрелке.
"""
def shoelace(vertices: list[Vertex]):
    sorted_vertices = sortPointsClockwise(vertices)

    area = 0.0
    for i in range(len(sorted_vertices)-1):
        area += 0.5 * (sorted_vertices[i].x * sorted_vertices[i+1].y - sorted_vertices[i+1].x * sorted_vertices[i].y)

    area += 0.5 * (sorted_vertices[-1].x * sorted_vertices[0].y - sorted_vertices[0].x * sorted_vertices[-1].y)

    return abs(area)

if __name__ == '__main__':
    n = int(input())
    vertices = list()
    for i in range(n):
        x, y = map(float, input().split())
        vertices.append(Vertex(x, y))

    print(shoelace(vertices))