import re

with open('day_3.txt', 'r') as input_file:
    data = input_file.read()
    pattern = r'mul\((\d+,\d+)\)'

    total = 0
    for pair in re.findall(pattern, data):
        num1, num2 = pair.split(',')
        total += int(num1) * int(num2)
    
    print("Question 1 Answer: ", total)

with open('day_3.txt', 'r') as input_file:
    data = input_file.read()
    do_pattern = r'do\(\)'
    dont_pattern = r'don\'t\(\)'
    mul_pattern = r'mul\((\d+,\d+)\)'

    def recursive_selective_multiply(input, do, total):
        if not input:
            return 

        if do:
            if re.search(dont_pattern, input):
                end_do = re.search(dont_pattern, input).end()
            else: 
                end_do = len(input)
            
            for pair in re.findall(mul_pattern, input[:end_do+1]):
                num1, num2 = pair.split(',')
                total += int(num1) * int(num2)
            
            return recursive_selective_multiply(input[end_do:], False, total)
        else:
            if re.search(do_pattern, input):
                end_dont = re.search(do_pattern, input).end()
            else:
                return total

            return recursive_selective_multiply(input[end_dont:], True, total)

    answer = recursive_selective_multiply(data, True, 0)
    print('Question 2 Answer: ', answer)