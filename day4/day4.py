def parse_input(file_name):
    lines = open(file_name).readlines()
    return [list(line.strip()) for line in lines]


def find(grid, patterns, word_rotations):
    result = 0
    for x in range(len(grid[0])):
        for y in range(len(grid)):
            for pattern in patterns:
                try:
                    word = ''.join([grid[y + dy][x + dx] for dx, dy in pattern])
                    if word in word_rotations:
                        result += 1
                except IndexError:
                    # Ugly, but it works. Did not want to think about it too much
                    pass

    return result


def part1(grid):
    patterns = [
        [[0, 0], [1, 0], [2, 0], [3, 0]],  # Horizontal
        [[0, 0], [0, 1], [0, 2], [0, 3]],  # Vertical
        [[0, 0], [1, 1], [2, 2], [3, 3]],  # Down-right
        [[0, 3], [1, 2], [2, 1], [3, 0]],  # Up-right
    ]
    word_rotations = ['XMAS', 'SAMX']
    return find(grid, patterns, word_rotations)


def part2(grid):
    patterns = [
        # M.S
        # .A.
        # M.S
        [[0, 0], [1, 1], [2, 2], [0, 2], [1, 1], [2, 0]],  # Cross
    ]
    word_rotations = ['MASMAS', 'SAMSAM', 'MASSAM', 'SAMMAS']
    return find(grid, patterns, word_rotations)


def run():
    inp = parse_input('day4/input.txt')

    print("Part 1: ", part1(inp))
    print("Part 2: ", part2(inp))
