WORD = 'XMAS'


class Grid:
    def __init__(self, grid):
        self.grid = grid

    # part 1
    def find_occurrences(self, word, x, y):
        directions = [
            (0, 1),  # right
            (1, 0),  # down
            (0, -1),  # left
            (-1, 0),  # up
            (1, 1),  # down right
            (1, -1),  # down left
            (-1, -1),  # up left
            (-1, 1),  # up right
        ]

        found = 0
        for dx, dy in directions:
            if self.check_direction(word, x, y, dx, dy):
                found += 1
        return found

    # part 1
    def check_direction(self, word, x, y, dx, dy):
        for i, letter in enumerate(word):
            nx, ny = x + i * dx, y + i * dy
            if nx < 0 or ny < 0 or nx >= len(self.grid) or ny >= len(self.grid[0]):
                return False
            if self.grid[ny][nx] != letter:
                return False
        return True

    # part 2
    def find_x_mas(self, x, y):
        patterns = [
            [(0, 0, 'M'), (2, 0, 'S'), (1, 1, 'A'), (0, 2, 'M'), (2, 2, 'S')],  # original
            [(0, 0, 'S'), (0, 2, 'M'), (1, 1, 'A'), (2, 0, 'S'), (2, 2, 'M')],  # 90 degrees
            [(0, 0, 'S'), (2, 0, 'M'), (1, 1, 'A'), (0, 2, 'S'), (2, 2, 'M')],  # 180 degrees
            [(0, 0, 'M'), (0, 2, 'S'), (1, 1, 'A'), (2, 0, 'M'), (2, 2, 'S')],  # 270 degrees
        ]

        for pattern in patterns:
            if self.check_x_mas(x, y, pattern):
                return True
        return False

    # part 2
    def check_x_mas(self, x, y, pattern):
        for dx, dy, char in pattern:
            if self.grid[y + dy][x + dx] != char:
                return False
        return True


def parse_input(file_name):
    lines = open(file_name).readlines()
    grid = [list(line.strip()) for line in lines]
    return Grid(grid)


def part1(grid):
    result = 0
    for y in range(len(grid.grid)):
        for x in range(len(grid.grid[y])):
            result += grid.find_occurrences(WORD, x, y)
    return result


def part2(grid):
    result = 0
    for y in range(len(grid.grid) - 2):
        for x in range(len(grid.grid[0]) - 2):
            if grid.find_x_mas(x, y):
                result += 1
    return result


def run():
    inp = parse_input('day4/input.txt')

    print("Part 1: ", part1(inp))
    print("Part 2: ", part2(inp))
