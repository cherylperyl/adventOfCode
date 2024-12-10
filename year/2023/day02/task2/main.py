"""
Author: Cheryl Goh
Puzzle: Advent of Code (year=2023 ; day=2 ; task=2)
"""

import sys


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
        min_red, min_green, min_blue = 0, 0, 0
        for subset in subsets:
            if "red" in subset:
                min_red = max(min_red, subset["red"])
            if "green" in subset:
                min_green = max(min_green, subset["green"])
            if "blue" in subset:
                min_blue = max(min_blue, subset["blue"])

        ans += min_red * min_green * min_blue

    print(ans)


if __name__ == "__main__":
    main()
