def main():

    with open("input.txt") as f:
        data = [int(e) for e in f.read().splitlines()]

    data = [(y - x > 0) for x, y in zip(data[:-1], data[1:])]
    print(sum(data))


if __name__ == "__main__":
    main()
