# Day eighteen can be found here: https://adventofcode.com/2023/day/18

import pdb

def readfile(filename):
    with open(filename) as f:
        plans = [[int(i) if index == 1 else i for index, i in enumerate(line.split(" "))] for line in f.read().strip().split("\n")]

    corners = [(0,0)]
    for i in range(len(plans)):
        #corners += dig(*plans[i], corners.pop())
        corners += dig(*plans[i], corners.pop(), True)

    area = shoelacepick(corners, plans)

    print(f"{area=}")

def dig(direction, distance, rgb, start_coord, isrgb=False):
    end = [None, None]
    directions = { 'R': (1, 1), 'L': (1, -1), 'D': (0, 1), 'U': (0, -1) } 
    if isrgb:
        direction, distance = getrgb(rgb[2:-1])
    index = directions[direction][0]
    invindex = 0 if index == 1 else 1
    end[index] = start_coord[index] + directions[direction][1] * distance
    end[invindex] = start_coord[invindex]
    return [start_coord, tuple(end)]

def getrgb(rgb, isperi=False):
    directionshex = { '0': 'R', '1': 'D', '2': 'L', '3': 'U' }
    direction = directionshex[rgb[-1]]
    distance = int(rgb[:-1], 16)
    return distance if isperi else (direction, distance)

def shoelacepick(corners, plans):
    y, x = zip(*corners)
    #peri = sum([plans[i][1] for i in range(len(plans))]) # part 1
    _, _, rgbdist = zip(*plans)
    peri = sum([getrgb(i[2:-1], True) for i in rgbdist])
    area = abs(sum(i * j for i, j in zip(x, y[1:] + y[:1])) - sum(i * j for i, j in zip(x[1:] + x[:1], y ))) / 2
    return area + 1 - (peri/2) + peri

def main():
    readfile('example.txt')
    readfile('input.txt')

if __name__ in '__main__':
    main()
