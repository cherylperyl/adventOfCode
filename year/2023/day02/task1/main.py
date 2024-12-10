"""
Author: Cheryl Goh
Puzzle: Advent of Code (year=2023 ; day=2 ; task=1)
"""

import sys


def correct_cube_amt(color, count):
    if color == "red":
        return count <= 12
    if color == "green":
        return count <= 13
    if color == "blue":
        return count <= 14


def main():
    games = {}
    for line in sys.stdin:
        line = line.strip("\n")

        # split to get game id
        game_id, cube_subsets = line.split(": ")
        game_id_int = int(game_id.split(" ")[1])
        cube_subsets = cube_subsets.split("; ")
        games[game_id_int] = []

        for subset in cube_subsets:
            subset_details = {}
            cubes = subset.split(", ")
            for cube in cubes:
                cube_count, cube_color = cube.split(" ")
                subset_details[cube_color] = int(cube_count)
            games[game_id_int].append(subset_details)

    ans = 0
    for game_id, subsets in games.items():
        game_possible = True
        for subset in subsets:
            for color, count in subset.items():
                if not correct_cube_amt(color, count):
                    game_possible = False
                    break
            if not game_possible:
                break

        if game_possible:
            ans += game_id

    print(ans)


if __name__ == "__main__":
    main()
