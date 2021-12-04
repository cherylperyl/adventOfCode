a = []

with open("input.txt") as f:
    for line in f:
        a.append(int(line.strip('\n')))

count = 0
for i in range(1,len(a)):
    if (a[i] - a[i-1]) > 0:
        count += 1
print(count)