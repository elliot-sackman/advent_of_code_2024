import csv

with open('day_7.txt', 'r') as input_file:
    reader = csv.reader(input_file)

    answer = 0
    operators = ['*', '+' , '||'] # Added || for part II, can get the answer for pt. I by removing that last element.

    def operate(operator, num1, num2):
        if operator == '*':
            return num1 * num2
        elif operator == '+':
            return num1 + num2
        elif operator == '||':
            return int(str(num1) + str(num2))

    def recursive_operate(objective, inputs, operators, index):
        if index == len(inputs) and inputs[index-1] == objective:
            return True
        
        if index == len(inputs) or inputs[index-1] > objective:
            return False
        
        for operator in operators:
            curr, prev = inputs[index], inputs[index-1] # Save the current value
            inputs[index] = operate(operator, prev, curr)
            if (recursive_operate(objective, inputs, operators, index+1)):
                return True
            
            # Reset the value to current before running again
            inputs[index] = curr

    for row in reader:
        objective, inputs = int(row[0].split(': ')[0]), [int(num) for num in ''.join(row[0].split(': ')[1]).split(' ')]
        orig = inputs.copy()
        if recursive_operate(objective, inputs, operators, 1):
            print(objective, inputs, orig)
            answer += objective
    
    print('\nAnswer: ', answer)