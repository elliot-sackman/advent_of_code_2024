from collections import defaultdict

with open('day_11.txt', 'r') as input_file:
    input_data = input_file.read()

    def blink(stone):
        stones = []
        if stone == '0':
            stones.append('1')
        elif len(stone) % 2 == 0:
            middle = len(stone) // 2
            left, right = stone[:middle], stone[middle:]
            stones.append(left)
            stones.append(str(int(right)))
        else:
            stones.append(str(int(stone)*2024))

        return stones

    blinks = 25
    stones = defaultdict(int)
    for stone in input_data.split(' '):
        stones[int(stone)] += 1
    
    for b in range(blinks):
        new_stones = defaultdict(int)

        for stone in stones:
            next_stones = blink(str(stone))
            for nxt in next_stones:
                new_stones[int(nxt)] += stones[stone]
        
        stones = new_stones
    
    print('Question 1 Answer: ', sum(stones.values()))

    blinks = 75
    stones = defaultdict(int)
    for stone in input_data.split(' '):
        stones[int(stone)] += 1
    
    for b in range(blinks):
        new_stones = defaultdict(int)

        for stone in stones:
            next_stones = blink(str(stone))
            for nxt in next_stones:
                new_stones[int(nxt)] += stones[stone]
        
        stones = new_stones

    print('Question 2 Answer: ', sum(stones.values()))