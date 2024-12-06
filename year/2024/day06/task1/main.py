"""
Author: Cheryl Goh
Puzzle: Advent of Code (year=2024 ; day=6 ; task=1)
"""

import sys


def get_next_position(position, direction):
    if direction == ">":
        next_position = (position[0] + 1, position[1])
    elif direction == "<":
        next_position = (position[0] - 1, position[1])
    elif direction == "v":
        next_position = (position[0], position[1] + 1)
    elif direction == "^":
        next_position = (position[0], position[1] - 1)
    return next_position


def main():
    lab_map = []
    for line in sys.stdin:
        lab_map.append([obj for obj in line.strip("\n")])

    obstruction = "#"
    directions = [">", "v", "<", "^"]
    height, width = len(lab_map), len(lab_map[0])
    curr_position, curr_direction = None, None

    positions_visited = set()

    # find starting position and direction
    for y in range(height):
        for x in range(width):
            if lab_map[y][x] in directions:
                curr_position = (x, y)
                curr_direction = lab_map[y][x]
                break
        if curr_direction and curr_position:
            break

    next_position = curr_position
    while next_position[0] >= 0 and next_position[0] < width and next_position[1] >= 0 and next_position[1] < height:
        # get next position
        next_position = get_next_position(curr_position, curr_direction)

        # if next position is an obstruction, change direction
        if next_position[0] >= 0 and next_position[0] < width and next_position[1] >= 0 and next_position[1] < height:
            while lab_map[next_position[1]][next_position[0]] == obstruction:
                direction_idx = directions.index(curr_direction)
                curr_direction = directions[(direction_idx + 1) % 4]
                next_position = get_next_position(curr_position, curr_direction)

        # leave current position
        positions_visited.add(curr_position)

        # move to next position
        curr_position = next_position

    print(len(positions_visited))


if __name__ == "__main__":
    main()
