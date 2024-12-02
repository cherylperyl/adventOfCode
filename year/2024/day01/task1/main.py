"""
Author: Cheryl Goh
Puzzle: Advent of Code (year=2024 ; day=1 ; task=1)
"""

import sys


def main():
    list_one = []
    list_two = []

    for line in sys.stdin:
        line_data = line.strip().split("   ")
        list_one.append(int(line_data[0]))
        list_two.append(int(line_data[1]))

    # Sort list numbers
    list_one.sort()
    list_two.sort()

    # Get distances
    total_distance = 0
    for i in range(len(list_one)):
        list_one_num = list_one[i]
        list_two_num = list_two[i]
        distance = abs(list_one_num - list_two_num)
        total_distance += distance

    print(total_distance)


if __name__ == "__main__":
    main()
