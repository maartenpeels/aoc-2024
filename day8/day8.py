def parse_input(file_name):
    lines = [list(line.strip()) for line in open(file_name).readlines()]
    return lines


def parse_grid(grid):
    antennas = {}
    for row, _row in enumerate(grid):
        for col, cell in enumerate(_row):
            if cell != '.':
                if cell not in antennas:
                    antennas[cell] = []
                antennas[cell].append((row, col))
    return antennas


def find_antinode(antenna1, antenna2):
    dy = antenna2[0] - antenna1[0]
    dx = antenna2[1] - antenna1[1]

    return antenna1[0] - dy, antenna1[1] - dx

def is_colinear(point, antenna1, antenna2):
    return (antenna1[0] - point[0]) * (antenna2[1] - point[1]) == (antenna1[1] - point[1]) * (antenna2[0] - point[0])


def is_valid_position(row, col, grid):
    return 0 <= row < len(grid) and 0 <= col < len(grid[0])


def part1(grid, antennas):
    result = 0

    for key, antenna in antennas.items():
        for antenna1 in antenna:
            for antenna2 in antenna:
                if antenna1 == antenna2:
                    continue
                antinode = find_antinode(antenna1, antenna2)
                if not is_valid_position(antinode[0], antinode[1], grid):
                    continue
                result += 1

    return result


def part2(grid, antennas):
    result = 0

    for key, antenna_list in antennas.items():
        if len(antenna_list) < 2:
            continue

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                for antenna1 in antenna_list:
                    for antenna2 in antenna_list:
                        if antenna1 == antenna2:
                            continue
                        if is_colinear((row, col), antenna1, antenna2):
                            result += 1
                            break

    return result


def run():
    grid = parse_input('day8/input.txt')
    antennas = parse_grid(grid)

    print("Part 1: ", part1(grid, antennas))
    print("Part 2: ", part2(grid, antennas))
