# Day seventeen can be found here: https://adventofcode.com/2023/day/17

import pdb, heapq

def readfile(filename):
    with open(filename) as f:
         city = [[int(i) for i in line] for line in f.read().strip().split('\n')]
    lowest_heat = cruciblerun(city)

    print(f"{filename} {lowest_heat=}")

def cruciblerun(city):
    moves = [(-1,0),(0,1),(1,0),(0,-1)]
    invalid = [(1,0),(0,-1),(-1,0),(0,1)]

    queue = [(0, 0, 0, -1)]
    seenblock = {*()}
    while queue:
        heat, y, x, last_move = heapq.heappop(queue)
        if y == len(city) - 1 and x == len(city[0]) - 1:
            return heat 
        if (y, x, last_move) in seenblock:
            continue
        seenblock.add((y, x, last_move))
        for move in range(4):
            heatcost = 0
            m_curr = moves[move]
            m_index = invalid.index(m_curr)
            if move == last_move or last_move == m_index:
                pass
            else:
                for i in range(1, 11): # change to range(1, 4) for part 1
                    new_y = y + moves[move][0] * i
                    new_x = x + moves[move][1] * i
                    if new_y in range(len(city)) and new_x in range(len(city[0])):
                        if i < 4: # remove this block for part 1
                            heatcost += city[new_y][new_x]
                        else:
                            heatcost += city[new_y][new_x]
                            new_heat = heat + heatcost
                            heapq.heappush(queue, (new_heat, new_y, new_x, move))
                        
def main():
    readfile('example.txt')
    readfile('example2.txt')
    readfile('input.txt')

if __name__ in '__main__':
    main()
