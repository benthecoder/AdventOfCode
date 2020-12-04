def main():
    with open("map.txt") as f:
        grid = f.read().splitlines()

    print(f"Part 1: {sol_1(grid)} trees \nPart 2: {sol_2(grid)} trees")


def tree_detect(grid, dr, dc):
    r, c, count = 0, 0, 0

    while r + 1 < len(grid):
        r += dr
        c += dc
        if grid[r][c % len(grid[0])] == "#":
            count += 1

    return count


def sol_1(grid):
    return tree_detect(grid, 1, 3)


def sol_2(grid):
    slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
    prod = 1

    for s in slopes:
        prod *= tree_detect(grid, s[0], s[1])

    return prod


if __name__ == '__main__':
    main()
