"""
Author: Cheryl Goh
Puzzle: Advent of Code (year=2021 ; day=2 ; task=2)
"""

import sys


def main():
    h = 0
    d = 0
    a = 0

    for line in sys.stdin:
        line = line.strip("\n").split()
        direction = line[0]
        value = int(line[1])
        if direction == "forward":
            h += value
            d += a*value
        elif direction == "up":
            a -= value
        elif direction == "down":
            a += value

    print(h*d)


if __name__ == "__main__":
    main()
