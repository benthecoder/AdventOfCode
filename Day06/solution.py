def read_file(file):
    with open(file) as f:
        file = f.read().replace('\n\n', '|').replace('\n', ' ').split('|')
    return file


def sol_1(answer):
    return len(set(answer.replace(' ', '')))


def sol_2(answer):
    return len(set.intersection(*map(set, answer.split())))


def main():
    part1, part2 = 0, 0
    answers = read_file("input.txt")

    for answer in answers:
        part1 += sol_1(answer)
        part2 += sol_2(answer)

    print(f"Part 1: {part1}\nPart 2: {part2}")


if __name__ == "__main__":
    main()
