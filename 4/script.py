class Board:

    def __init__(self, numbers):
        self.numbers = numbers
        self.mask = [[False for c in row] for row in numbers]
        self.last_value = None

    def calculate_score(self):
        marked = 0
        for x, row in enumerate(self.mask):
            for y, col_value in enumerate(row):
                if not col_value:
                    marked += self.numbers[x][y]
        return marked * self.last_value

    def mark(self, value):
        self.last_value = value
        for x, row in enumerate(self.numbers):
            for y, col_value in enumerate(row):
                if value == col_value:
                    self.mask[x][y] = True

    def bingo(self):
        rows = any([all(row) for row in self.mask])
        columns = any([all(col) for col in zip(*self.mask)])
        return rows or columns


class Game:
    def __init__(self, boards):
        self.boards = boards

    def next_round(self, value):

        winners = []
        for b in self.boards:
            b.mark(value)
            is_bingo = b.bingo()
            if is_bingo:
                winners.append(b)

        return winners

    def remove_boards(self, boards):
        self.boards = [b for b in self.boards if b not in boards]

    def boards_left(self):
        return len(self.boards)


def load_game(input_file):
    with open(input_file) as f:
        data = f.read().splitlines()

    randoms = [int(n) for n in data[0].split(",")]
    boards = list()
    numbers = list()
    for line in data[2:]:
        if line:
            numbers.append([int(n) for n in line.split()])
        else:
            boards.append(Board(numbers))
            numbers = list()

    return Game(boards), randoms


def main():

    # Part 1
    game, randoms = load_game("input")

    for random in randoms:
        winners = game.next_round(random)
        if winners:
            break
    print(winners[0].calculate_score())

    # Part 2
    game, randoms = load_game("input")

    for random in randoms:
        winners = game.next_round(random)
        game.remove_boards(winners)
        if game.boards_left() == 0:
            break

    print(winners[-1].calculate_score())


if __name__ == "__main__":
    main()
