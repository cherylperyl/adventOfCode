"""
Author: Cheryl Goh
Puzzle: Advent of Code (year=2024 ; day=8 ; task=1)
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


def get_antinodes(antenna_1, antenna_2, width, height):
    dist_x = abs(antenna_1[0] - antenna_2[0])
    dist_y = abs(antenna_1[1] - antenna_2[1])

    positions = determine_positions(antenna_1, antenna_2)

    valid_antinodes = []

    # \
    if positions["left"] == positions["up"]:
        antinodes = [(positions["left"][0] - dist_x, positions["left"][1] - dist_y),
                     (positions["right"][0] + dist_x, positions["right"][1] + dist_y)]

    # /
    elif positions["left"] == positions["down"]:
        antinodes = [(positions["left"][0] - dist_x, positions["left"][1] + dist_y),
                     (positions["right"][0] + dist_x, positions["right"][1] - dist_y)]

    for antinode in antinodes:
        if (0 <= antinode[0] < width) and (0 <= antinode[1] < height):
            valid_antinodes.append(antinode)

    return valid_antinodes


def main():
    row = 0
    antennas = defaultdict(list)
    for line in sys.stdin:
        line_list = [ch for ch in line.strip('\n')]
        for col in range(len(line_list)):
            if line_list[col] != '.':
                antennas[line_list[col]].append((col, row))
        row += 1

    height, width = row, len(line_list)

    antinodes = set()
    for antenna_list in antennas.values():
        antenna_combinations = list(combinations(antenna_list, 2))

        for antenna_1, antenna_2 in antenna_combinations:
            for antinode in get_antinodes(antenna_1, antenna_2, width, height):
                antinodes.add(antinode)

    print(len(antinodes))


if __name__ == "__main__":
    main()
