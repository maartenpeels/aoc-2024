# Should we render the room?
DEBUG = False

#region DEBUG
if DEBUG:
    import matplotlib

    matplotlib.use('TkAgg')
    import matplotlib.pyplot as plt
    import matplotlib.patches as patches
    import time

    # Create a persistent figure outside the function
    fig, ax = plt.subplots()

    # Turn on interactive mode
    plt.ion()


    def plot_room(room, path):
        global fig, ax

        # Clear the previous plot contents
        ax.clear()

        ax.set_aspect('equal')
        ax.set_xticks(range(len(room[0]) + 1))
        ax.set_yticks(range(len(room) + 1))
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        ax.grid(True)

        for y in range(len(room)):
            for x in range(len(room[0])):
                if room[y][x] == '#':
                    ax.add_patch(patches.Rectangle((x, y), 1, 1, fill=True, color='black'))
                elif room[y][x] == '^':
                    ax.add_patch(patches.Rectangle((x, y), 1, 1, fill=True, color='blue'))

        for (x, y) in path:
            ax.add_patch(patches.Circle((x + 0.5, y + 0.5), 0.2, fill=True, color='red'))

        ax.invert_yaxis()
        plt.draw()
        plt.pause(0.1)
#endregion

DIRECTIONS = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # up, right, down, left

def parse_input(file_name):
    return [list(line.strip()) for line in open(file_name).readlines()]


def get_start_pos(room):
    for y in range(len(room)):
        for x in range(len(room)):
            if room[y][x] == '^':
                return x, y

    return None

def walk(start, room):
    visited = set()
    x, y = start
    visited.add((x, y))

    # 0 = up, 1 = right, 2 = down, 3 = left
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    direction = 0

    while True:
        # Calculate next position
        next_x = x + directions[direction][0]
        next_y = y + directions[direction][1]

        # Check if next position is out of bounds
        if next_x < 0 or next_y < 0 or next_x >= len(room) or next_y >= len(room):
            break

        # Check if next position is a wall
        if room[next_y][next_x] == '#':
            # Turn right
            direction = (direction + 1) % 4
        else:
            # Move to next position
            x, y = next_x, next_y
            visited.add((x, y))

    return visited

# Almost the same as walk
def is_loop(start, room):
    visited = set()
    x, y = start
    path = [(x, y)]

    # 0 = up, 1 = right, 2 = down, 3 = left
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    direction = 0

    while True:
        # Calculate next position
        next_x = x + directions[direction][0]
        next_y = y + directions[direction][1]

        # Check if next position is out of bounds
        if next_x < 0 or next_y < 0 or next_x >= len(room[0]) or next_y >= len(room):
            if DEBUG: plot_room(room, path)
            return False

        # Check if the current position and direction have been visited
        if (x, y, direction) in visited:
            if DEBUG: plot_room(room, path)
            return True

        # Add current position and direction to visited
        visited.add((x, y, direction))
        path.append((x, y))

        # Check if next position is a wall
        if room[next_y][next_x] == '#':
            # Turn right
            direction = (direction + 1) % 4
        else:
            # Move to next position
            x, y = next_x, next_y

        # Plot the room and path at each step
        if DEBUG: plot_room(room, path)
        if DEBUG: time.sleep(0.1)


def part1(room):
    start = get_start_pos(room)
    visited = walk(start, room)

    return len(visited)


def part2(room):
    result = 0

    start_pos = get_start_pos(room)
    for y in range(len(room)):
        for x in range(len(room)):
            if room[y][x] != '.':
                continue

            room[y][x] = '#'

            if is_loop(start_pos, room):
                result += 1

            room[y][x] = '.'

    return result


def run():
    inp = parse_input('day6/input.txt')

    print("Part 1: ", part1(inp))
    print("Part 2: ", part2(inp))
