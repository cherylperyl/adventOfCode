"""
Author: Cheryl Goh
Puzzle: Advent of Code (year=2024 ; day=10 ; task=2)
"""

import sys
from collections import deque


def get_neighbours(node, topo_map):
    col_idx, row_idx = node[0], node[1]
    height = topo_map[row_idx][col_idx]
    neighbours = []
    if height < 9:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for c_i, r_i in directions:
            neighbour = (col_idx + c_i, row_idx + r_i)
            if (0 <= neighbour[1] < len(topo_map)) and \
                (0 <= neighbour[0] < len(topo_map[0])) and \
                    topo_map[neighbour[1]][neighbour[0]] == (height + 1):
                neighbours.append((col_idx + c_i, row_idx + r_i))
    return neighbours


def main():
    topo_map, trailheads, row_idx = [], [], 0
    for line in sys.stdin:
        line_strip = line.strip("\n")
        row = []
        for col_idx in range(len(line_strip)):
            row.append(int(line_strip[col_idx]))
            if line_strip[col_idx] == '0':
                trailheads.append((col_idx, row_idx))
        topo_map.append(row)
        row_idx += 1

    score_sum = 0
    for trailhead in trailheads:
        queue = deque([trailhead])

        while queue:
            node = queue.popleft()

            if topo_map[node[1]][node[0]] == 9:
                score_sum += 1

            else:
                for neighbour in get_neighbours(node, topo_map):
                    queue.append(neighbour)

    print(score_sum)


if __name__ == "__main__":
    main()
