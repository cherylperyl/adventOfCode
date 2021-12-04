a = []

with open("input.txt") as f:
    for line in f:
        a.append(int(line.strip('\n')))

count = 0
previous_sum = a[0]+a[1]+a[2]
for i in range(3,len(a)):
    current_sum = a[i-2] + a[i-1] + a[i]
    if current_sum > previous_sum:
        count += 1
    previous_sum = current_sum

print(count)