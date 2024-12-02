"""
Author: Cheryl Goh
Puzzle: Advent of Code (year=2021 ; day=1 ; task=1)
"""

import sys


def main():
    a = []

    for line in sys.stdin:
        a.append(int(line.strip('\n')))

    count = 0
    for i in range(1, len(a)):
        if (a[i] - a[i-1]) > 0:
            count += 1

    print(count)


if __name__ == "__main__":
    main()
