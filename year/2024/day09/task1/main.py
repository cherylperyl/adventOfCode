"""
Author: Cheryl Goh
Puzzle: Advent of Code (year=2024 ; day=9 ; task=1)
"""

import sys
from collections import deque


def main():
    for line in sys.stdin:
        disk_map = line.strip("\n")

    space = {}
    idx, file_id = 0, 0
    free_spaces = deque([])
    file_spaces = []
    # map out files and free space
    for i in range(len(disk_map)):

        # if position is even, it is a file block
        if (i == 0) or (i % 2 == 0):
            for j in range(int(disk_map[i])):
                space[idx] = str(file_id)
                file_spaces.append(idx)
                idx += 1
            file_id += 1

        # if position is odd, it represents free space
        else:
            for j in range(int(disk_map[i])):
                space[idx] = "."
                free_spaces.append(idx)
                idx += 1

    # iterate from back
    for i in file_spaces[::-1]:
        next_free_space = free_spaces.popleft()
        if next_free_space > i:
            break

        # shift file
        file_id = space[i]
        space[next_free_space] = file_id
        space[i] = "."

    result = 0
    for key, value in space.items():
        if value != ".":
            result += key*int(value)

    print(result)


if __name__ == "__main__":
    main()
