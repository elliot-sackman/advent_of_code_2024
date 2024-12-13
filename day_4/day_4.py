import csv
import queue

with open('day_4.txt', 'r') as input_file:
    reader = csv.reader(input_file)

    grid = []
    for row in reader:
        grid.append(row[0])
    
    rows, cols = len(grid), len(grid[0])
    
    dirs = [(0,1), (0,-1), (1,0), (-1,0), (-1,-1), (-1,1), (1,-1), (1,1)]
    total_xmas = 0
    lookup = {'X': 'M', 'M': 'A', 'A': 'S'}

    for x in range(rows):
        for y in range(cols):
            if grid[x][y] == 'X':
                q = queue.Queue()
                q.put((x, y, dirs))

                while not q.empty():
                    r, c, currdirs = q.get()

                    curr = grid[r][c]

                    if curr == 'S':
                        total_xmas += 1
                        continue
                        
                    nxt = lookup[curr]

                    for off_x, off_y in currdirs:
                        if 0 <= r+off_x < rows and 0 <= c+off_y < cols:
                            if grid[r+off_x][c+off_y] == nxt:
                                q.put((r+off_x, c+off_y, [(off_x, off_y)]))
                
    print('Question 1 Answer: ', total_xmas)

with open('day_4.txt', 'r') as input_file:
    reader = csv.reader(input_file)

    grid = []
    for row in reader:
        grid.append(row[0])
    
    rows, cols = len(grid), len(grid[0])
    
    total_x_mas = 0

    for x in range(rows):
        for y in range(cols):
            if x < rows-2 and y < cols-2:
                curr = grid[x][y]

                if curr == 'M' and grid[x+1][y+1] == 'A':
                    if grid[x+2][y] == 'M' and grid[x][y+2] == 'S' and grid [x+2][y+2] == 'S':
                        total_x_mas += 1
                    if grid[x+2][y] == 'S' and grid[x][y+2] == 'M' and grid [x+2][y+2] == 'S':
                        total_x_mas += 1
                elif curr == 'S' and grid[x+1][y+1] == 'A':
                    if grid[x+2][y] == 'M' and grid[x][y+2] == 'S' and grid [x+2][y+2] == 'M':
                        total_x_mas += 1
                    if grid[x+2][y] == 'S' and grid[x][y+2] == 'M' and grid [x+2][y+2] == 'M':
                        total_x_mas += 1
    
    print('Question 2 Answer: ', total_x_mas)