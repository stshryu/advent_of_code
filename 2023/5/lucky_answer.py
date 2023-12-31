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

    for i in range(0, len(seeds), 2):
        for j in range(seeds[i], seeds[i] + seeds[i+1], 1000000):
            seed_loc[j] = map_to_map(j, maps)
    
    mkey, mval = min(seed_loc.items(), key=lambda x: x[1])

    min_band = None
    for i in range(0, len(seeds), 2):
        start = seeds[i]
        end = seeds[i] + seeds[i+1]

        min_band = (start, end) if mkey in range(start, end) else min_band

        if min_band:
            break
    
    seed_loc = {}
    for i in range(min_band[0], min_band[1], 1000):
        seed_loc[i] = map_to_map(i, maps)

    mkey2, mval2 = min(seed_loc.items(), key=lambda x: x[1])

    seed_loc = {}
    for i in range(mkey2 - 10000, mkey2 + 10001):
        seed_loc[i] = map_to_map(i, maps)

    mkey3, mval3 = min(seed_loc.items(), key=lambda x: x[1])

    pdb.set_trace() 
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

#read_and_parse('example.txt')
#read_and_parse('input.txt')
read_and_parse('kevininput.txt')
