warehouse = []
movements = ""
with open("tests/01.in", "r") as file:
    for line in file:
        line = line.strip("\n")
        if "#" in line:
            transformed_line = []
            for ch in line:
                if ch == "#":
                    transformed_line.extend(["#", "#"])
                elif ch == "O":
                    transformed_line.extend(["[", "]"])
                elif ch == ".":
                    transformed_line.extend([".", "."])
                elif ch == "@":
                    transformed_line.extend(["@", "."])
            warehouse.append(transformed_line)
        else:
            movements += line

for line in warehouse:
    for ch in line:
        print(ch, end="")
    print(end="\n")
print()

curr_position = None
walls, boxes_left = set(), set()
height, width = len(warehouse), len(warehouse[0])
for r in range(height):
    for c in range(width):
        if warehouse[r][c] == "@":
            curr_position = (r, c)
        elif warehouse[r][c] == "#":
            walls.add((r, c))
        elif warehouse[r][c] == "[":
            boxes_left.add((r, c))

directions = {
    "<": (0, -1),
    ">": (0, 1),
    "v": (1, 0),
    "^": (-1, 0)
}

for move in movements[:40]:
    print(move)

    direction = directions[move]
    next_position = (curr_position[0] + direction[0],
                     curr_position[1] + direction[1])

    print(next_position)

    # if it is wall dont move
    if next_position in walls:
        for line in warehouse:
            for ch in line:
                print(ch, end="")
            print(end="\n")
            print()
        continue

    # if empty space move one step
    if warehouse[next_position[0]][next_position[1]] == ".":
        # shift robot
        warehouse[next_position[0]][next_position[1]] = \
            warehouse[curr_position[0]][curr_position[1]]
        warehouse[curr_position[0]][curr_position[1]] = "."

        curr_position = next_position

        for line in warehouse:
            for ch in line:
                print(ch, end="")
            print(end="\n")
        print()
        continue

    # if box, then shift two step at a time if going right/ left
    box_position = None
    if warehouse[next_position[0]][next_position[1]] in ["[", "]"]:
        if move in ["<", ">"]:
            factor = 1
            while (warehouse[curr_position[0] + direction[0]*factor][
                    curr_position[1] + direction[1]*factor] in ["[", "]"]):
                factor += 1
                if warehouse[curr_position[0] + direction[0]*factor][
                        curr_position[1] + direction[1]*factor] == ".":
                    box_position = (curr_position[0] + direction[0]*factor,
                                    curr_position[1] + direction[1]*factor)
        elif warehouse[next_position[0]][next_position[1]] == "[":
            factor = 1
            while (warehouse[curr_position[0] + direction[0]*factor][
                    curr_position[1] + direction[1]*factor] in ["[", "]"]):
                factor += 1
                if warehouse[curr_position[0] + direction[0]*factor][
                        curr_position[1] + direction[1]*factor] == ".":
                    box_position = (curr_position[0] + direction[0]*factor,
                                    curr_position[1] + direction[1]*factor)

    print(box_position)

    if box_position is not None:

        if (box_position[1] > curr_position[1]):
            # shift boxes
            for i in range(box_position[1], curr_position[1], -1):
                warehouse[box_position[0]][i] = warehouse[box_position[0]][i-1]
                if warehouse[box_position[0]][i] == "[":
                    boxes_left.add(warehouse[box_position[0]][i])
                    boxes_left.remove(warehouse[box_position[0]][i-1])

            # shift robot
            warehouse[next_position[0]][next_position[1]] = \
                warehouse[curr_position[0]][curr_position[1]]
            warehouse[curr_position[0]][curr_position[1]] = "."

            curr_position = next_position

        elif (curr_position[1] > box_position[1]):
            # shift boxes
            for i in range(box_position[1], curr_position[1]):
                warehouse[box_position[0]][i] = warehouse[box_position[0]][i+1]
                if warehouse[box_position[0]][i] == "[":
                    boxes_left.add(warehouse[box_position[0]][i])
                    boxes_left.remove(warehouse[box_position[0]][i+1])

            # shift robot
            warehouse[next_position[0]][next_position[1]] = \
                warehouse[curr_position[0]][curr_position[1]]
            warehouse[curr_position[0]][curr_position[1]] = "."

            curr_position = next_position

        elif (box_position[0] > curr_position[0]):
            # shift boxes
            for i in range(box_position[0], curr_position[0], -1):
                warehouse[box_position[0]][i] = warehouse[box_position[0]][i+1]
                if warehouse[box_position[0]][i] == "[":
                    boxes_left.add(warehouse[box_position[0]][i])
                    boxes_left.remove(warehouse[box_position[0]][i+1])

            # shift robot
            warehouse[next_position[0]][next_position[1]] = \
                warehouse[curr_position[0]][curr_position[1]]
            warehouse[curr_position[0]][curr_position[1]] = "."

            curr_position = next_position

        if move == ">":
            # shift box
            warehouse[box_position[0]][box_position[1]] = \
                warehouse[next_position[0]][next_position[1]]
            warehouse[box_position[0]][box_position[1] + 1] = \
                warehouse[next_position[0]][next_position[1] + 1]

            boxes_left.remove(next_position)
            boxes_left.add(box_position)

            # shift robot
            warehouse[next_position[0]][next_position[1] + 1] = \
                warehouse[curr_position[0]][curr_position[1]]
            warehouse[next_position[0]][next_position[1]] = "."
            warehouse[curr_position[0]][curr_position[1]] = "."

            curr_position = (next_position[0], next_position[1]+1)

        elif move == "<":
            # shift box
            warehouse[box_position[0]][box_position[1]] = \
                warehouse[next_position[0]][next_position[1]]
            warehouse[box_position[0]][box_position[1] - 1] = \
                warehouse[next_position[0]][next_position[1] - 1]

            boxes_left.remove((next_position[0], next_position[1]-1))
            boxes_left.add((box_position[0], box_position[1]-1))

            # shift robot
            warehouse[next_position[0]][next_position[1] - 1] = \
                warehouse[curr_position[0]][curr_position[1]]
            warehouse[next_position[0]][next_position[1]] = "."
            warehouse[curr_position[0]][curr_position[1]] = "."

            curr_position = (next_position[0], next_position[1]-1)

        elif move in ["^", "v"]:
            if warehouse[next_position[0]][next_position[1]] == "[":
                # shift box
                warehouse[box_position[0]][box_position[1]] = \
                    warehouse[next_position[0]][next_position[1]]
                warehouse[box_position[0]][box_position[1] + 1] = \
                    warehouse[next_position[0]][next_position[1] + 1]

                boxes_left.remove(next_position)
                boxes_left.add(box_position)

                # shift robot
                warehouse[next_position[0]][next_position[1]] = \
                    warehouse[curr_position[0]][curr_position[1]]
                warehouse[next_position[0]][next_position[1] + 1] = "."
                warehouse[curr_position[0]][curr_position[1]] = "."

                curr_position = (next_position[0], next_position[1])

            elif warehouse[next_position[0]][next_position[1]] == "]":
                # shift box
                warehouse[box_position[0]][box_position[1]] = \
                    warehouse[next_position[0]][next_position[1]]
                warehouse[box_position[0]][box_position[1] - 1] = \
                    warehouse[next_position[0]][next_position[1] - 1]

                boxes_left.remove((next_position[0], next_position[1] - 1))
                boxes_left.add((box_position[0], box_position[1] - 1))

                # shift robot
                warehouse[next_position[0]][next_position[1]] = \
                    warehouse[curr_position[0]][curr_position[1]]
                warehouse[next_position[0]][next_position[1] - 1] = "."
                warehouse[curr_position[0]][curr_position[1]] = "."

                curr_position = (next_position[0], next_position[1])

    for line in warehouse:
        for ch in line:
            print(ch, end="")
        print(end="\n")
    print()

ans = 0
for box in boxes_left:
    ans += (100 * box[0]) + box[1]

print(ans)
