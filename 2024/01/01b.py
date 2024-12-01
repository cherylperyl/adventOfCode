list_one = []
list_two = {}

# Open the file in read mode
with open('input.txt', 'r') as file:
    # Read line by line
    for line in file:
        line_data = line.strip().split("   ")

        # Adds list one num to the list
        list_one.append(int(line_data[0]))

        # Get num count for list_two
        list_two_num = int(line_data[1])
        if list_two_num in list_two:
            list_two[list_two_num] += 1
        else:
            list_two[list_two_num] = 1

# Get similarity score
total_similarity_score = 0
for i in list_one:
    if i in list_two:
        total_similarity_score += i * list_two[i]

# Print answer
print(total_similarity_score)
