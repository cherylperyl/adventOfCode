"""
Author: Cheryl Goh
Puzzle: Advent of Code (year=2024 ; day=9 ; task=2)
"""

import sys


def main():
    for line in sys.stdin:
        disk_map = line.strip("\n")

    space = {}
    idx, file_id = 0, 0
    free_spaces = []
    file_lengths, file_positions = {}, {}

    # map out files and free space
    for i in range(len(disk_map)):
        length = int(disk_map[i])

        # if position is even, it is a file block
        if (i == 0) or (i % 2 == 0):
            file_idxs = []
            for _ in range(length):
                space[idx] = str(file_id)
                file_idxs.append(idx)
                idx += 1
            file_lengths[file_id], file_positions[file_id] = length, file_idxs
            file_id += 1

        # if position is odd, it represents free space
        else:
            free_space_idxs = []
            for _ in range(length):
                space[idx] = "."
                free_space_idxs.append(idx)
                idx += 1
            free_spaces.append(free_space_idxs)

    # iterate from the last file_id
    biggest_file_id = file_id - 1
    for file_id in range(biggest_file_id, 0, -1):
        avail_free_space_idxs = None
        file_length = file_lengths[file_id]

        # find free space
        for i in range(len(free_spaces)):
            free_space_idxs = free_spaces[i]
            if file_length <= len(free_space_idxs) and \
                    not (free_space_idxs[0] > file_positions[file_id][-1]):
                avail_free_space_idxs = free_space_idxs
                break

        # if free space found
        if avail_free_space_idxs:
            # fill up free space
            space_to_fill = avail_free_space_idxs[0:file_length]
            remaining_space = avail_free_space_idxs[file_length:]
            free_spaces[i] = remaining_space
            for idx in space_to_fill:
                space[idx] = str(file_id)

            # empty file space
            for idx in file_positions[file_id]:
                space[idx] = "."

    result = 0
    for key, value in space.items():
        if value != ".":
            result += key*int(value)

    print(result)


if __name__ == "__main__":
    main()
