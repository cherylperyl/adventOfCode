"""
Author: Cheryl Goh
Puzzle: Advent of Code (year=2024 ; day=2 ; task=2)
"""

import sys


def checkIfSafe(report: list[int]) -> bool:
    isSafe = True
    direction = ""
    for i in range(len(report)-1):
        first_num = report[i]
        second_num = report[i+1]

        diff = second_num - first_num
        curr_direction = ""
        if diff == 0:
            isSafe = False
            break
        if diff > 0:
            curr_direction = "increasing"
        else:
            curr_direction = "decreasing"

        # Rule 1: The levels are either all increasing or all decreasing.
        if i == 0:
            direction = curr_direction
        else:
            if direction != curr_direction:
                isSafe = False
                break

        # Rule 2: Any two adjacent levels differ by at least one and at most three.
        mod_diff = abs(diff)
        if mod_diff > 3:
            isSafe = False
            break

    return isSafe


def main():
    safeReportsCount = 0

    for line in sys.stdin:
        line_data = line.strip()
        report = [int(item) for item in line_data.split(" ")]

        if checkIfSafe(report):
            safeReportsCount += 1
        else:
            for i in range(len(report)):
                new_report = report[0:i] + report[i+1:]
                if checkIfSafe(new_report):
                    safeReportsCount += 1
                    break

    print(safeReportsCount)


if __name__ == "__main__":
    main()
