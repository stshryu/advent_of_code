# Day fourteen can be found here: https://adventofcode.com/2023/day/14

import pdb, cProfile
from pprint import pprint

def readfile(filename):
    with open(filename) as f:
        dish = [line.strip() for line in f.read().rstrip().split("\n")]

    dish_len = len(dish[0])
    final_dish = spincycle(dish, 1000000000)

    total = 0
    for count, value in enumerate(reversed(final_dish), start=1):
        total += count * (value.count('O'))

    print(f"Total sum for {filename} is: {total}")

# The logic here is that we want to do our cycles continuously until we meet a dish we've already seen. If we've
# already seen a dish, we no longer need to calculate our cycles since the pattern will just repeat. 
def spincycle(start_dish, total_spins):
    dish_len = len(start_dish[0])
    states = dict.fromkeys([create_state(start_dish)])

    new_dish = start_dish
    while(True):
        new_dish = cycle(new_dish)
        new_dish_state = create_state(new_dish)
        if new_dish_state in states:
            break
        else:
            states[new_dish_state] = None

    # Written out operations for clarity
    keylist = list(states.keys())
    loop_end_index = len(keylist)
    loop_start_index = keylist.index(new_dish_state) 
    loop_length = loop_end_index - loop_start_index
    length_remainder = (1000000000 - loop_start_index) % loop_length
    final_state_index = loop_start_index + length_remainder
    final_state = keylist[final_state_index]
    final_dish = create_dish(final_state, dish_len)
    return final_dish 

def cycle(dish):
    t_dish = dish
    for d in ['N', 'W', 'S', 'E']:
        if d == 'N':
            t_dish = [list(row) for row in zip(*t_dish)]
        elif d == 'W':
            t_dish = t_dish
        elif d == 'S':
            t_dish = [list(row)[::-1] for row in zip(*t_dish)][::-1]
        elif d == 'E':
            t_dish = [list(row)[::-1] for row in t_dish]
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

        if d == 'N':
            t_dish = [list(row) for row in zip(*n_dish)] 
        elif d == 'W':
            t_dish = n_dish
        elif d == 'S':
            t_dish = [list(row)[::-1] for row in zip(*n_dish)][::-1]
        elif d == 'E':
            t_dish = [list(row)[::-1] for row in n_dish]
    return t_dish

def create_state(dish):
    key = ''
    for row in dish:
        key += ''.join(row)
    return key

def create_dish(state, dish_len):
    dish = []
    for i in range(0, len(state), dish_len):
        dish.append(state[i:i + dish_len])
    return dish

readfile('example.txt')

with cProfile.Profile() as pr:
    readfile('input.txt')
    pr.print_stats()
