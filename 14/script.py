from collections import defaultdict
import typing as tp

Rule = tp.NamedTuple("Rule", [('pattern', str), ('rule', int)])
Template = str


def load_data(filename: str) -> tp.Tuple[Template, tp.List[Rule]]:
    with open(filename) as f:
        data = f.read().splitlines()

    template = data[0]
    rules = [Rule(*line.split(" -> ")) for line in data[2:]]
    return template, rules


def apply_rules(template: Template, rules: tp.List[Rule]) -> Template:

    def _pattern_match(template, rule):
        result = []
        for i in range(len(template) - 1):
            if rule.pattern == template[i:i+2]:
                result.append((i + 1, rule.rule))
        return result

    def _insert_char(string, index, char):
        return string[:index] + char + string[index:]

    matchings = list()
    for rule in rules:
        matchings += _pattern_match(template, rule)

    matchings = sorted(matchings, reverse=True, key=lambda x: x[0])
    for match in matchings:
        template = _insert_char(template, match[0], match[1])

    return template


def solve_naive(template, rules, steps=10):
    for i in range(steps):
        template = apply_rules(template, rules)

    freq = [template.count(i) for i in set(template)]
    freq = sorted(freq, reverse=True)
    return freq[0] - freq[-1]


def solve_smart(template, rules, steps=40):

    rules = {r.pattern: r.rule for r in rules}
    pair_counts = defaultdict(int)
    letter_counts = defaultdict(int)

    for l in template:
        letter_counts[l] += 1

    for i in range(len(template) - 1):
        pair = template[i: i+2]
        pair_counts[pair] += 1

    for step in range(steps):
        pair_counts_new = pair_counts.copy()
        for pair, counts in pair_counts.items():
            if pair not in rules:
                continue
            rule_value = rules[pair]
            half_1, half_2 = pair
            pair_counts_new[pair] -= counts
            pair_counts_new[half_1 + rule_value] += counts
            pair_counts_new[rule_value + half_2] += counts
            letter_counts[rule_value] += counts
        pair_counts = pair_counts_new

    freq = sorted(letter_counts.items(), reverse=True, key=lambda x: x[1])
    return freq[0][1] - freq[-1][1]


def main():
    template, rules = load_data("input")
    assert solve_naive(template, rules, 10) == solve_smart(template, rules, 10)
    print("Part1:", solve_smart(template, rules, 10))
    print("Part2:", solve_smart(template, rules, 40))


if __name__ == "__main__":
    main()
