# Day three can be found here: https://adventofcode.com/2023/day/3

import pdb

def read_file(filename):
    input_array = [] 

    with open(filename) as f:
        for line in f:
            input_array.append([c for c in line.rstrip("\n")])

    return input_array
            
def parse_input(input_array):
    new_input_array = input_array
    total_sum = 0

    # Iterate through the 2D array
    for y in range(0, len(new_input_array)):
        for x in range(0, len(new_input_array[y])):
            if is_symbol(new_input_array[y][x]):
                new_input_array, subsum = seek_around_symbol(y, x, new_input_array)
                total_sum += subsum

    return total_sum

def is_symbol(c):
    if c == "." or c.isalnum():
        return False
    return True

def seek_around_symbol(y, x, input_array):
    # Initial coordinates unknown
    upper_left_coord = [-1, -1]
    lower_right_coord = [-1, -1]

    # Find the upper left corner
    upper_left_coord[1] = y if y - 1 < 0 else y - 1
    upper_left_coord[0] = x if x - 1 < 0 else x - 1

    # Find the lower right corner
    lower_right_coord[1] = y if y + 1 >= len(input_array) else y + 1
    lower_right_coord[0] = x if x + 1 >= len(input_array[0]) else x + 1

    new_input_array = input_array
    subsum = 0
    for i in range(upper_left_coord[1], lower_right_coord[1] + 1):
        for j in range(upper_left_coord[0], lower_right_coord[0] + 1):
            if new_input_array[i][j].isalnum():
                new_input_array, num = find_and_replace_number(new_input_array, i, j)
                subsum += int(num)
                
    return new_input_array, subsum

def find_and_replace_number(input_array, i, j):
    num_start = num_end = j 

    for left in range(j, -1, -1):
        if input_array[i][left].isalnum():
            num_start = left
        else:
            break

    for right in range(j, len(input_array[i])):
        if input_array[i][right].isalnum():
            num_end = right
        else:
            break

    num = ""
    for y in range(num_start, num_end + 1):
        num += input_array[i][y]
        input_array[i][y] = "."

    return input_array, num


input_array = read_file("example.txt")
total = parse_input(input_array)
print(f"Total for example is: {total}")

input_array = read_file("input.txt")
total = parse_input(input_array)
print(f"Total for input is: {total}")
