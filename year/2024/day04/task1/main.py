"""
Author: Cheryl Goh
Puzzle: Advent of Code (year=2024 ; day=4 ; task=1)
"""

import sys


def get_range(start, end):
    if start == end:
        return [start for _ in "XMAS"]
    elif start < end:
        return [i for i in range(start, end, 1)]
    else:
        return [i for i in range(start, end, -1)]


def main():
    puzzle = []
    for line in sys.stdin:
        puzzle.append([ch for ch in line.strip("\n")])

    xmas_count = 0
    width, height = len(puzzle[0]), len(puzzle)

    for start_y in range(height):
        for start_x in range(width):
            possible_directions = [
                (start_x + 4, start_y),         # right
                (start_x - 4, start_y),         # left
                (start_x, start_y + 4),         # down
                (start_x, start_y - 4),         # up
                (start_x + 4, start_y + 4),     # right-down
                (start_x - 4, start_y + 4),     # left-down
                (start_x + 4, start_y - 4),     # right-up
                (start_x - 4, start_y - 4)      # left-up
            ]

            for (end_x, end_y) in possible_directions:
                if (end_x >= -1) and (end_x <= width) and (end_y >= -1) and \
                        (end_y <= height):
                    range_x = get_range(start_x, end_x)
                    range_y = get_range(start_y, end_y)
                    word = ""

                    for i in range(len("XMAS")):
                        x, y = range_x[i], range_y[i]
                        word += puzzle[y][x]

                    if word == "XMAS":
                        xmas_count += 1

    print(xmas_count)


if __name__ == "__main__":
    main()
