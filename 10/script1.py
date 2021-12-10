
def wrong_chunk_generator(data):

    def match(open_char, close_char):
        if (
            ord(open_char) + 2 == ord(close_char) or
            ord(open_char) + 1 == ord(close_char)
        ):
            return True
        return False

    for line in data:
        queue = []

        for char in line:
            if char in "{([<":
                queue.append(char)
            elif char in "})]>":
                prev_char = queue.pop()
                if not match(prev_char, char):
                    yield char
                    break


def solve_part_1(data):
    _map = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }
    return sum([_map[wc] for wc in wrong_chunk_generator(data)])


def main():

    with open("input") as f:
        data = f.read().splitlines()
    print("Part 1:", solve_part_1(data))


if __name__ == "__main__":
    main()
