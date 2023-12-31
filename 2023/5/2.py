# Day five can be found here: https://adventofcode.com/2023/day/5

import pdb, cProfile, sys

def read_file(filename):
    with open(filename) as f:
        seeds, *raw_maps = f.read().split("\n\n")
    seeds = seeds.split()[1:]
    seeds = sorted([(int(seeds[i]), int(seeds[i + 1])) for i in range(0, len(seeds), 2)], key=lambda x: x[1])

    maps = []
    for _map in raw_maps:
        key, coords = _map.split(":")

        # I made this mapping to prove I can do list comprehensions (to myself) don't ever do this
        maps.append(sorted([[int(in_c) for in_c in c.split()] for c in coords.strip().split("\n")], key=lambda x: x[0]))

    seed_endpoints = reverse_transformation(seeds, maps)
    valid_seeds = []
    for i in seeds:
        for seed in seed_endpoints:
            # This line is a neat trick Kevin found out about indexing into ranges to test for membership within said range
            if seed in range(i[0], i[0] + i[1]):
                valid_seeds.append(seed)

    final_loc = transform_seeds(valid_seeds, maps)
    print(f"The lowest seed location for {filename} is: {final_loc}")

# We want to traverse from the location backwards, to get the valid endpoints of each of our "virtual bands" between
# the mappings. We want to invert each linear mapping and find the endpoints of the segments where the discontinuities
# happen. This will give us the exact seed id's that happen right before, and right after a "transformation" in the 
# location value.
def reverse_transformation(seeds, maps):
    # Everything from 1-infinity is one to one mapping initially 
    size_range = [0, sys.maxsize]
    for i in maps[::-1]:
        size_range = map_endpoints(i, size_range)
    
    return size_range

# Note: as I implemented my idea I ran into various errors with the range banding as I iterated through the 
# example code. I took some inspiration from here: https://tinyurl.com/2amb7tcm to help me find all the bands
# that I was missing.
# 
# This is the big kahuna. I've got a pen and paper with scrawls that covers what exactly is happening here but the 
# basic gist is that instead of using our read_map() method we're going to be using our reverse_search() method.
# This method starts from the end (the location ranges) versus the start (the seed ranges) and works backwards to 
# figure out where each discontinuity occurs. For example, from location to humidty each disconnect occurs from 
#
# 0 to 55 and 56 to 92 and 93 to 96 and 97 to infinity
# Since our locations increases monotonically (+1 every single linked increment with humidity) we know that since
# the example ranges from 56 -> 93 we need to check both values 55 and 92. Same goes for 93 to 97, we have to 
# check 96. This brings our endpoints based on our bands to [0,55,56,92,93,96,97,sys.maxsize]. maxsize stands
# in for infinity.
#
# if we map humidity to temperature we get an additional set of endpoints, this is where as you increment through
# humidity, you will see a change in location (meaning from our previous bands we need to take into account the 
# LAST value in the band (since 0 to 55 is [inclusive, exclusive)) we need to check the value 54 in addition to 
# the value 55 in the humidity values. Meaning we are left with this:
#
# [0,54,55,68,69,70,92,93,96,97,maxsize]
#
# if we take ANY of the valid temperature values, and start converting them into humidity and then into location
# these are the locations of the temperature values that will discontinue the +1 linked incrementation, since
# this is where the defined transformations are. We repeat this transformation until we finally reach the end 
# state which is a list of endpoints that contains every single seed where a transformation on location occurs
# 
# [0,13,14,15,21,22,25,26,43,44,49,50,51,52,53,54,58,59,61,62,65,66,68,69,70,71,81,82,91,92,93,97,98,99,100,inf] 
#
# This means that if we were to iterate through every valid seed id in our example set, between these values
# if there are ranges between these values to iterate through, the location would increment in parity with 
# our seed (+1 per) until our seed id hits one of these values, after which some transformation causes the 
# location value to change. This means that these values, at the edges of these contiguous incrementation 
# ranges will eventually give us the lowest possible seed to location mapping.
def map_endpoints(map_to_map, size_range):
    # map_to_map is similar to the P1 solution function. It contains the inner mapping ranges for each transform
    endpoints = [[(dest, src), (dest + size - 1, src + size - 1)] for (dest, src, size) in map_to_map]

    # squash all the discrete list of ranges from map_to_map into one singular master list
    endpoints = [item for sublist in endpoints for item in sublist]

    # reverse search gives us the range of the previous list. The range for location was sent from the previous
    # function call as [0,sys.maxsize]. A range of (basically infinity) but it only contains 2 items. As we 
    # iterate through each reverse mapping, we'll be adding to these endpoints. The function reverse_search()
    # will check whether or not we need to add new source endpoints for this particular mapping.
    # Instead of checking values in our read_map() function, we're checking for the range of valid values 
    # based on the mapping rules of this specific transformation. Can probably clean this up with code found 
    # here: https://old.reddit.com/r/adventofcode/comments/18cedl0/2023_day_05_python_3_cool_data_structure_trick/
    dest_endpoints = sorted([reverse_search(map_to_map, j) for j in size_range])
    src_endpoints = sorted(set([x for (y, x) in endpoints]))

    # if the last value in our source endpoints is greater than 0 we want to add back in 0 and another endpoint 
    # that is 1 less than the previous value. This is necessary because our ranges are [inclusive, exclusive).
    # Check line 51-54 for the explanation why we need to expand this band by one.
    if src_endpoints[0] > 0:
        src_endpoints = [0, src_endpoints[0] - 1] + src_endpoints

    # check line 51-54 for explanation
    if src_endpoints[-1] < sys.maxsize:
        src_endpoints = src_endpoints + [src_endpoints[-1] + 1, sys.maxsize]

    # once we have our valid src endpoints lets find the intersections between the destination and source sets
    src_endpoints = sorted(set(dest_endpoints) | set(src_endpoints))

    # if you would like to see the endpoints generated in real time uncomment these two lines below:
    #print(src_endpoints)
    #pdb.set_trace()

    return src_endpoints

def reverse_search(map_to_map, j):
    for (dest, src, size) in map_to_map:
        if dest <= j < dest + size:
            return src + (j - dest)
    return j

def transform_seeds(seeds, maps):
    seed_loc = {}

    for seed in seeds:
        seed_loc[seed] = map_to_map(seed, maps)

    return min(seed_loc.values())

def map_to_map(seed, maps):
    transformed_val = seed

    for m in maps:
        transformed_val = read_map(transformed_val, m)

    return transformed_val

def read_map(x, m):
    for i in m:
        dest, src, size = i

        if x in range(src, src + size):
            return dest + x - src 
    return x


read_file('example.txt')
read_file('input.txt')
