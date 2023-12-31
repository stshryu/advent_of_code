# Day eight can be found here: https://adventofcode.com/2023/day/8

import pdb, cProfile

def readfile(filename):

    file = []
    with open(filename) as f:
        file = f.read()

    traversal, _nodes = file.split("\n\n")

    # this node parsing is written not because it's legible but because it can be done
    # dictionary keys only keep ordering after 3.6 so we can use the dictionary and iterate through the keys for our nodes.
    nodes = { key_value.split(" = ")[0]: tuple(key_value.split(" = ")[1][1:-1].replace(' ','').split(',')) for key_value in _nodes.strip().split("\n") }

    total_steps = traverse_nodes(traversal, nodes)
    print(f"Total steps required for {filename} is: {total_steps}")
    
def traverse_nodes(traversal, nodes, step=0):
    current_node = 'AAA' 

    while(current_node != 'ZZZ'):
        for c in traversal:
            current_node = nodes[current_node][0] if c == 'L' else nodes[current_node][1]
            if current_node == 'ZZZ':
                step += 1
                return step
            step += 1

readfile('example.txt')
readfile('input.txt')
