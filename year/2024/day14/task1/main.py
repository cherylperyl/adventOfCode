"""
Author: Cheryl Goh
Puzzle: Advent of Code (year=2024 ; day=14 ; task=1)
"""

import sys


def get_robot_count_in_quadrant(start_x, end_x, start_y, end_y, space):
    count = 0
    for y in range(start_y, end_y):
        for x in range(start_x, end_x):
            count += space[y][x]
    return count


def main():
    height, width = 103, 101
    space = [[0 for _ in range(width)] for _ in range(height)]
    for line in sys.stdin:
        line = line.strip("\n")

        initial_position, velocity = line.split(" ")
        x, y = initial_position.split("=")[1].split(",")
        step_x, step_y = velocity.split("=")[1].split(",")
        x, y = int(x), int(y)
        step_x, step_y = int(step_x), int(step_y)

        # after 100 seconds
        x_after_100 = (x + (100 * step_x)) % width
        y_after_100 = (y + (100 * step_y)) % height

        # place in space
        space[y_after_100][x_after_100] += 1

    result = get_robot_count_in_quadrant(0, (width-1)//2, 0,
                                         (height-1)//2, space) \
        * get_robot_count_in_quadrant((width+1)//2, width, 0,
                                      (height-1)//2, space) \
        * get_robot_count_in_quadrant(0, (width-1)//2,
                                      (height+1)//2, height, space) \
        * get_robot_count_in_quadrant((width+1)//2, width,
                                      (height+1)//2, height, space)

    print(result)


if __name__ == "__main__":
    main()
