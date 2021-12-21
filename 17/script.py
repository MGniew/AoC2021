import math


def gauss_sum(n):
    return n * (n + 1) // 2


class Area:

    def __init__(self, x_min, x_max, y_min, y_max):
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max

    def __str__(self):
        return f"x={self.x_min}..{self.x_max}, y={self.y_min}..{self.y_max}"

    @staticmethod
    def from_file(filename):
        with open(filename) as f:
            data = f.read()

        x_min, x_max = data[data.find("x=")+2:data.find(",")].split("..")
        y_min, y_max = data[data.find("y=")+2:].split("..")
        return Area(
            x_min = int(x_min),
            x_max = int(x_max),
            y_min = int(y_min),
            y_max = int(y_max),
        )

    def is_probe_intersect(self, probe):
        return (
            probe.x >= self.x_min and probe.x <= self.x_max and
            probe.y >= self.y_min and probe.y <= self.y_max
        )

    def is_missed(self, probe):
        return probe.x > self.x_max or probe.y < self.y_min


class Probe:

    def __init__(self, x, y, v_x, v_y):
        self.x = x
        self.y = y
        self.v_x = v_x
        self.v_y = v_y

    def __str__(self):
        return f"p=({self.x},{self.y}), v=({self.v_x}..{self.v_y})"

    def step(self):
        self.x += self.v_x
        self.y += self.v_y
        self._update_speed()

    def _update_speed(self):
        if self.v_x != 0:
            self.v_x = self.v_x + 1 if self.v_x < 0 else self.v_x - 1
        self.v_y -= 1


def solve_part_1():
    """Solves part 1.

    - v_x is irrelevant as we are looking for max y
    - v_y_min is same as y_min
    - v_y_max is same as -y_min - 1
        - it is really unbounded in real space
        - it is bounded here as a probe that passed
          the area was not nessecery within (the speed cannot be to large)
        - -1 as the speed needs to be the same at a 0,0 point
          as the v_y_min (gravity - it took me a while)
    - v_y_max hits, so it must give the optimal solution
    """
    area = Area.from_file("input")
    return gauss_sum(-area.y_min - 1)


def solve_part_2():
    area = Area.from_file("input")

    def get_v_x_min(x_min):
        """Gets v_x_min from x_min
        
        gauss_sum(vx) >= xmin
        0 = v_x**2 + v_x - 2 * x_min
        """
        d = 1 + 8 * x_min
        return math.ceil((-1 + d**(1/2)) / 2)

    v_y_min = area.y_min
    v_y_max = -(area.y_min + 1)
    v_x_min = get_v_x_min(area.x_min)
    v_x_max = area.x_max

    solutions = list()

    for v_y in range(v_y_min, v_y_max + 1):
        for v_x in range(v_x_min, v_x_max + 1):
            probe = Probe(x=0, y=0, v_x=v_x, v_y=v_y)
            while not area.is_missed(probe):
                probe.step()
                if area.is_probe_intersect(probe):
                    solutions.append((probe.v_x, probe.v_y))
                    break
    return len(solutions)


def main():
    print("Part 1:", solve_part_1())
    print("Part 2:", solve_part_2())


if __name__ == "__main__":
    main()
