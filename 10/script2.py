
def incomplete_queue_generator(data):

    def match(open_char, close_char):
        return (
            ord(open_char) + 2 == ord(close_char) or
            ord(open_char) + 1 == ord(close_char)
        )

    for line in data:
        queue = []

        for char in line:
            if char in "{([<":
                queue.append(char)
            elif char in "})]>":
                prev_char = queue.pop()
                if not match(prev_char, char):
                    queue = []
                    break
        if queue:
            yield queue


def solve_part_2(data):
    _map = {
        "(": 1,
        "[": 2,
        "{": 3,
        "<": 4,
    }

    scores = []
    for queue in incomplete_queue_generator(data):
        score = 0
        while queue:
            score = 5 * score + _map[queue.pop()]
        scores.append(score)

    return sorted(scores)[len(scores)//2]


def main():

    with open("input") as f:
        data = f.read().splitlines()
    print("Part 2:", solve_part_2(data))


if __name__ == "__main__":
    main()
