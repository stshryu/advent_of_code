# Day fourteen can be found here: https://adventofcode.com/2023/day/14

import pdb, cProfile
from pprint import pprint

def readfile(filename):
    with open(filename) as f:
        dish = [line.strip() for line in f.read().rstrip().split("\n")]
    new_dish = move(dish)

    total = 0
    for count, value in enumerate(reversed(new_dish), start=1):
        total += count * (value.count('O'))

    print(f"Total sum for {filename} is: {total}")

def move(dish):
    # Swap row and columns
    t_dish = [list(row) for row in zip(*dish)]
    n_dish = []
    for row in t_dish:
        cube_index = [index for index, value in enumerate(row) if value == '#']
        rock_index = [index for index, value in enumerate(row) if value == 'O']

        current_index = 0
        shifted_rock_index = []
        if cube_index:
            for ci in range(len(cube_index)):
                shifted_rock_index.append(([i for i in rock_index if current_index <= i < cube_index[ci]], range(current_index, cube_index[ci] + 1)))
                current_index = cube_index[ci] + 1
                if cube_index[ci] == cube_index[-1]:
                    shifted_rock_index.append(([i for i in rock_index if current_index <= i < len(row)], range(current_index, len(row))))
        else:
            shifted_rock_index = [([i for i in rock_index], range(0, len(row) - 1))]

        new_row = ['.' for _ in range(len(row))]

        current_index = 0
        for ci in cube_index:
            new_row[ci] = '#'

        for rocks in shifted_rock_index:
            if len(rocks[0]) != 0:
                for i in range(rocks[1].start, rocks[1].start + len(rocks[0])):
                    new_row[i] = 'O'

        n_dish.append(new_row)

    # Swap row and column back
    return [list(row) for row in zip(*n_dish)] 

readfile('example.txt')
readfile('input.txt')
