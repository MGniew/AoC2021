def solve(data, days):
    data = data.copy()
    for d in range(days):
        for k in sorted(data.keys()):
            data[k - 1] = data[k]
        data[8] = data[-1]
        data[6] += data[-1]
        data.pop(-1)

    print(sum(data.values()))

def main():
    with open("input") as f:
        data = [int(el) for el in f.read().split(",")]
    data = {el: data.count(el) for el in range(9)}
    solve(data, days=80)
    solve(data, days=256)


if __name__ == "__main__":
    main()
