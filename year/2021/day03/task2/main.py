"""
Author: Cheryl Goh
Puzzle: Advent of Code (year=2021 ; day=3 ; task=2)
"""

import sys


def convert_to_dec(binary):
    if len(binary) == 0:
        return 0
    return int(binary[0])*2**(len(binary)-1) + convert_to_dec(binary[1:])


def main():
    numbers = []

    for line in sys.stdin:
        line = line.strip('\n')
        numbers.append(line)

    numbers_o = numbers
    next = []
    idx = 0
    while len(numbers_o) != 1:
        count_0 = 0
        count_1 = 0
        for num in numbers_o:
            if num[idx] == "0":
                count_0 += 1
            else:
                count_1 += 1

        if count_0 > count_1:
            next = [num for num in numbers_o if num[idx] == "0"]
        else:
            next = [num for num in numbers_o if num[idx] == "1"]

        idx += 1
        count_0, count_1, numbers_o = 0, 0, next

    numbers_s = numbers
    next = []
    idx = 0
    while len(numbers_s) != 1:
        count_0 = 0
        count_1 = 0
        for num in numbers_s:
            if num[idx] == "0":
                count_0 += 1
            else:
                count_1 += 1

        if count_0 > count_1:
            next = [num for num in numbers_s if num[idx] == "1"]
        else:
            next = [num for num in numbers_s if num[idx] == "0"]

        idx += 1
        count_0, count_1, numbers_s = 0, 0, next

    o = convert_to_dec(numbers_o[0])
    s = convert_to_dec(numbers_s[0])
    print(o*s)


if __name__ == "__main__":
    main()
