import math
import statistics as st


def get_used_fuel(x):
    return ((x + 1) * x) / 2


def main():
    with open("input") as f:
        data = [int(d) for d in f.read().split(",")]
    median = st.median(data)
    print("Part 1:")
    print(int(sum([abs(d - median) for d in data])))

    mean = st.mean(data)
    mean_up = int(mean - 1/2)
    mean_down = int(mean + 1/2)

    print("Part 2:")
    a = sum([get_used_fuel(abs(d - mean_up)) for d in data])
    b = sum([get_used_fuel(abs(d - mean_down)) for d in data])
    print(int(min((a, b))))


if __name__ == "__main__":
    main()
