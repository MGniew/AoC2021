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



def main():
    
    template, rules = load_data("input")
    for i in range(10):
        template = apply_rules(template, rules)

    freq = [template.count(i) for i in set(template)]
    freq = sorted(freq, reverse=True)
    print("Part1:", freq[0] - freq[-1])


if __name__ == "__main__":
    main()
