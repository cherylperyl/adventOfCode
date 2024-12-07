"""
Author: Cheryl Goh
Puzzle: Advent of Code (year=2024 ; day=6 ; task=2)
"""

import sys
import copy


def get_next_position(position, direction):
    moves = {">": (1, 0), "<": (-1, 0), "v": (0, 1), "^": (0, -1)}
    move_x, move_y = moves[direction]
    return position[0] + move_x, position[1] + move_y


def within_range(position, width, height):
    return 0 <= position[0] < width and 0 <= position[1] < height


def stimulation(lab_map, start_position, start_direction, height, width,
                directions):
    obstruction = "#"
    curr_position, curr_direction = start_position, start_direction
    next_position = curr_position

    visted_states = set()
    while within_range(curr_position, width, height):
        # get next position
        next_position = get_next_position(curr_position, curr_direction)

        # if next position is an obstruction, change direction
        while within_range(next_position, width, height) and \
                lab_map[next_position[1]][next_position[0]] == obstruction:
            direction_idx = directions.index(curr_direction)
            curr_direction = directions[(direction_idx + 1) % 4]
            next_position = get_next_position(curr_position, curr_direction)

        # if next position is a visted state, a potential obstacle position has been found
        if (curr_position, curr_direction) in visted_states:
            return True

        # else add the state to visited states
        visted_states.add((curr_position, curr_direction))

        # move to next position
        curr_position = next_position
    return False


def main():
    lab_map = []
    for line in sys.stdin:
        lab_map.append([obj for obj in line.strip("\n")])

    # initialise values
    directions = [">", "v", "<", "^"]
    height, width = len(lab_map), len(lab_map[0])
    curr_position, curr_direction = next(
        ((x, y), lab_map[y][x])
        for y in range(height)
        for x in range(width)
        if lab_map[y][x] in directions
    )

    # get positions without obstructions
    positions_wo_obstruction = [(x, y) for y in range(height)
                                for x in range(width)
                                if lab_map[y][x] == "."]

    new_obstruction_position_count = 0
    for (x, y) in positions_wo_obstruction:
        new_lab_map = copy.deepcopy(lab_map)

        # add obstacle
        new_lab_map[y][x] = "#"

        if stimulation(new_lab_map, curr_position, curr_direction, height,
                       width, directions):
            new_obstruction_position_count += 1

    print(new_obstruction_position_count)


if __name__ == "__main__":
    main()
