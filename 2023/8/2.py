# Day eight can be found here: https://adventofcode.com/2023/day/8

import pdb, cProfile
from math import gcd

def readfile(filename):
    with open(filename) as f:
        file = f.read()

    traversal, _nodes = file.split("\n\n")

    # this node parsing is written not because it's legible but because it can be done
    # dictionary keys only keep ordering after 3.6 so we can use the dictionary and iterate through the keys for our nodes.
    nodes = { key_value.split(" = ")[0]: tuple(key_value.split(" = ")[1][1:-1].replace(' ','').split(',')) for key_value in _nodes.strip().split("\n") }

    total_steps = traverse_node_length(traversal, nodes)
    print(f"Total steps required for {filename} is: {total_steps}")

def traverse_node_length(traversal, nodes):
    starting_nodes = [key for key in nodes.keys() if key[-1].endswith('A')]

    # Instead of calculating through each node individually and attempting to check if all the nodes they landed on end in a 'Z'
    # we can instead calculate each starting node's least steps to an end node and find the least common multiple among all nodes.
    steps_per_node = [traverse_node_to_end(traversal, node, nodes) for node in starting_nodes]

    return(least_common_multiple(steps_per_node))

def traverse_node_to_end(traversal, start_node, nodes, step=0):
    current_node = start_node

    while(current_node[-1] != 'Z'):
        # For whatever reason, each input traversal ends at EXACTLY the same location on the traversal map (for my input at 270).
        # This means there is no reason to figure out the offset of each node arriving at their respective endpoints since every
        # node reached is the same within the cycle. 
        for i in range(0, len(traversal)):
            current_node = nodes[current_node][0] if traversal[i] == 'L' else nodes[current_node][1]
            if current_node[-1] == 'Z':
                step += 1
                return step
            step += 1

def least_common_multiple(steps_per_node):
    lcm = 1
    for steps in steps_per_node:
        lcm = lcm * steps // gcd(lcm, steps)
    return lcm

with cProfile.Profile() as pr:
    readfile('example2.txt')
    pr.print_stats()

with cProfile.Profile() as pr:
    readfile('input.txt')
    pr.print_stats()
