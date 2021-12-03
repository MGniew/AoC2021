import operator


def build_filter_fun(data, pos=0, op=operator.ge):
    s = sum(int(d[pos], 2) for d in data)
    if op(s, len(data) - s):
        to_be_left = "1"
    else:
        to_be_left = "0"

    def filter_fun(element):
        if element[pos] == to_be_left:
            return True
        return False

    return filter_fun


def main():
    with open("input") as f:
        data = f.read().splitlines()

    pos = 0
    oxygen = data[:]
    while len(oxygen) > 1:
        f_fun = build_filter_fun(oxygen, pos=pos, op=operator.ge)
        oxygen = list(filter(f_fun, oxygen))
        pos += 1

    pos = 0
    co2 = data[:]
    while len(co2) > 1:
        f_fun = build_filter_fun(co2, pos=pos, op=operator.lt)
        co2 = list(filter(f_fun, co2))
        pos += 1

    print(int(oxygen[0], 2) * int(co2[0], 2))


if __name__ == "__main__":
    main()
