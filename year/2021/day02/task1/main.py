"""
Author: Cheryl Goh
Puzzle: Advent of Code (year=2021 ; day=2 ; task=1)
"""

import sys


def main():
    h = 0
    d = 0

    for line in sys.stdin:
        line = line.strip("\n").split()
        direction = line[0]
        value = int(line[1])
        if direction == "forward":
            h += value
        elif direction == "up":
            d -= value
        elif direction == "down":
            d += value

    print(h*d)


if __name__ == "__main__":
    main()
