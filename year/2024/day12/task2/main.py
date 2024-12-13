"""
Author: Cheryl Goh
Puzzle: Advent of Code (year=2024 ; day=12 ; task=1)
"""

import sys
from collections import deque


def main():
    garden = []
    for line in sys.stdin:
        line = line.strip("\n")
        garden.append([ch for ch in line])

    height, width = len(garden), len(garden[0])
    visited = set()
    plant_regions = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for r in range(height):
        for c in range(width):
            if (r, c) not in visited:
                plant_type = garden[r][c]
                region = []
                plots_to_check = deque([(r, c)])
                visited.add((r, c))
                while plots_to_check:
                    curr_plot = plots_to_check.popleft()
                    region.append(curr_plot)
                    for step_r, step_c in directions:
                        new_r, new_c = curr_plot[0] + step_r, curr_plot[1] + step_c
                        new_plot = (new_r, new_c)
                        if new_plot not in visited:
                            if 0 <= new_r < height and 0 <= new_c < width:
                                if garden[new_r][new_c] == plant_type:
                                    plots_to_check.append(new_plot)
                                    visited.add(new_plot)
                plant_regions.append((plant_type, region))

    total_cost = 0
    for plant, region in plant_regions:
        area = len(region)
        if area in (1, 2):
            perimeter = 4
        
        else:
            min_r, min_c, max_r, max_c = region[0][0], region[0][1], region[0][0], region[0][1]
            for r, c in region:
                min_r, max_r = min(r, min_r), max(r, max_r)
                min_c, max_c = min(c, min_c), max(c, max_c)

            region_height, region_width = max_r - min_r + 1, max_c - min_c + 1
            fence_plots = [[' ' for _ in range(region_width + 2)] for _ in range(region_height + 2)]
            for r, c in region:
                fence_plots[r - min_r + 1][c - min_c + 1] = plant

            # count perimeters
            perimeter = 0
            for r in range(region_height + 1):
                for c in range(region_width + 1):
                    # print(r, c)
                    plant_count = 0
                    for r_step, c_step in [(0, 0), (0, 1), (1, 0), (1, 1)]:
                        if fence_plots[r + r_step][c + c_step] == plant:
                            plant_count += 1
                    if plant_count in (1, 3):
                        perimeter += 1
                    elif plant_count == 2 and fence_plots[r][c] == fence_plots[r + 1][c + 1]:
                        perimeter += 2

        total_cost += area * perimeter
        
    print(total_cost)


if __name__ == "__main__":
    main()
