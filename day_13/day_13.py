import re
from collections import deque

with open('day_13.txt', 'r') as input_file:
    raw_input = input_file.read()
    
    machines = []
    a_regex, b_regex, prize_regex = r'Button A: X\+(\d+), Y\+(\d+)', r'Button B: X\+(\d+), Y\+(\d+)', r'Prize: X=(\d+), Y=(\d+)'
    for line in raw_input.split('\n'):
        if re.findall(a_regex, line): 
            machines.append([])
            machines[-1].append(re.findall(a_regex, line)[0])
        elif re.findall(b_regex, line):
            machines[-1].append(re.findall(b_regex, line)[0])
        elif re.findall(prize_regex, line):
            machines[-1].append(re.findall(prize_regex, line)[0])
    
    '''
    for machine in machines:
        a, b, prize = machine[0], machine[1], machine[2]

        prize_x, prize_y = int(prize[0]), int(prize[1])
        dp = [[401 for i in range(prize_y + 1)] for j in range(prize_x + 1)]
        dp[0][0] = 0

        # A first
        x, y = int(a[0]), int(a[1])
        for i in range(x, prize_x+1):
            for j in range(y, prize_y+1):
                    dp[i][j] = min(dp[i][j], dp[i-x][j-y] + 3)
        
        # B second
        x, y = int(b[0]), int(b[1])
        for i in range(x, prize_x+1):
            for j in range(y, prize_y+1):
                    dp[i][j] = min(dp[i][j], dp[i-x][j-y] + 1)
        
        print(dp[-1][-1])
    '''
    '''
    for machine in machines:
        a, b, prize = machine[0], machine[1], machine[2]
        xa, ya, cost_a, xb, yb, cost_b, x_prize, y_prize = int(a[0]), int(a[1]), 3, int(b[0]), int(b[1]), 1, int(prize[0]), int(prize[1])
        visited = {}
        q = deque()

        q.append((0, 0, 0))

        while len(q) > 0:
            x, y, tokens = q.popleft()

            # if we've reached this point with fewer tokens, we skip
            if (x, y) in visited and visited[(x, y)] < tokens:
                continue

            visited[(x, y)] = tokens
            
            # If we're at or past the prize, we don't need to keep pressing buttons
            if x >= x_prize or y >= y_prize:
                continue

            q.append((x+xa, y+ya, tokens+3))
            q.append((x+xb, y+yb, tokens+1))
        
        if (x_prize, y_prize) in visited:
            print(visited[(x_prize, y_prize)])
    '''
    
    total_tokens = 0
    for machine in machines:
        a, b, prize = machine[0], machine[1], machine[2]
        xa, ya, cost_a, xb, yb, cost_b, x_prize, y_prize = int(a[0]), int(a[1]), 3, int(b[0]), int(b[1]), 1, int(prize[0]), int(prize[1])

        min_tokens = 401
        for tokens in range(1, 401):
            max_a = tokens // 3

            for num_a in range(max_a + 1):
                num_b = tokens - (3*num_a)

                x = num_a * xa + num_b * xb
                y = num_a * ya + num_b * yb
                if x == x_prize and y == y_prize:
                    min_tokens = tokens
                    break
        
        if min_tokens < 401:
            total_tokens += min_tokens
            print(machine, min_tokens)

    print('Question 1 Answer: ', total_tokens)