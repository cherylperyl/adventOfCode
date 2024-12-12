"""
Author: Cheryl Goh
Puzzle: Advent of Code (year=2024 ; day=11 ; task=2)
"""

import sys
import functools


@functools.cache
def is_even_digits(stone):
    stone_str = str(stone)
    stone_len = len(stone_str)
    return stone_len % 2 == 0


@functools.cache
def split_stone(stone):
    stone_str = str(stone)
    stone_len = len(stone_str)
    first_half = stone_str[0:stone_len//2]
    second_half = stone_str[stone_len//2:]
    return [int(first_half), int(second_half)]


@functools.cache
def muliply_by_2024(num):
    return num * 2024


def main():
    for line in sys.stdin:
        stones = [int(ch) for ch in line.strip("\n").split(" ")]

    after_blink = []
    for _ in range(75):
        for stone in stones:

            # 0 become 1
            if stone == 0:
                after_blink.append(1)

            # even digits - split into two stones
            elif is_even_digits(stone):
                after_blink += split_stone(stone)

            # multiply by 2024
            else:
                after_blink.append(stone * 2024)

        stones = after_blink
        after_blink = []

    print(len(stones))


if __name__ == "__main__":
    main()
