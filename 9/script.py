import itertools
from string import ascii_lowercase
from functools import reduce


def name_generator():
    size = 1
    while True:
        for name in itertools.product(ascii_lowercase, repeat=size):
            yield "".join(name)
        size += 1


def load_data(filename="input"):
    with open(filename) as f:
        data = f.read().splitlines()
    data = [[int(el) for el in list(d)] for d in data]
    return data


def locate_minima(data):
    result = []
    for x in range(len(data)):
        for y in range(len(data[0])):
            l = True if y-1 < 0 else data[x][y] < data[x][y-1]
            u = True if x-1 < 0 else data[x][y] < data[x-1][y] 
            d = True if x+1 >= len(data) else data[x][y] < data[x+1][y]
            r = True if y+1 >= len(data[0]) else data[x][y] < data[x][y+1]
            if all((l, u, d, r)):
                result.append((x ,y))
    return result


def fill_water(x, y, symbol, data, current_result):
    
    if (x < 0 or x >= len(data)) or (y < 0 or y >= len(data[0])):
        return current_result
    if (x, y) in [item for sublist in current_result.values() for item in sublist]:
        return current_result

    if data[x][y] < 9:
        current_result[symbol] += [(x, y)]
    else:
        return current_result

    current_result = fill_water(x-1, y, symbol, data, current_result)
    current_result = fill_water(x+1, y, symbol, data, current_result)
    current_result = fill_water(x, y-1, symbol, data, current_result)
    current_result = fill_water(x, y+1, symbol, data, current_result)

    return current_result

def solve_part_2(data):
    """Solve part2 using ~watershed algorithm."""
    minima = {
        _min: name for _min, name in zip(locate_minima(data), name_generator())
    }

    result = dict()
    for _min, symbol in minima.items():
        result[symbol] = list()
        result = fill_water(_min[0], _min[1], symbol, data, result)

    result = {k: len(v) for k, v in result.items()}
    result = sorted(result.items(), key=lambda x: x[1], reverse=True)
    result = reduce((lambda x, y: x * y), [y for x, y in result[:3]])
    return result
        
        
def solve_part_1(data):
    minima = locate_minima(data)
    _sum = 0
    for x, y in minima:
        _sum += data[x][y] + 1
    return _sum


def main():

    data = load_data()

    print("Part1: ", solve_part_1(data))
    print("Part2: ", solve_part_2(data))


if __name__ == "__main__":
    main()


