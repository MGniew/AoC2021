
def load_data(filename):
    with open(filename) as f:
        data = f.read().splitlines()

    coord_y, coord_x = [], []
    folds = []
    for line in data:
        if line.startswith("fold along"):
            value = int(line[line.find("=")+1:])
            if "y" in line:
                folds.append((value, -1))
            else:
                folds.append((-1, value))
        elif line:
            coord = line.split(",")
            coord_x.append(int(coord[0]))
            coord_y.append(int(coord[1]))

    max_x = max(coord_x) + 1
    coords = []
    for y in range(max(coord_y) + 1):
        sublist = [0] * max_x
        coords.append(sublist)

    for x, y in zip(coord_x, coord_y):
        coords[y][x] = 1

    return coords, folds


def fold(coords, fold):
    axis = 1 if fold[0] == -1 else 0
    axis_value_y = 0 if axis == 1 else fold[axis] + 1
    axis_value_x = 0 if axis == 0 else fold[axis] + 1

    if axis == 0:
        new_coords = [[value for value in line] for line in coords[:axis_value_y - 1]]
    else:
        new_coords = [[value for value in line[:axis_value_x - 1]] for line in coords]

    for y, row in enumerate(coords[axis_value_y:]):
        y += axis_value_y
        for x, value in enumerate(row[axis_value_x:]):
            x += axis_value_x
            if axis == 0:
                new_y = -y % (axis_value_y - 1)
                new_x = x
            else:
                new_x = -x % (axis_value_x - 1)
                new_y = y
            new_coords[new_y][new_x] |= coords[y][x] 

    return new_coords


def main():
    coords, folds = load_data("input")

    print("Part 1:")
    print(sum([value for line in fold(coords, folds[0]) for value in line]))

    print("Part 2:")
    for f in folds:
        coords = fold(coords, f)
    for line in coords:
        line = "".join([chr(176) if c else " " for c in line])
        print(line)



if __name__ == "__main__":
    main()

