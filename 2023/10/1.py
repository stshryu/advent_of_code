# Day ten can be found here: https://adventofcode.com/2023/day/10

import pdb, cProfile
from pprint import pprint

move = { 'W': (0, -1), 'S': (1, 0), 'E': (0, 1), 'N': (-1, 0) }
opposite_direction = { 'N': 'S', 'S': 'N', 'E': 'W', 'W':'E' }
pipemap = {
    '|': { 'S': 'S', 'N': 'N' },
    '-': { 'W': 'W', 'E': 'E' },
    'L': { 'S': 'E', 'W': 'N' },
    'J': { 'S': 'W', 'E': 'N' },
    '7': { 'N': 'W', 'E': 'S' },
    'F': { 'N': 'E', 'W': 'S' }
}

# This solution was inspired by this github user: TheBlackOne under his Advent-of-Code repository.
def parsefile(filename):
    maze = []

    with open(filename) as f:
        for line in f:
            maze.append(line.strip())

    step, inside_tiles = readmaze(maze)
    print(f"Total step: {str(int(step/2))}")
    print(f"{inside_tiles=}")

def readmaze(maze):
    coords = []
    for y in range(0, len(maze)):
        for x in range(0, len(maze[y])):
            if maze[y][x] == 'S':
                start = (y, x)
                coords.append((y, x))

    last_directions = []

    for direction, (y_offset, x_offset) in move.items():
        if direction in last_directions:
            continue

        step = 1
        y = start[0] + y_offset
        x = start[1] + x_offset

        if x < 0 or y < 0 or maze[y][x] == ".":
            continue

        current_node = maze[y][x]
        while current_node in pipemap.keys():
            current_directions = pipemap[current_node]
            if direction not in current_directions.keys():
                break
            direction = current_directions[direction]
            (y_offset, x_offset) = move[direction]
            y += y_offset
            x += x_offset
            coords.append((y, x))
            current_node = maze[y][x]
            step += 1
            
        if current_node == 'S':
            inside_tiles = shoelace(coords, step)
            return step, inside_tiles

# Copy and pasting day 18 solution for shoelace + picks theorum here.
def shoelace(coords, perimeter):
    y, x = zip(*coords)
    area = abs(sum(i * j for i, j in zip(x, y[1:] + y[:1])) - sum(i * j for i, j in zip(x[1:] + x[:1], y ))) / 2
    return area + 1 - (perimeter/2)

parsefile('example3.txt')
parsefile('example.txt')
parsefile('example2.txt')
parsefile('input.txt')
