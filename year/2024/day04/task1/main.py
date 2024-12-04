puzzle = []
with open("../input.txt", "r") as file:
    for line in file:
        puzzle.append([ch for ch in line.strip("\n")])

print(puzzle)


def get_range(start, end):
    if start == end:
        return [start for _ in "XMAS"]
    elif start < end:
        return [i for i in range(start, end, 1)]
    else:
        return [i for i in range(start, end, -1)]


def within_range(x, y):
    return (x >= -1) and (x <= width) and (y >= -1) and (y <= height)


xmas_count = 0
width = len(puzzle[0])
height = len(puzzle)
for start_y in range(height):
    for start_x in range(width):
        possible_directions = [
            (start_x + 4, start_y),         # right
            (start_x - 4, start_y),         # left
            (start_x, start_y + 4),         # down
            (start_x, start_y - 4),         # up
            (start_x + 4, start_y + 4),     # right-down
            (start_x - 4, start_y + 4),     # left-down
            (start_x + 4, start_y - 4),     # right-up
            (start_x - 4, start_y - 4)      # left-up
        ]

        for (end_x, end_y) in possible_directions:
            if within_range(end_x, end_y):
                range_x, range_y = get_range(start_x, end_x), get_range(start_y, end_y)
                word = ""
                for i in range(len("XMAS")):
                    x, y = range_x[i], range_y[i]
                    word += puzzle[y][x]

                if word == "XMAS":
                    xmas_count += 1

print(xmas_count)


