import csv
from collections import deque

with open('day_12.txt', 'r') as input_file:
    reader = csv.reader(input_file)

    grid = []

    for row in reader:
        grid.append(row[0])

    seen = set()

    rows, cols = len(grid), len(grid[0])
    directions = [(1,0), (0,1), (-1,0), (0,-1)]

    total_price = 0
    for i in range(rows):
        for j in range(cols):
            curr = grid[i][j]

            if (i, j) in seen:
                continue

            q = deque()

            q.append((i, j))

            region = set()
            perimeter = 0
            while len(q) > 0:
                r, c = q.popleft()

                if (r, c) in region:
                    continue

                region.add((r, c))
                seen.add((r, c))

                for x, y in directions:
                    if 0 <= r+x < rows and 0 <= c+y < cols:
                        if grid[r+x][c+y] == curr:
                            q.append((r+x, c+y))
                        else:
                            perimeter += 1
                    else:
                        perimeter += 1
            
            # print(curr, ' perimeter is ', perimeter, ' and area is ', len(region))
            total_price += perimeter * len(region)
    
    print('Question 1 Answer: ', total_price)

with open('day_12.txt', 'r') as input_file:
    reader = csv.reader(input_file)

    grid = []

    for row in reader:
        grid.append(row[0])

    seen = set()

    rows, cols = len(grid), len(grid[0])
    directions = [(1,0), (0,1), (-1,0), (0,-1)]

    total_price = 0
    for i in range(rows):
        for j in range(cols):
            curr = grid[i][j]

            if (i, j) in seen:
                continue

            q = deque()
            
            # Add starting position, empty set to contain direction of sides, and a tuple that stores previous position
            q.append((i, j, set(), (-1, -1)))

            region = {}
            sides = 0
            while len(q) > 0:
                r, c, curr_sides, prev = q.popleft()

                if (r, c) in region:
                    continue

                region[(r, c)] = curr_sides # Keep track of which sides we counted on a given spot
                seen.add((r, c))

                # First loop through directions and check for new sides or remove sides
                for x, y in directions:
                    # If we look in a direction and see an edge, check if it's accounted for
                    if not (0 <= r+x < rows and 0 <= c+y < cols) or grid[r+x][c+y] != curr:
                        if (x, y) not in curr_sides:
                            sides += 1
                        
                        curr_sides.add((x, y))
                    # If we look in a direction and the region continues, remove that directions from curr_sides if it's there
                    elif 0 <= r+x < rows and 0 <= c+y < cols and grid[r+x][c+y] == curr:
                        if (x, y) in curr_sides:
                            curr_sides.remove((x, y))
                
                # Then queue up the next coords
                for x, y in directions:
                    if 0 <= r+x < rows and 0 <= c+y < cols and grid[r+x][c+y] == curr:
                        # If it's already been visited, and isn't the previous spot visited, see if we accounted for a side that we added earlier
                        if (r+x, c+y) in region and (r+x, c+y) != prev:
                            next_sides = region[(r+x, c+y)]
                            for dir in next_sides:
                                # We've visited that spot and counted a same side at some point in the chain, meaning we double counted
                                if dir in curr_sides:
                                    sides -= 1
                        else:
                            q.append((r+x, c+y, curr_sides.copy(), (r,c)))
    
    print('Question 2 Answer: ', total_price)