def main():
    with open("input.txt") as f:
        data = [int(e) for e in f.read().splitlines()]
    
    ws = 3
    data = [sum(data[i: i + ws]) for i in range(len(data) - ws + 1)]
    data = [(y - x > 0) for x, y in zip(data[:-1], data[1:])]
    print(sum(data))


if __name__ == "__main__":
    main()
