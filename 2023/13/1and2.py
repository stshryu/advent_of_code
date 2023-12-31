# Day thirteen can be found here: https://adventofcode.com/2023/day/13

import pdb, cProfile
from pprint import pprint

def readfile(filename):
    with open(filename) as f:
        mazes = [line.rstrip().split("\n") for line in f.read().split("\n\n")]

    total = 0
    for maze in mazes:
        total += get_axis(maze) 

    print(f"Total note sum for {filename} is: {total}")

def get_axis(maze):
    # Row
    for i in range(len(maze)):
        smudge = 0
        next_row = maze[i+1] if i + 1 < len(maze) else None
        if next_row:
            valid, smudge = is_valid(maze[i], next_row, smudge)
            if valid:
                valid, smudge = is_mirror_row(maze, i, smudge)
                if valid and smudge == 0:
                    continue
                elif valid:
                    return 100 * (i + 1)

    # Col
    for j in range(len(maze[0])):
        smudge = 0
        col = ''.join([maze[i][j] for i in range(len(maze))])
        next_col = ''.join([maze[i][j+1] for i in range(len(maze))]) if j + 1 < len(maze[0]) else None
        if (col and next_col):
            valid, smudge = is_valid(col, next_col, smudge)
            if valid:
                valid, smudge = is_mirror_col(maze, j, smudge)
                if valid and smudge == 0:
                    continue
                elif valid:
                    return j + 1

def is_valid(compare, compare2, smudge):
    for i in range(0, len(compare)):
        if compare[i] != compare2[i]:
            smudge += 1
            if smudge > 1:
                return False, smudge
    return True, smudge

def is_mirror_col(maze, j, smudge):
    r_x = j
    for x in range(j, len(maze[0])):
        if r_x < 0:
            return (True, smudge)

        compare_L = ''.join([maze[i][r_x - 1] for i in range(len(maze))]) if r_x - 1 >= 0 else None
        compare_R = ''.join([maze[i][x + 2] for i in range(len(maze))]) if x + 2 < len(maze[0]) else None
        
        if (compare_L and compare_R):
            valid, smudge = is_valid(compare_L, compare_R, smudge)
            if not valid:
                return (False, smudge)

        r_x -= 1
    return (True, smudge)

def is_mirror_row(maze, i, smudge):
    r_x = i
    for x in range(i, len(maze)):
        if r_x < 0:
            return (True, smudge)

        compare_L = maze[r_x - 1] if r_x - 1 >= 0 else None
        compare_R = maze[x + 2] if x + 2 < len(maze) else None

        if (compare_L and compare_R):
            valid, smudge = is_valid(compare_L, compare_R, smudge)
            if not valid:
                return (False, smudge)

        r_x -= 1
    return (True, smudge)

readfile('example.txt')
readfile('input.txt')
