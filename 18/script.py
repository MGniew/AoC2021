import copy
import itertools
import json
import math


class Node:

    def __init__(self, left, right, parent):
        self.right = right
        self.left = left
        self.parent = parent

        if isinstance(right, list):
           self.right = Node(right[0], right[1], self)
        if isinstance(left, list):
           self.left = Node(left[0], left[1], self)

    def __str__(self):
        return f"[{self.left},{self.right}]"

    @staticmethod
    def from_str(string):
        data = json.loads(string)
        return Node(data[0], data[1], None)

    def __add__(self, other):
        result = Node(copy.deepcopy(self), copy.deepcopy(other), None)
        result.left.parent = result
        result.right.parent = result
        result.reduce()
        return result

    def magnitude(self):
        
        if isinstance(self.left, int): 
            left_magnitude = self.left
        else:
            left_magnitude = self.left.magnitude()

        if isinstance(self.right, int): 
            right_magnitude = self.right
        else:
            right_magnitude = self.right.magnitude()

        return 3 * left_magnitude + 2 * right_magnitude

    def reduce(self):
        while True:
            if self.explode():
                continue
            if self.split():
                continue
            break

    def _explosion(self):
        
        # left
        number = self.left
        node = self
        while node.parent is not None:
            if node is node.parent.left:
                node = node.parent
            elif node is node.parent.right:
                if isinstance(node.parent.left, int):
                    node.parent.left += number
                    break
                else:
                    right = node.parent.left
                    while not isinstance(right.right, int):
                        right = right.right
                    right.right += number
                    break

        # right
        number = self.right
        node = self
        while node.parent is not None:
            if node is node.parent.right:
                node = node.parent
            elif node is node.parent.left:
                if isinstance(node.parent.right, int):
                    node.parent.right += number
                    break
                else:
                    left = node.parent.right
                    while not isinstance(left.left, int):
                        left = left.left
                    left.left += number
                    break

        if self.parent.left is self:
            self.parent.left = 0
        else:
            self.parent.right = 0


    def explode(self, depth=0):
        if depth < 4:
            explosion = False
            if isinstance(self.left, Node):
                explosion = self.left.explode(depth + 1)

            if not explosion and isinstance(self.right, Node):
                explosion = self.right.explode(depth + 1)
        else:
            self._explosion()
            return True

        return explosion

    def split(self):
        splitted = False
        if isinstance(self.left, int):
            if self.left >= 10:
                self.left = Node(
                    math.floor(self.left/2),
                    math.ceil(self.left/2),
                    self
                )
                splitted =  True
        else:
            splitted = self.left.split()

        if splitted:
            return True

        if isinstance(self.right, int):
            if self.right >= 10:
                self.right = Node(
                    math.floor(self.right/2),
                    math.ceil(self.right/2),
                    self
                )
                splitted = True
        else:
            splitted = self.right.split()
        return splitted


def snailfish_number_generator(filename):
    with open(filename) as f:
        data = f.read().splitlines()
    for line in data:
        yield Node.from_str(line)


def solve_part_1():
    numbers = snailfish_number_generator("input")
    result = next(numbers)
    for n in numbers:
        result += n
    return result.magnitude()


def solve_part_2():
    m_max = 0
    numbers = snailfish_number_generator("input")
    for a, b in itertools.permutations(numbers, 2):
        m = (a + b).magnitude()
        if m > m_max:
            m_max = m
    return m_max


def main():
    print("Part 1", solve_part_1())
    print("Part 2", solve_part_2())
    

if __name__ == "__main__":
    main()
