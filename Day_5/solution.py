def read_file(file):
    with open(file, 'r') as f:
        file = f.read().splitlines()
    return file


def solution(seats):
    seatIDs = set()
    for seat in seats:
        row = int(seat[:7].replace('F', '0').replace('B', '1'), 2)
        col = int(seat[-3:].replace('L', '0').replace('R', '1'), 2)
        seatIDs.add(row * 8 + col)

    part1 = max(seatIDs)

    part2 = [seat for seat in range(
        min(seatIDs), max(seatIDs)) if seat not in seatIDs][0]

    return part1, part2


def main():
    seats = read_file("input.txt")

    part1, part2 = solution(seats)

    print(f"Part 1: {part1}\nPart 2: {part2}")


if __name__ == "__main__":
    main()
