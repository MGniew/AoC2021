# 1: 2
# 7: 3
# 4: 4
# 2: 5
# 3: 5
# 5: 5
# 0: 6
# 6: 6
# 9: 6
# 8: 7

#  aaaa
# b    c
# b    c
#  dddd
# e    f
# e    f
#  gggg


def find_pattern(signal):
    patterns = {i: "" for i in range(10)}
    for d in signal:
        if len(d) == 2:
            patterns[1] = set(d)
        elif len(d) == 3:
            patterns[7] = set(d)
        elif len(d) == 4:
            patterns[4] = set(d)
        elif len(d) == 7:
            patterns[8] = set(d)

    a_line = patterns[7] - patterns[1]
    for s in signal:
        if len(s) == 6 and a_line | patterns[4] <= set(s):
            patterns[9] = set(s)
    g_line = patterns[9] - patterns[4] - set(a_line)
    e_line = patterns[8] - patterns[9]

    zero_and_six = [
        set(s) for s in signal if len(s) == 6 and set(s) != patterns[9]
    ]
    if zero_and_six[0] - zero_and_six[1] <= patterns[1]:
        patterns[0] = zero_and_six[0]
        patterns[6] = zero_and_six[1]
    else:
        patterns[0] = zero_and_six[1]
        patterns[6] = zero_and_six[0]

    c_line = patterns[0] - patterns[6]
    d_line = patterns[6] - patterns[0]

    patterns[2] = a_line | c_line | d_line | g_line | e_line
    f_line = patterns[1] - c_line
    b_line = patterns[8] - patterns[2] - f_line

    _map = {
        a_line.pop(): "a",
        b_line.pop(): "b",
        c_line.pop(): "c",
        d_line.pop(): "d",
        e_line.pop(): "e",
        f_line.pop(): "f",
        g_line.pop(): "g",
    }
    return _map


def load_data(filename="input"):
    with open(filename) as f:
        data = f.read().splitlines()

    data = [line.split("|") for line in data]
    data = [(line[0].split(), line[1].split()) for line in data]
    return data


def solve_part_2(data):
    pattern_to_digit = {
        "abcefg": 0,
        "cf": 1,
        "acdeg": 2,
        "acdfg": 3,
        "bcdf": 4,
        "abdfg": 5,
        "abdefg": 6,
        "acf": 7,
        "abcdefg": 8,
        "abcdfg": 9,
    }

    result = 0
    for signals, digits in data:
        _map = find_pattern(signals)
        new_digits = list(map(
            lambda x: "".join(sorted([_map[el] for el in x])),
            digits
        ))
        new_digits = [pattern_to_digit[d] for d in new_digits]
        mult = 1000
        for d in new_digits:
            result += d * mult
            mult /= 10

    return result


def solve_part_1(data):

    result = {k: 0 for k in [2, 3, 4, 7]}
    _map = {
        2: 1,
        3: 7,
        4: 4,
        7: 8,
    }
    for signals, digits in data:
        for d in digits:
            if len(d) in result.keys():
                result[len(d)] += 1
    result = {_map[k]: v for k, v in result.items()}
    return sum(result.values())


def main():

    data = load_data()
    print("Part 1: ,", solve_part_1(data))
    print("Part 1: ,", solve_part_2(data))


if __name__ == "__main__":
    main()
