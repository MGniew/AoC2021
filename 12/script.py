from collections import defaultdict



def load_data(filename):
    with open(filename) as f:
        data = f.read().splitlines()

    result = defaultdict(list)
    for line in data:
        src, dst = line.split("-")
        result[src].append(dst)
        result[dst].append(src)
    return result


def solve_part_1(data):

    paths = []
    to_be_checked = [["start"]]
    while to_be_checked:
        item = to_be_checked.pop()
        for v in data[item[-1]]:
            if v.islower() and v in item:
                continue
            elif v == "end":
                paths.append(item + [v])
            else:
                to_be_checked.append(item + [v])

    return paths


def solve_part_2(data):

    paths = []
    to_be_checked = [["start"]]
    while to_be_checked:
        item = to_be_checked.pop()
        for v in data[item[-1]]:
            if v == "start":
                continue
            elif v.islower() and v in item:
                lowers = {l: item.count(l) for l in set(item) if l.islower()}
                if 2 in lowers.values():
                    continue
                else:
                    to_be_checked.append(item + [v])
            elif v == "end":
                paths.append(item + [v])
            else:
                to_be_checked.append(item + [v])

    return paths


def main():

    data = load_data("input")

    print("Solve part 1:", len(solve_part_1(data)))
    print("Solve part 2:", len(solve_part_2(data)))

if __name__ == "__main__":
    main()
