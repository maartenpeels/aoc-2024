def parse_input(file_name):
    lines = [line.strip() for line in open(file_name).readlines()]
    return lines


def part1(rules, updates):
    result = 0
    return result


def part2(rules, updates, wrong_indices):
    result = 0
    return result


def run():
    inp1, inp2 = parse_input('day/test.txt')

    print("Part 1: ", part1(inp1, inp2))
    print("Part 2: ", part2(inp1, inp2))
