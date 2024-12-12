from collections import deque


garden = []
with open("input.txt", "r") as file:
    for line in file:
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
    perimeter = 0

    for r, c in region:
        for step_r, step_c in directions:
            new_r, new_c = r + step_r, c + step_c
            if new_r < 0 or new_r >= height or new_c < 0 or new_c >= width:
                perimeter += 1
            elif garden[new_r][new_c] != plant:
                perimeter += 1

    total_cost += area * perimeter

print(total_cost)
