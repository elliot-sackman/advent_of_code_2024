import csv

with open('day_8.txt', 'r') as input_file:
    reader = csv.reader(input_file)

    grid = []

    for row in reader:
        grid.append([ele for ele in row[0]])
    
    rows, cols = len(grid), len(grid[0])

    nodes = {}
    for i in range(rows):
        for j in range(cols):
            curr = grid[i][j]
            if curr != '.':
                if curr not in nodes:
                    nodes[curr] = []
                
                nodes[curr].append((i, j))
    
    antinodes = set()
    for key in nodes:
        key_nodes = nodes[key]

        for i in range(len(key_nodes)):
            for j in range(i+1, len(key_nodes)):
                r1, c1 = key_nodes[i]
                r2, c2 = key_nodes[j]

                r_diff, c_diff = r2 - r1, c2 - c1

                # Look up-left
                if 0 <= r1 - r_diff < rows and 0 <= c1 - c_diff < cols:
                    antinodes.add((r1 - r_diff, c1 - c_diff))
                
                # Look down-right
                if 0 <= r2 + r_diff < rows and 0 <= c2 + c_diff < cols:
                    antinodes.add((r2 + r_diff, c2 + c_diff))
    
    print('Question 1 Answer: ', len(antinodes))
    
    antinodes_2 = set()
    for key in nodes:
        key_nodes = nodes[key]

        for i in range(len(key_nodes)):
            for j in range(i+1, len(key_nodes)):
                r1, c1 = key_nodes[i]
                r2, c2 = key_nodes[j]

                # Any two antennas become antinodes
                antinodes_2.add((r1, c1))
                antinodes_2.add((r2, c2))

                r_diff, c_diff = r2 - r1, c2 - c1

                # Look up-left

                while 0 <= r1 - r_diff < rows and 0 <= c1 - c_diff < cols:
                    antinodes_2.add((r1 - r_diff, c1 - c_diff))
                    r1 -= r_diff
                    c1 -= c_diff
                
                # Look down-right
                while 0 <= r2 + r_diff < rows and 0 <= c2 + c_diff < cols:
                    antinodes_2.add((r2 + r_diff, c2 + c_diff))
                    r2 += r_diff
                    c2 += c_diff

    print('Question 2 Answer: ', len(antinodes_2))