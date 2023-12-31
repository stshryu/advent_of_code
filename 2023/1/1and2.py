# Day one can be found here: https://adventofcode.com/2023/day/1
import pdb

# The first part solution is simple, we iterate from the beginning and the end as two separate cursors until the first encountered digits are found
# From the beginning we iterate through i until len(line) from the end we iterate from len(line) to 0. Once both numbers are found concat them together
# and return the value to read_and_sum.

def parse_function_partone(line):
    first_digit = -1
    last_digit = -1
    end = len(line) - 1

    for i in range(0,len(line)):
        if line[i].isdigit() and first_digit == -1:
            first_digit = line[i]
        if line[end].isdigit() and last_digit == -1:
            last_digit = line[end]
        if first_digit != -1  and last_digit != -1:
            break
        end -= 1
    return first_digit + last_digit 

# The second part is going to require us to do some substring searching. A brute force method would be to (for ever non-numeric character) recursively
# seek forward to see if the charstring is a number spelled out in english (one two three etc...) and snap back to the initial seek index until we find a 
# valid english number. Another method (the one shown below) utilizes already known find() and rfind() methods to iteratively find the lowest index 
# substring and the highest index substring before comparing it to the indexes of the digits found in the string to concat the final sum.

def parse_function_parttwo(line):
    nummap = { 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9' }

    first_num, last_num = iterate_through_nums(line)

    first_digit = (-1, -1)
    last_digit = (-1, -1)
    end = len(line) - 1

    for i in range(0, len(line)):
        if line[i].isdigit() and first_digit[1] == -1:
            first_digit = (i, line[i])
        if line[end].isdigit() and last_digit[1] == -1:
            last_digit = (end, line[end])
        if first_digit[1] != -1 and last_digit[1] != -1:
            break
        end -= 1

    final_first = final_last = (-1, -1) 
    if first_num[0] == -1:
        final_first = first_digit[1]
    elif first_digit[0] == -1:
        final_first = nummap[first_num[1]]
    elif first_num[0] > first_digit[0]:
        final_first = first_digit[1]
    else:
        final_first = nummap[first_num[1]]

    if last_num[0] == -1:
        final_last = last_digit[1]
    elif last_digit[0] == -1:
        final_last = nummap[last_num[1]]
    elif last_num[0] < last_digit[0]:
        final_last = last_digit[1]
    else:
        final_last = nummap[last_num[1]]
    
    return final_first + final_last

def iterate_through_nums(line):
    nummap = { 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9' }
    nums = list(nummap.keys())

    lowest_indexes = []
    highest_indexes = []

    for num in nums:
        index = line.find(num)
        if index != -1:
            lowest_indexes.append((index, num))

    for num in nums:
        index = line.rfind(num)
        if index != -1:
            highest_indexes.append((index, num))
            
    sorted_lowest = sorted(lowest_indexes, key=lambda x: x[0]) if len(lowest_indexes) > 0 else [(-1,-1)]
    sorted_highest = sorted(highest_indexes, key=lambda x: x[0]) if len(highest_indexes) > 0 else [(-1,-1)]
    return sorted_lowest[0], sorted_highest[-1]

def read_and_sum_partone(filename):
    cur_sum = 0

    with open(filename) as f:
        for line in f:
            coord = int(parse_function_partone(line))
            cur_sum += coord
    
    print(f"Total Sum for {filename} is: {cur_sum}")

def read_and_sum_parttwo(filename):
    cur_sum = 0

    with open(filename) as f:
        for line in f:
            coord = int(parse_function_parttwo(line))
            cur_sum += coord

    print(f"Total Sum for {filename} in part two is: {cur_sum}")

read_and_sum_partone('example.txt')
read_and_sum_partone('input.txt')

read_and_sum_parttwo('example2.txt')
read_and_sum_parttwo('input.txt')
