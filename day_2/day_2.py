import csv

# Default check for increase, will pass in row forwards and backwards
def is_safe(row):
    prev = -1

    for num in row:
        if prev == -1:
            prev = int(num)
            continue

        if int(num) <= prev or int(num) - prev > 3:
            return False
        
        prev = int(num)
        
    return True
    


with open('day_2.csv', 'r') as input_file:
    reader = csv.reader(input_file)

    num_safe = 0
    for row in reader:
        if is_safe(row) or is_safe(row[::-1]):
            num_safe += 1
    
    print('Question 1 Answer: ', num_safe)

def is_or_can_be_made_safe(row):
    if is_safe(row):
        return True
    
    for index in range(len(row)):
        if is_safe(row[:index] + row[index+1:]):
            return True
    
    return False

with open('day_2.csv', 'r') as input_file:
    reader = csv.reader(input_file)

    num_safe = 0
    for row in reader:
        if is_or_can_be_made_safe(row) or is_or_can_be_made_safe(row[::-1]):
            num_safe += 1
        else:
            print(row)

    print('Question 2 Answer: ', num_safe)