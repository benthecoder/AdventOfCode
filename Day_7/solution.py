import re
import collections


def read_file(file):
    with open(file) as f:
        file = f.read().splitlines()
    return file


def sol_1(inv_rules, color='shiny gold'):
    queue, reachable = collections.deque([color]), set()

    while queue:
        color = queue.pop()
        for c in inv_rules.get(color, []):
            # print(c)
            if c not in reachable:
                reachable.add(c)
                queue.appendleft(c)
                # print(f"{reachable}\n")
                # print(f"{queue}\n")

    return len(reachable)


def sol_2(rules, color="shiny gold"):
    return sum(number + number * sol_2(rules, c) for c, number in rules[color].items())


def main():
    rules_file = read_file("input.txt")

    rules, inv_rules = {}, {}

    for rule in rules_file:
        color, cl_rule = rule.split(' bags contain ')
        rules[color] = {color: int(number) for number, color in re.findall(
            '(\d+) (\w+ \w+)', cl_rule)}
        for c in rules[color]:
            inv_rules[c] = inv_rules.get(c, []) + [color]

    print(inv_rules['shiny gold'])
    # print(rules['shiny gold'].items())
    # print(rules['pale aqua'])
    print(f'Part 1: {sol_1(inv_rules)}\nPart 2: {sol_2(rules)}')


if __name__ == "__main__":
    main()
