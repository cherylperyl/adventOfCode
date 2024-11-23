h = 0
d = 0

with open("input.txt") as f:
    for line in f:
        line = line.strip("\n").split()
        direction = line[0]
        value = int(line[1])
        if direction == "forward":
            h += value
        elif direction == "up":
            d -= value
        elif direction == "down":
            d += value

print(h*d)