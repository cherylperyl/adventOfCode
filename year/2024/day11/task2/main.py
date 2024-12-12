from collections import deque, defaultdict


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

print(plant_regions)

total_cost = 0
for plant, region in plant_regions:
    area = len(region)

    min_r, min_c, max_r, max_c = region[0][0], region[0][1], region[0][0], region[0][1]
    for r, c in region:
        min_r, max_r = min(r, min_r), max(r, max_r)
        min_c, max_c = min(c, min_c), max(c, max_c)

    region_height, region_width = max_r - min_r + 1, max_c - min_c + 1
    fence_plots = [[0 for _ in range(region_width + 2)] for _ in range(region_height + 2)]
    for r, c in region:
        for step_r, step_c in directions:
            new_r, new_c = r + step_r, c + step_c
            if new_r < 0 or new_r >= height or new_c < 0 or new_c >= width:
                print(new_r, new_c)
                fence_plots[new_r + 1 - min_r][new_c + 1 - min_c] += 1
            elif garden[new_r][new_c] != plant:
                print(new_r, new_c)
                fence_plots[new_r + 1 - min_r][new_c + 1 - min_c] += 1
    for row in fence_plots:
        print(row)

    # count perimeters
    perimeter = 0
    fence_height, fence_width = len(fence_plots), len(fence_plots[0])
    for r in range(fence_height):
        for c in range(fence_width):
            directions = defaultdict(int)
            while fence_plots[r][c] > 0:

                found_step_r, found_step_c = None, None
                for step_r, step_c in directions:
                    # find direction to go into
                    if 0 <= r + step_r < fence_height and 0 <= c + step_c < fence_width and fence_plots[r + step_r][c + step_c] > 0:
                        found_step_r, found_step_c = step_r, step_c
                        break

                # go in that direction if direction found
                if found_step_r is not None and found_step_c is not None and directions[(found_step_r, found_step_c)] < 2:
                    directions[(found_step_r, found_step_c)] += 1
                    fence_plots[r][c] -= 1
                    factor = 1
                    new_r, new_c = r + found_step_r*factor, c + found_step_c*factor
                    while 0 <= new_r < fence_height and 0 <= new_c < fence_width:
                        if fence_plots[new_r][new_c] == 0:
                            break
                        fence_plots[new_r][new_c] -= 1
                        factor += 1
                        new_r, new_c = r + found_step_r*factor, c + found_step_c*factor
                    perimeter += 1

                elif fence_plots[r][c] > 0:
                    perimeter += fence_plots[r][c]
                    fence_plots[r][c] = 0

    print(perimeter)

    total_cost += area * perimeter

print(total_cost)
