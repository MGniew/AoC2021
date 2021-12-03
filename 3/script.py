def get_gamma(data):
    pos_to_count = {}
    for i in range(len(data[0])):
        pos_to_count[i] = {
            "0": 0,
            "1": 0,
        }
        for s in data:
            pos_to_count[i][s[i]] += 1

    gamma = ""
    epsilon = ""
    for k, v in pos_to_count.items():
        if v["1"] > v["0"]:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"

    return int(gamma, 2), int(epsilon, 2)


def main():
    with open("input") as f:
        data = f.read().splitlines()

    gamma, epsilon = get_gamma(data)


if __name__ == "__main__":
    main()
