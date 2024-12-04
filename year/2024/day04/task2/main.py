"""
Author: Cheryl Goh
Puzzle: Advent of Code (year=2024 ; day=4 ; task=2)
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

    x_mas_count = 0
    width, height = len(puzzle[0]), len(puzzle)
    for start_y in range(1, height-1):
        for start_x in range(1, width-1):
            if puzzle[start_y][start_x] == "A":
                pairs_to_check = [
                    (
                        # left-up and right-down
                        [start_x - 1, start_y - 1],
                        [start_x + 1, start_y + 1]
                    ),
                    (
                        # right-up and left-down
                        [start_x + 1, start_y - 1],
                        [start_x - 1, start_y + 1]
                    ),
                ]

                pairs_result = []
                for (top_letter_idx, bottom_letter_idx) in pairs_to_check:
                    top_letter = puzzle[top_letter_idx[1]][top_letter_idx[0]]
                    bottom_letter = \
                        puzzle[bottom_letter_idx[1]][bottom_letter_idx[0]]

                    if (top_letter == "M" and bottom_letter == "S") or \
                            (top_letter == "S" and bottom_letter == "M"):
                        pairs_result.append(True)
                    else:
                        pairs_result.append(False)

                if pairs_result[0] and pairs_result[1]:
                    x_mas_count += 1

    print(x_mas_count)


if __name__ == "__main__":
    main()
