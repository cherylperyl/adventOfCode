h = 0
d = 0
a = 0

with open("input.txt") as f:
    for line in f:
        line = line.strip("\n").split()
        direction = line[0]
        value = int(line[1])
        if direction == "forward":
            h += value
            d += a*value
        elif direction == "up":
            a -= value
        elif direction == "down":
            a += value

print(h*d)