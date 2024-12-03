import re


def parse_input(file_name):
    lines = open(file_name).readlines()
    return ''.join(lines)

def part1(line):
    mul_regex = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
    matches = mul_regex.findall(line)
    result = 0
    for match in matches:
        result += int(match[0]) * int(match[1])
    return result

def part2(line):
    # Not very efficient, but it works
    mul_regex = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
    do_regex = re.compile(r'do\(\)')
    dont_regex = re.compile(r"don't\(\)")

    result = 0
    mul_enabled = True
    i = 0

    while i < len(line):
        if do_regex.match(line, i):
            mul_enabled = True
            i += len('do()')
        elif dont_regex.match(line, i):
            mul_enabled = False
            i += len("don't()")
        else:
            match = mul_regex.match(line, i)
            if match and mul_enabled:
                result += int(match.group(1)) * int(match.group(2))
                i += len(match.group(0))
            else:
                i += 1

    return result


def run():
    inp = parse_input('day3/input.txt')

    print("Part 1: ", part1(inp))
    print("Part 2: ", part2(inp))
