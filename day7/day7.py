import itertools


def parse_input(file_name):
    lines = [line.strip() for line in open(file_name).readlines()]

    return [(int(line.split(':')[0]), [int(n) for n in line.split(':')[1].split()]) for line in lines]


def calculate(equations, operators):
    r = 0
    for equation in equations:
        perms = itertools.product(operators, repeat=len(equation[1]) - 1)
        for perm in perms:
            result = equation[1][0]
            for idx, op in enumerate(perm):
                result = op(result, equation[1][idx + 1])

            if result == equation[0]:
                r += equation[0]
                break

    return r


def part1(equations):
    return calculate(equations, [
        lambda a, b: a + b,
        lambda a, b: a * b
    ])


def part2(equations):
    return calculate(equations, [
        lambda a, b: a + b,
        lambda a, b: a * b,
        lambda a, b: int(str(a) + str(b))
    ])


def run():
    equations = parse_input('day7/input.txt')

    print("Part 1: ", part1(equations))
    print("Part 2: ", part2(equations))
