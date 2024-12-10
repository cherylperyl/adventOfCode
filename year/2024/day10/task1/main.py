from collections import deque

topo_map = []
trailheads = []
with open("input.txt", "r") as file:
    row_idx = 0
    for line in file:
        line_strip =  line.strip("\n")
        row = []
        for col_idx in range(len(line_strip)):
            row.append(int(line_strip[col_idx]))
            if line_strip[col_idx] == '0':
                trailheads.append((col_idx, row_idx))
        topo_map.append(row)
        row_idx += 1

for line in topo_map:
    print(line)

def get_neighbours(node, topo_map):
    print(node)
    col_idx = node[0]
    row_idx = node [1]
    height = topo_map[row_idx][col_idx]

    neighbours = []
    if height < 9:
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        for c_i, r_i in directions:
            if (0 <= row_idx + r_i < len(topo_map)) and (0 <= col_idx + c_i < len(topo_map[0])):
                if topo_map[row_idx + r_i][col_idx + c_i] == height + 1:
                    neighbours.append((col_idx + c_i, row_idx + r_i))

    return neighbours

score_sum = 0
for trailhead in trailheads:
    unique_peaks = set()
    queue = deque([trailhead])

    while queue:
        # print(trailheads)
        node = queue.popleft()

        # end of trail
        if topo_map[node[1]][node[0]] == 9:
            unique_peaks.add(node)

        else:
            for neighbour in get_neighbours(node, topo_map):
                queue.append(neighbour)

    score_sum += len(unique_peaks)

print(score_sum)
