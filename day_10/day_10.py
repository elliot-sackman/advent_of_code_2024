import csv
from collections import deque

with open('day_10.txt', 'r') as input_file:
    reader = csv.reader(input_file)

    grid = []
    trailheads = []

    for i, row in enumerate(reader):
        grid.append([int(num) for num in row[0]])

        for j, char in enumerate(row[0]):
            if char == '0':
                trailheads.append((i, j))
    
    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    rows, cols = len(grid), len(grid[0])

    trailhead_score = 0
    for trailhead in trailheads:
        r, c = trailhead

        seen = set()

        nines = set()

        q = deque()

        q.append((r, c))

        while len(q) > 0:
            x, y = q.popleft()

            if (x, y) in seen:
                continue
                
            seen.add((x, y))

            if grid[x][y] == 9:
                nines.add((x, y))
                continue

            height = grid[x][y]

            for i, j in directions:
                if 0 <= x + i < rows and 0 <= y + j < cols:
                    if grid[x+i][y+j] == height + 1:
                        q.append((x+i, y+j))
        
        trailhead_score += len(nines)

    print('Question 1 Answer: ', trailhead_score)

    trailhead_ratings = 0
    
    for trailhead in trailheads:
        r, c = trailhead
        dp = [[0 for j in range(cols)] for i in range(rows)]
        dp[r][c] = 1

        q = deque()

        q.append((r, c))
        
        while len(q) > 0:
            x, y = q.popleft()
                
            if grid[x][y] == 9:
                trailhead_ratings += dp[x][y]
                continue

            height = grid[x][y]
            trail_rating = dp[x][y]

            for i, j in directions:
                if 0 <= x + i < rows and 0 <= y + j < cols:
                    if grid[x+i][y+j] == height + 1:
                        if dp[x+i][y+j] == 0:
                            q.append((x+i, y+j))
                            
                        dp[x+i][y+j] += trail_rating

        
    print('Question 2 Answer: ', trailhead_ratings)