"""
Author: Cheryl Goh
Puzzle: Advent of Code (year=2024 ; day=5 ; task=1)
"""

import sys


def main():
    rules = {}
    updates = []
    for line in sys.stdin:
        # If line has "|" it is a page ordering rule
        if "|" in line:
            order_rules = line.strip("\n").split("|")
            if order_rules[0] in rules:
                rules[order_rules[0]].append(order_rules[1])
            else:
                rules[order_rules[0]] = [order_rules[1]]
        # dict meaning: the key has to come before all values

        # If line has "," it is an update
        if "," in line:
            updates.append(line.strip("\n").split(","))

    updates_in_right_order = []

    # check updates
    for update in updates:
        in_right_order = True
        reversed_update = update[::-1]
        # check from the back
        for i in range(len(reversed_update)):
            curr_page = reversed_update[i]
            remaining_pages = set(reversed_update[i+1:])
            if curr_page in rules:
                for page_num in rules[curr_page]:
                    if page_num in remaining_pages:
                        in_right_order = False
                        break
            if not in_right_order:
                break

        if in_right_order:
            updates_in_right_order.append(update)

    # Get sum of middle page corrctly-orderd updates
    ans = 0
    for update_in_right_order in updates_in_right_order:
        middle_page_idx = (len(update_in_right_order)-1) // 2
        ans += int(update_in_right_order[middle_page_idx])

    print(ans)


if __name__ == "__main__":
    main()
