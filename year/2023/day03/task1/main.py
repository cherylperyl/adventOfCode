"""
Author: Cheryl Goh
Puzzle: Advent of Code (year=2023 ; day=3 ; task=1)
"""

import sys


def get_coordinates_to_check(coordinates, bounds, position=""):
    directions = [(1, 0), (-1, 0)]  # middle
    left_extra = [(-1, -1), (1, -1), (0, -1)]
    right_extra = [(1, 1), (-1, 1), (0, 1)]
    if position == "left":
        directions += left_extra
    elif position == "right":
        directions += right_extra
    elif position == "only":
        directions += left_extra + right_extra

    coors_to_check = []
    for row_step, col_step in directions:
        row_aft_step = coordinates[0] + row_step
        col_aft_step = coordinates[1] + col_step
        if (0 <= row_aft_step < bounds[0]) and (0 <= col_aft_step < bounds[1]):
            coors_to_check.append((row_aft_step, col_aft_step))

    return coors_to_check


def main():
    schematic = []
    for line in sys.stdin:
        schematic.append([ch for ch in line.strip("\n")])

    part_num_idxs = []
    for row_idx in range(len(schematic)):
        num = []
        for col_idx in range(len(schematic[row_idx])):
            if schematic[row_idx][col_idx].isdigit():
                num.append((row_idx, col_idx))
            elif len(num) > 0:
                part_num_idxs.append(num)
                num = []
        part_num_idxs.append(num)

    bounds = (len(schematic), len(schematic[0]))
    sum = 0
    for part_num in part_num_idxs:
        coors_to_check = []
        if len(part_num) == 1:
            coors_to_check += get_coordinates_to_check(part_num[0], bounds, "only")
        elif len(part_num) == 2:
            coors_to_check += get_coordinates_to_check(part_num[0], bounds, "left")
            coors_to_check += get_coordinates_to_check(part_num[-1], bounds, "right")
        elif len(part_num) == 3:
            coors_to_check += get_coordinates_to_check(part_num[0], bounds, "left")
            coors_to_check += get_coordinates_to_check(part_num[2], bounds, "right")
            coors_to_check += get_coordinates_to_check(part_num[1], bounds=bounds)

        object_found = False
        for row_idx, col_idx in coors_to_check:
            if schematic[row_idx][col_idx] != "." and not schematic[row_idx][col_idx].isdigit():
                object_found = True
                break

        if object_found:
            part_num_str = ""
            for row_idx, col_idx in part_num:
                part_num_str += schematic[row_idx][col_idx]
            sum += int(part_num_str)

    print(sum)


if __name__ == "__main__":
    main()
