def increase_energy(data, by=1):
    return [[a+by for a in line] for line in data]


def flash(data):
    def generator_neigbours(x, y):
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i != 0 or j != 0:
                    if 10 > x+i >= 0 and 10 > y+j >= 0:
                        yield (x+i, y+j)

    to_be_checked = []
    for x, row in enumerate(data):
        for y, fish in enumerate(row):
            if fish > 9:
                data[x][y] = 0
                to_be_checked += list(generator_neigbours(x, y))

    while to_be_checked:
        x, y = to_be_checked.pop()
        if data[x][y] == 0:
            continue
        data[x][y] += 1
        if data[x][y] > 9:
            data[x][y] = 0
            to_be_checked += list(generator_neigbours(x, y))

    return data


def flash_generator(data, n=100):
    data = [[a for a in line] for line in data]
    for s in range(n):
        data = increase_energy(data)
        data = flash(data)
        yield sum([a == 0 for line in data for a in line])


def main():
    with open("input") as f:
        data = f.read().splitlines()
    data = [[int(a) for a in line] for line in data]

    print("Part 1:", sum(list(flash_generator(data))))

    for i, result in enumerate(flash_generator(data, n=10000)):
        if result == 100:
            print("Part 2:", i+1)
            break


if __name__ == "__main__":
    main()
