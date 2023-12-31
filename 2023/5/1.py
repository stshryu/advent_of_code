# Day five can be found here: https://adventofcode.com/2023/day/5

import pdb, cProfile

def read_and_parse(filename):
    with open(filename) as f:
        seeds, *raw_maps = f.read().split("\n\n")

    seeds = [int(seed) for seed in seeds.split()[1:]] 
    maps = [] 
    for _map in raw_maps:
        key, coords = _map.split(":")
        maps.append(sorted([c.split() for c in coords.strip().split("\n")], key=lambda x: x[0]))

    min_val = transform_seeds(seeds, maps)
    print(f"Minimum location for {filename} is: {min_val}")

def transform_seeds(seeds, maps):
    seed_loc = {}
    
    for seed in seeds:
        seed_loc[seed] = map_to_map(seed, maps)

    return min(seed_loc.values())

def map_to_map(seed, maps):
    transformed_seed = seed

    for m in maps:
        transformed_seed = read_map(transformed_seed, m)

    return transformed_seed

def read_map(x, m):
    for i in m:
        dest = int(i[0])
        source = int(i[1])
        offset = int(i[2])
        
        if x in range(source, source + offset): 
            return dest + x - source
    return x

read_and_parse('example.txt')
read_and_parse('input.txt')
