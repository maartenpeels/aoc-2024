def parse_input(file_name):
    _list1 = []
    _list2 = []

    lines = [line for line in open(file_name).readlines()]
    for line in lines:
        _list1.append(int(line.split()[0]))
        _list2.append(int(line.split()[1]))

    return _list1, _list2

def part1(list1, list2):
    # Sort the lists
    list1.sort()
    list2.sort()

    # Calculate the sum of differences
    sum_diff = 0
    for i in range(len(list1)):
        sum_diff += abs(list1[i] - list2[i])

    return sum_diff

def part2(list1, list2):
    # Calculate the occurrences of each element from the first list in the second list
    occurrences = {}
    for num in list1:
        occurrences[num] = list2.count(num)

    # Calculate the similarity score
    similarity_score = 0
    for num in list1:
        similarity_score += num * occurrences[num]

    return similarity_score


def run():
    list1, list2 = parse_input('day1/input.txt')

    print("Part 1: ", part1(list1, list2))
    print("Part 2: ", part2(list1, list2))
