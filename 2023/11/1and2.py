# Day eleven can be found here: https://adventofcode.com/2023/day/11

import pdb, cProfile

def readfile(filename):
    galaxy_map = []

    with open(filename) as f:
        for line in f:
            galaxy_map.append([ c for c in line.strip()])

    empty_rows, empty_cols = galaxy_expansion(galaxy_map)
    galaxy_loc = assign_galaxies(galaxy_map)
    total_dist = calculate_dist(galaxy_loc, *galaxy_expansion(galaxy_map))

    print(f"Total distance for {filename} is: {total_dist}")

def galaxy_expansion(galaxy_map):
    galaxies = []
    for i in range(0, len(galaxy_map)):
        for j in range(0, len(galaxy_map[i])):
            galaxies.append((j, i)) if galaxy_map[i][j] == '#' else None 
    row_galaxy = { t[1] for t in galaxies }
    col_galaxy = { t[0] for t in galaxies }

    empty_rows = sorted(set(range(0, len(galaxy_map))) - row_galaxy, reverse=True)
    empty_cols = sorted(set(range(0, len(galaxy_map[0]))) - col_galaxy, reverse=True)

    return empty_rows, empty_cols

def assign_galaxies(galaxy_map):
    key = 0
    galaxy_loc = {}
    for i in range(0, len(galaxy_map)):
        for j in range(0, len(galaxy_map[i])):
            if galaxy_map[i][j] == '#':
                galaxy_loc[key] = (i, j)
                key += 1

    return galaxy_loc

def calculate_dist(galaxy_loc, empty_rows, empty_cols):
    keys = list(galaxy_loc.keys())
    dist = 0
    #expansion_rate = 2 # Solution to part one
    expansion_rate = 1000000 

    # Figure out how many times while traveling from galaxy to galaxy we traverse any empty rows or columns and multiply that by the expansion rate
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            start_loc = galaxy_loc[i] 
            end_loc = galaxy_loc[j]
            row_offset = (start_loc[0], end_loc[0]) if start_loc[0] >= end_loc[0] else (end_loc[0], start_loc[0])
            col_offset = (start_loc[1], end_loc[1]) if start_loc[1] >= end_loc[1] else (end_loc[1], start_loc[1])
            row_count = len([x for x in empty_rows if row_offset[1] <= x <= row_offset[0]])
            col_count = len([x for x in empty_cols if col_offset[1] <= x <= col_offset[0]])
            dist += abs(start_loc[0] - end_loc[0]) + abs(start_loc[1] - end_loc[1]) + (row_count * (expansion_rate - 1)) + (col_count * (expansion_rate - 1))

    return dist

readfile('example.txt')
readfile('input.txt')
