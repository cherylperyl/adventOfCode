"""
Author: Cheryl Goh
Puzzle: Advent of Code (year=2024 ; day=15 ; task=1)
"""

import sys


def main():
    warehouse = []
    movements = ""
    curr_position = None
    walls, boxes = set(), set()
    row = 0
    for line in sys.stdin:
        line = line.strip("\n")
        if "#" in line:
            for col in range(len(line)):
                if line[col] == "#":
                    walls.add((row, col))
                elif line[col] == "O":
                    boxes.add((row, col))
                elif line[col] == "@":
                    curr_position = (row, col)
            warehouse.append([ch for ch in line])
        else:
            movements += line
        row += 1

    directions = {
        "<": (0, -1),
        ">": (0, 1),
        "v": (1, 0),
        "^": (-1, 0)
    }

    for move in movements:
        direction = directions[move]
        next_position = (curr_position[0] + direction[0],
                         curr_position[1] + direction[1])

        if next_position in walls:
            # dont move
            continue

        if warehouse[next_position[0]][next_position[1]] == ".":
            # shift robot
            warehouse[next_position[0]][next_position[1]] = \
                warehouse[curr_position[0]][curr_position[1]]
            warehouse[curr_position[0]][curr_position[1]] = "."

            curr_position = next_position
            continue

        box_position = None
        if next_position in boxes:
            factor = 1
            while (curr_position[0] + direction[0]*factor,
                   curr_position[1] + direction[1]*factor) in boxes:
                factor += 1
                if warehouse[curr_position[0] + direction[0]*factor][
                        curr_position[1] + direction[1]*factor] == ".":
                    box_position = (curr_position[0] + direction[0]*factor,
                                    curr_position[1] + direction[1]*factor)

        if box_position is not None:
            # shift box
            warehouse[box_position[0]][box_position[1]] = \
                warehouse[next_position[0]][next_position[1]]

            boxes.remove(next_position)
            boxes.add(box_position)

            # shift robot
            warehouse[next_position[0]][next_position[1]] = \
                warehouse[curr_position[0]][curr_position[1]]
            warehouse[curr_position[0]][curr_position[1]] = "."

            curr_position = next_position

    ans = 0
    for box in boxes:
        ans += (100 * box[0]) + box[1]

    print(ans)


if __name__ == "__main__":
    main()
