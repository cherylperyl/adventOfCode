"""
Author: Cheryl Goh
Puzzle: Advent of Code (year=2021 ; day=3 ; task=1)
"""

import sys


def convert_to_dec(binary):
    if len(binary) == 0:
        return 0
    return int(binary[0])*2**(len(binary)-1) + convert_to_dec(binary[1:])


def main():
    count = []

    for line in sys.stdin:
        line = line.strip('\n')
        line_len = len(line)
        if count == []:
            count = [[0, 0] for _ in range(line_len)]
        for i in range(line_len):
            if line[i] == '0':
                count[i][0] += 1
            else:
                count[i][1] += 1

    g = ""
    e = ""

    for i in count:
        if i[0] > i[1]:
            g += "0"
            e += "1"
        else:
            g += "1"
            e += "0"

    g = convert_to_dec(g)
    e = convert_to_dec(e)
    print(g*e)


if __name__ == "__main__":
    main()
