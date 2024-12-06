"""
Author: Cheryl Goh
Puzzle: Advent of Code (year=2024 ; day=5 ; task=2)
"""

import sys
from collections import deque


# topo sort with Kahn algo
def topo_sort(graph: dict) -> list:
    """
    :param graph:
    :return topo_sorted_list:
    Logic of Kahn algo is iteratively prioritising the nodes with no dependencies, dependency status of a node is updated everytime a node with no dependency is added to the topo sort
    """
    in_degrees = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            if neighbor in in_degrees:
                in_degrees[neighbor] += 1

    queue = deque([node for node in in_degrees if in_degrees[node] == 0])
    sorted_list = []

    while queue:
        node = queue.popleft()
        sorted_list.append(node)

        # update in_degrees
        for neighbor in graph[node]:
            if neighbor in in_degrees:
                in_degrees[neighbor] -= 1

                # if in_degree become 0, add to queue
                if in_degrees[neighbor] == 0:
                    queue.append(neighbor)

    return sorted_list


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

    # get updates in wrong order
    updates_in_wrong_order = []
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
        if not in_right_order:
            updates_in_wrong_order.append(update)

    sorted_updates = []
    for update_in_wrong_order in updates_in_wrong_order:
        # Gather rules related to the numbers in the wrongly ordered update
        graph = {}
        for i in range(len(update_in_wrong_order)):
            curr_page = update_in_wrong_order[i]
            graph[curr_page] = set()
            remaining_pages = update_in_wrong_order[0:i] + \
                update_in_wrong_order[i+1:]
            # Add only relevant rules
            for page in remaining_pages:
                if curr_page in rules and page in rules[curr_page]:
                    graph[curr_page].add(page)
        sorted_updates.append(topo_sort(graph))

    # Get sum of middle page corrctly-orderd updates
    ans = 0
    for update in sorted_updates:
        middle_page_idx = (len(update)-1) // 2
        ans += int(update[middle_page_idx])

    print(ans)


if __name__ == "__main__":
    main()
