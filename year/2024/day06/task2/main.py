"""
Author: Cheryl Goh
Puzzle: Advent of Code (year=2024 ; day=6 ; task=2)
"""

import sys
import copy


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

    positions_wo_obstruction = []
    for y in range(height):
        for x in range(width):
            # find starting position and direction
            if (curr_direction is None) and (lab_map[y][x] in directions):
                curr_position = (x, y)
                curr_direction = lab_map[y][x]

            # get positions without obstructions
            if lab_map[y][x] == ".":
                positions_wo_obstruction.append((x, y))

    new_obstruction_position_count = 0
    for (x, y) in positions_wo_obstruction:
        new_lab_map = copy.deepcopy(lab_map)

        # add obstacle
        new_lab_map[y][x] = "#"

        curr_position_temp = curr_position
        curr_direction_temp = curr_direction
        next_position = curr_position_temp
        visted_states = set()
        while next_position[0] >= 0 and next_position[0] < width and next_position[1] >= 0 and next_position[1] < height:
            # get next position
            next_position = get_next_position(curr_position_temp, curr_direction_temp)

            # if next position is an obstruction, change direction
            if next_position[0] >= 0 and next_position[0] < width and next_position[1] >= 0 and next_position[1] < height:
                while new_lab_map[next_position[1]][next_position[0]] == obstruction:
                    direction_idx = directions.index(curr_direction_temp)
                    curr_direction_temp = directions[(direction_idx + 1) % 4]
                    next_position = get_next_position(curr_position_temp, curr_direction_temp)

            # if next position is a visted state, a potential obstacle position has been found
            if (curr_position_temp, curr_direction_temp) in visted_states:
                new_obstruction_position_count += 1
                break
            visted_states.add((curr_position_temp, curr_direction_temp))

            # move to next position
            curr_position_temp = next_position

    print(new_obstruction_position_count)


if __name__ == "__main__":
    main()
