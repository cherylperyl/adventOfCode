"""
Author: Cheryl Goh
Puzzle: Advent of Code (year=2024 ; day=11 ; task=1)
"""

import sys


def main():
    for line in sys.stdin:
        stones = [int(ch) for ch in line.strip("\n").split(" ")]

    after_blink = []
    for _ in range(25):
        for stone in stones:
            stone_str = str(stone)
            stone_len = len(stone_str)

            # 0 become 1
            if stone == 0:
                after_blink.append(1)

            # even digits - split into two stones
            elif stone_len % 2 == 0:
                first_half = stone_str[0:stone_len//2]
                second_half = stone_str[stone_len//2:]
                after_blink += [int(first_half), int(second_half)]

            # multiply by 2024
            else:
                after_blink.append(stone * 2024)

        stones = after_blink
        after_blink = []

    print(len(stones))


if __name__ == "__main__":
    main()
