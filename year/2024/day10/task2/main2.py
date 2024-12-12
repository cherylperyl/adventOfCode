def count_stones_after_blinks(stone, blinks, memo):
    # Base case: no more blinks
    if blinks == 0:
        return 1

    # Check if result is already computed
    if (stone, blinks) in memo:
        return memo[(stone, blinks)]

    # Apply rules
    if stone == 0:
        result = count_stones_after_blinks(1, blinks - 1, memo)
    elif len(str(stone)) % 2 == 0:
        # Split the stone
        digits = str(stone)
        mid = len(digits) // 2
        left = int(digits[:mid])
        right = int(digits[mid:])
        result = (count_stones_after_blinks(left, blinks - 1, memo) +
                  count_stones_after_blinks(right, blinks - 1, memo))
    else:
        # Multiply by 2024
        new_stone = stone * 2024
        result = count_stones_after_blinks(new_stone, blinks - 1, memo)

    # Store result in memo
    memo[(stone, blinks)] = result
    return result

def total_stones_after_blinks(initial_stones, blinks):
    memo = {}
    total_stones = 0
    for stone in initial_stones:
        total_stones += count_stones_after_blinks(stone, blinks, memo)
    return total_stones

# Example initial arrangement
initial_stones = [3279, 998884, 1832781, 517, 8, 18864, 28, 0]

# Calculate the exact number of stones after 75 blinks
exact_number_of_stones = total_stones_after_blinks(initial_stones, 75)
print(exact_number_of_stones)
