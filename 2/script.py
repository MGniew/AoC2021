with open("input") as f:
    data = f.read().splitlines()

data = [line.split() for line in data]
data = [(line[0], int(line[1])) for line in data]
forward = sum([d[1] for d in data if d[0] == "forward"])
up_down = sum(
    [d[1] * -1 if d[0] == "up" else d[1] for d in data if d[0] != "forward"]
)

print("Result (part1): ", up_down * forward)


# part2
aim, up_down, forward = 0, 0, 0
for direction, value in data:
    if direction != "forward":
        aim += -1 * value if direction == "up" else value
    else:
        forward += value
        up_down += aim * value

print("Result (part2): ", up_down * forward)
