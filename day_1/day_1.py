import csv
import heapq
from collections import Counter

with open('day_1.csv', 'r') as input_data:
    reader = csv.reader(input_data)

    left, right = [], []

    for row in reader:
        heapq.heappush(left, int(row[0]))
        heapq.heappush(right, int(row[1]))

    distance = 0
    
    if len(left) != len(right):
        raise Exception('Lists are not the same length!')
    
    while left and right:
        l, r = heapq.heappop(left), heapq.heappop(right)
        distance += abs(l - r)
    
    print('Question 1 Answer: ', distance)

with open('day_1.csv', 'r') as input_data:
    reader = csv.reader(input_data)

    left, right = [], []

    for row in reader:
        left.append(int(row[0]))
        right.append(int(row[1]))

    counter = Counter(right)

    score = 0

    for num in left:
        score += num*counter[num]

    print('Question 2 Answer: ', score)
    