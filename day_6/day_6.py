import csv

with open('day_6.txt', 'r') as input_file:
    reader = csv.reader(input_file)

    grid = []

    start_r, start_c = -1, -1
    for row_num, row in enumerate(reader):
        grid.append(row[0])
        if '^' in row[0]:
            start_r, start_c = row_num, row[0].index('^')
    
    rows, cols = len(grid), len(grid[0])

    dirmap = {
        (-1,0): (0, 1),
        (0, 1): (1, 0),
        (1, 0): (0,-1),
        (0,-1): (-1,0)
    }

    direction = (-1, 0)
    visited = set()
    locations = 0
    r, c = start_r, start_c

    while 0 <= r < rows and 0 <= c < cols:
        if (r, c) not in visited:
            locations += 1
        
        visited.add((r, c))
        x, y = direction

        # Do we change direction or not
        if 0 <= r + x < rows and 0 <= c + y < cols and grid[r+x][c+y] == '#':
            direction = dirmap[direction]
            continue
        
        r += x
        c += y

    print('Question 1 Answer: ', locations)

    def traverse_until_loop_detected(r, c, direction, new_grid):
        new_visited = set()

        while 0 <= r < rows and 0 <= c < cols:
            if (r, c, direction) in new_visited:
                return True
            
            new_visited.add((r, c, direction))
            x, y = direction

            # Do we change direction or not
            if 0 <= r + x < rows and 0 <= c + y < cols and new_grid[r+x][c+y] == '#':
                direction = dirmap[direction]
                continue
        
            r += x
            c += y
        
        return False
    
    r, c = start_r, start_c

    direction = (-1, 0)

    new_obstacles = set()
    visited = set()

    # Walk the path again and try placing an obstacle at the next space to see if it creates a loop
    while 0 <= r < rows and 0 <= c < cols:
        x, y = direction

        visited.add((r, c))

        # Do we change direction or not
        if 0 <= r + x < rows and 0 <= c + y < cols and grid[r+x][c+y] == '#':
            direction = dirmap[direction]
            continue
        
        # Try placing an obstacle at the next position and see if you can detect a loop
        # Don't place an obstacle in the path itself and don't double count new obstacles in the same positions
        if 0 <= r + x < rows and 0 <= c + y < cols and (r+x, c+y) not in new_obstacles and (r+x, c+y) not in visited:
            new_grid = [[char for char in row] for row in grid]
            new_grid[r+x][c+y] = '#'

            if traverse_until_loop_detected(r, c, direction, new_grid):
                new_obstacles.add((r+x, c+y))
        
        r += x
        c += y
    
    print('Question 2 Answer: ', len(new_obstacles))
        