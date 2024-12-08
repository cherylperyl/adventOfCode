"""
Author: Cheryl Goh
Puzzle: Advent of Code (year=2024 ; day=8 ; task=2)
"""

import sys
from collections import defaultdict
from itertools import combinations


def get_positions_for_axis(axis, direction_1, direction_2, antenna_1,
                           antenna_2):
    positions = {}
    if (antenna_1[axis] - antenna_2[axis]) > 0:
        positions[direction_1], positions[direction_2] = antenna_2, antenna_1
    else:
        positions[direction_1], positions[direction_2] = antenna_1, antenna_2
    return positions


def determine_positions(antenna_1, antenna_2):
    positions = \
        get_positions_for_axis(0, "left", "right", antenna_1, antenna_2) | \
        get_positions_for_axis(1, "up", "down", antenna_1, antenna_2)
    return positions


def main():
    row = 0
    antennas = defaultdict(list)
    for line in sys.stdin:
        line_list = [ch for ch in line.strip('\n')]
        for col in range(len(line_list)):
            if line_list[col] != '.':
                antennas[line_list[col]].append((col, row))
        row += 1

    HEIGHT, WIDTH = row, len(line_list)

    def get_antinodes_in_direction(x, y, dist_x, dist_y):
        valid_antinodes = []
        move_x, move_y = dist_x, dist_y
        while (0 <= (x + move_x) < WIDTH) and (0 <= (y + move_y) < HEIGHT):
            valid_antinodes.append((x + move_x, y + move_y))

            move_x += dist_x
            move_y += dist_y

        return valid_antinodes

    antinodes = set()
    for antenna_list in antennas.values():
        if len(antenna_list) == 0:
            continue

        for antenna in antenna_list:
            antinodes.add(antenna)

        antenna_combinations = list(combinations(antenna_list, 2))
        for antenna_1, antenna_2 in antenna_combinations:
            dist_x = abs(antenna_1[0] - antenna_2[0])
            dist_y = abs(antenna_1[1] - antenna_2[1])

            positions = determine_positions(antenna_1, antenna_2)
            x_1, y_1 = positions["left"][0], positions["left"][1]
            x_2, y_2 = positions["right"][0], positions["right"][1]

            valid_nodes = []

            # \
            if positions["left"] == positions["up"]:
                valid_nodes += get_antinodes_in_direction(x_1, y_1, -dist_x, -dist_y)
                valid_nodes += get_antinodes_in_direction(x_2, y_2, dist_x, dist_y)

            # /
            elif positions["left"] == positions["down"]:
                valid_nodes += get_antinodes_in_direction(x_1, y_1, -dist_x, dist_y)
                valid_nodes += get_antinodes_in_direction(x_2, y_2, dist_x, -dist_y)

            antinodes.update(valid_nodes)

    print(len(antinodes))


if __name__ == "__main__":
    main()
