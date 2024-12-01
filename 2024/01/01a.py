list_one = []
list_two = []

# Open the file in read mode
with open('input.txt', 'r') as file:
    # Read line by line
    for line in file:
        line_data = line.strip().split("   ")
        list_one.append(int(line_data[0]))
        list_two.append(int(line_data[1]))

# Sort list numbers
list_one.sort()
list_two.sort()

# Get distances
total_distance = 0
for i in range(len(list_one)):
    list_one_num = list_one[i]
    list_two_num = list_two[i]
    distance = abs(list_one_num - list_two_num)
    total_distance += distance

# Print answer
print(total_distance)
