"""
Author: Cheryl Goh
Puzzle: Advent of Code (year=2024 ; day=14 ; task=2)
"""

import sys


def main():
    height, width = 103, 101
    space = [[0 for _ in range(width)] for _ in range(height)]
    robots = []
    for line in sys.stdin:
        line = line.strip("\n")

        initial_position, velocity = line.split(" ")
        x, y = initial_position.split("=")[1].split(",")
        step_x, step_y = velocity.split("=")[1].split(",")
        x, y = int(x), int(y)
        step_x, step_y = int(step_x), int(step_y)
        robots.append(((x, y), (step_x, step_y)))

    for i in range(10000):
        probable = True
        space = [[0 for _ in range(width)] for _ in range(height)]
        for (x, y), (step_x, step_y) in robots:
            x_after_step = (x + (i * step_x)) % width
            y_after_step = (y + (i * step_y)) % height

            if space[y_after_step][x_after_step] == 0:
                space[y_after_step][x_after_step] += 1
            else:
                probable = False
                break

        if probable:
            # print("after", i, "seconds")
            # for row in space:
                # for col in row:
                    # if col != 0:
                        # print("\033[41mR\033[0m", end="")
                    # else:
                        # print(" ", end="")
                # print(end="\n")
            # print()
            print(i)


if __name__ == "__main__":
    main()
