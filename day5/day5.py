def parse_input(file_name):
    lines = [line.strip() for line in open(file_name).readlines()]

    rules = []
    updates = []

    stage = 'rules'
    for line in lines:
        if line == '':
            stage = 'updates'
            continue

        if stage == 'rules':
            parts = line.split('|')
            rules.append([int(parts[0]), int(parts[1])])
        else:
            updates.append([int(x) for x in line.split(',')])

    return rules, updates


def part1(rules, updates):
    result = 0
    wrong = []

    for update_idx, update in enumerate(updates):
        middle = update[int((len(update) - 1)/2)]
        rules_to_check = []
        for rule in rules:
            if rule[0] in update and rule[1] in update:
                rules_to_check.append(rule)

        is_valid = True
        for rule in rules_to_check:
            if update.index(rule[0]) > update.index(rule[1]):
                is_valid = False
                wrong.append(update_idx)
                break

        if is_valid:
            result += middle

    return result, wrong


def part2(rules, updates, wrong_indices):
    result = 0
    for index in wrong_indices:
        update = updates[index]

        rules_to_check = []
        for rule in rules:
            if rule[0] in update and rule[1] in update:
                rules_to_check.append(rule)

        position = {page: i for i, page in enumerate(update)}

        change = True
        while change:
            change = False
            for rule in rules_to_check:
                if position[rule[0]] > position[rule[1]]:
                    change = True
                    position[rule[0]], position[rule[1]] = position[rule[1]], position[rule[0]]

        indexed_update = [(element, position[element]) for element in update]
        indexed_update.sort(key=lambda x: x[1])
        new_update = [element for element, _ in indexed_update]
        result += new_update[int((len(new_update) - 1)/2)]

    return result


def run():
    inp1, inp2 = parse_input('day5/input.txt')

    answer, wrong_indices = part1(inp1, inp2)
    print("Part 1: ", answer)
    print("Part 2: ", part2(inp1, inp2, wrong_indices))
