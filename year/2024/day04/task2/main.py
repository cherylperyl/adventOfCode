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



x_mas_count = 0
width = len(puzzle[0])
height = len(puzzle)
for start_y in range(1, height-1):
    for start_x in range(1, width-1):
        if puzzle[start_y][start_x] == "A":
            pairs_to_check = [
                ([start_x - 1, start_y - 1], [start_x + 1, start_y + 1]),   # left-up and right-down
                ([start_x + 1, start_y - 1], [start_x - 1, start_y + 1]),   # right-up and left-down
            ]

            pairs_result = []
            for (top_letter_indexes, bottom_letter_indexes) in pairs_to_check:
                top_letter = puzzle[top_letter_indexes[1]][top_letter_indexes[0]]
                bottom_letter = puzzle[bottom_letter_indexes[1]][bottom_letter_indexes[0]]

                if (top_letter == "M" and bottom_letter == "S") or (top_letter == "S" and bottom_letter == "M"):
                    pairs_result.append(True)
                else:
                    pairs_result.append(False)

            if pairs_result[0] and pairs_result[1]:
                x_mas_count += 1

print(x_mas_count)
