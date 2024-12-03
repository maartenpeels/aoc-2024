def parse_input(file_name):
    reports = []
    for line in open(file_name).readlines():
        reports.append([int(num) for num in line.split()])
    return reports

def check_report(report):
    report_safe = True

    # all numbers decreasing or increasing?
    increasing = all(report[i] < report[i + 1] for i in range(len(report) - 1))
    decreasing = all(report[i] > report[i + 1] for i in range(len(report) - 1))
    report_safe = report_safe and (increasing or decreasing)

    # Increasing or decreasing at most 3?
    for i in range(len(report) - 1):
        if abs(int(report[i]) - int(report[i + 1])) > 3:
            report_safe = report_safe and False

    return report_safe

def part1(reports):
    safe = 0
    for report in reports:
        report_safe = check_report(report)
        if report_safe:
            safe += 1

    return safe

def part2(reports):
    safe = 0

    # This is pretty ugly, just run it a bunch of times with one number removed
    for report in reports:
        # Default
        report_safe = check_report(report)
        if report_safe:
            safe += 1
        else:
            # Try removing one number
            for i in range(len(report)):
                new_report = report[:i] + report[i+1:]
                report_safe = check_report(new_report)
                if report_safe:
                    safe += 1
                    break

    return safe


def run():
    inp = parse_input('day2/input.txt')

    print("Part 1: ", part1(inp))
    print("Part 2: ", part2(inp))
