
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __truediv__(self, other):
        if isinstance(other, float):
            return Vector(self.x/other, self.y/other)
        raise NotImplementedError

    def normalize(self):
        length = (self.x**2 + self.y**2)**(1/2)
        result = self / length

        if abs(result.x) == abs(result.y):
            result.x /= abs(result.x)
            result.y /= abs(result.y)
        return result

    def __str__(self):
        return (f"Vector({self.x}, {self.y})")

    __repr__ = __str__


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return Vector(
            self.x - other.x,
            self.y - other.y
        )

    def copy(self):
        return Point(self.x, self.y)

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __hash__(self):
        return hash((self.x, self.y))

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return (f"Point({self.x}, {self.y})")

    __repr__ = __str__


class Line:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_covered_points(self):
        dir_vec = self._get_dir_vector()

        points = [self.a]
        pos = self.a.copy()
        while pos != self.b:
            pos += dir_vec
            if pos.x.is_integer() and pos.y.is_integer():
                points.append(pos)
        return points

    def _get_dir_vector(self):
        vec = (self.b - self.a).normalize()
        return vec

    def is_parallel_to_axis(self):
        return self.a.x == self.b.x or self.a.y == self.b.y

    def is_diagonal(self):
        return abs(self.a.x - self.b.x) == abs(self.a.y - self.b.y)

    def __str__(self):
        return (f"Line({self.a} -> {self.b})")

    __repr__ = __str__
        

def load(input_file):

    with open(input_file) as f:
        data = f.read().splitlines()

    lines = list()
    for record in data:
        record = record.replace(" -> ", ",").split(",")
        point_a = Point(*[float(el) for el in record[:2]])
        point_b = Point(*[float(el) for el in record[2:]])
        lines.append(Line(point_a, point_b))

    return lines


def solve_part_1(lines):

    intersections = dict()

    for line in lines:
        if not line.is_parallel_to_axis():
            continue
        points = line.get_covered_points()
        for p in points:
            if p in intersections:
                intersections[p] += 1
            else:
                intersections[p] = 1


    i = 0
    for k, v in intersections.items():
        if v >= 2:
            i+= 1
        
    print("Part 1: ", i)


def solve_part_2(lines):

    intersections = dict()

    for line in lines:
        points = line.get_covered_points()
        for p in points:
            if p in intersections:
                intersections[p] += 1
            else:
                intersections[p] = 1


    i = 0
    for k, v in intersections.items():
        if v >= 2:
            i+= 1
        
    print("Part 2: ", i)


def main():

    lines = load("input")
    solve_part_1(lines)
    solve_part_2(lines)


if __name__ == "__main__":
    main()
