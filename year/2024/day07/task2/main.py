"""
Author: Cheryl Goh
Puzzle: Advent of Code (year=2024 ; day=7 ; task=2)
"""

import sys
import itertools


def get_combinations(positions, symbols):
    # Generate all possible combinations
    combinations = itertools.product(symbols, repeat=positions)

    # Convert the combinations to a list of strings and print them
    combinations_list = [''.join(combination) for combination in combinations]

    return combinations_list


def main():
    equations = []
    for line in sys.stdin:
        test, remaining_nums = line.strip('\n').split(':')
        remaining_nums_list = remaining_nums.strip().split(' ')
        equations.append((int(test), [int(num) for num in remaining_nums_list]))

    symbols = ['+', '*', '|']
    total = 0
    for test_val, remaining_nums in equations:
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
                elif symbol == '|':
                    result = int(str(result) + str(num))
                if result > test_val:
                    break
            if result == test_val:
                total += test_val
                break
    print(total)


if __name__ == "__main__":
    main()
