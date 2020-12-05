# read txt file and return necessary elements
def read(line):
    string = line.rstrip().replace(':', '').split(' ')
    num_1, num_2 = map(int, string[0].split('-'))
    letter = string[1]
    pw = string[2]
    return num_1, num_2, letter, pw

# Part 1 solution


def sol_1(line):
    min, max, letter, pw = read(line)
    if min <= pw.count(letter) <= max:
        return 1
    return 0

# Part 2 solution


def sol_2(line):
    pos_1, pos_2, letter, pw = read(line)
    if (pw[pos_1 - 1] == letter) != (pw[pos_2 - 1] == letter):
        return 1
    return 0

# returns count for part 1 and 2


def main():
    count_1, count_2 = 0, 0
    with open("input.txt", "r") as f:
        for line in f:
            count_1 += sol_1(line)
            count_2 += sol_2(line)
    print(f"Part 1: {count_1} \nPart 2: {count_2}")


if __name__ == "__main__":
    main()
