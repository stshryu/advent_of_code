# Day fifteen can be found here: https://adventofcode.com/2023/day/15

import pdb, cProfile

def readfile(filename):
    with open(filename) as f:
        seq = f.read().strip().split(',')
    boxes = HASHMAP(seq)

    focusing_power = 0
    for i in list(boxes.keys()):
        if len(boxes[i]) > 0:
            keylist = list(boxes[i].keys())
            for j in range(len(keylist)):
                focusing_power += (i + 1) * (j + 1) * boxes[i][keylist[j]]

    print(f"Focusing power for {filename} is: {focusing_power}")
    
# Part 2
def HASHMAP(instructions):
    boxes = {key: {} for key in range(0, 256)}

    for instruction in instructions:
        operation = (instruction.split("=")) if "=" in instruction else (instruction.split("-")[0], "-") 
        box = HASH(operation[0])
        label = operation[0]

        if operation[1] == '-':
            void = boxes[box].pop(label) if label in boxes[box] else None
        else:
            boxes[box][label] = int(operation[1])
    return boxes

# Part 1
def HASH(string):
    current_val = 0
    for c in string:
        current_val += ord(c)
        current_val *= 17
        current_val = current_val % 256
    return current_val

readfile('example.txt')
readfile('input.txt')
