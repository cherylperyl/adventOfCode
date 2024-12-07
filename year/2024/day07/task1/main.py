input = {}
with open('input.txt', 'r') as f:
    for line in f:
        test, remaining_nums = line.strip('\n').split(':')
        input[int(test)] = [int(num) for num in remaining_nums.strip().split(' ')]

import itertools
def get_combinations(positions, symbols):
    # Generate all possible combinations
    combinations = itertools.product(symbols, repeat=positions)

    # Convert the combinations to a list of strings and print them
    combinations_list = [''.join(combination) for combination in combinations]

    return combinations_list


symbols = ['+', '*']
total = 0
for test_val, remaining_nums in input.items():
    remaining_nums_count = len(remaining_nums)
    combinations_list = get_combinations(remaining_nums_count-1, symbols)
    for combination in combinations_list:
        result = remaining_nums[0]
        for i in range(len(combination)):
            symbol = combination[i]
            num = remaining_nums[i+1]
            if symbol == '*':
                result *= num
            elif symbol == '+':
                result += num
            # if result > test_val:
            #     break
        if result == test_val:
            total += test_val
            break
print(total)
