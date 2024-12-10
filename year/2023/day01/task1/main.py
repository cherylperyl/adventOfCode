"""
Author: Cheryl Goh
Puzzle: Advent of Code (year=2023 ; day=1 ; task=1)
"""

import sys


def main():
    result = 0
    for line in sys.stdin:
        line_strip = line.strip("/n")

        two_digit_num = ""
        # first digit from the front
        for ch in line_strip:
            if ch.isdigit():
                two_digit_num += ch
                break

        # first digit from the back
        for ch in line_strip[::-1]:
            if ch.isdigit():
                two_digit_num += ch
                break

        result += int(two_digit_num)

    print(result)


if __name__ == "__main__":
    main()
