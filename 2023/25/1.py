# Day twenty-five can be found here: https://adventofcode.com/2023/day/25

import pdb 
from pprint import pprint

def readfile(filename):
    with open(filename) as f:
        connections = f.read().strip().split("\n")

    pdb.set_trace()

def main():
    readfile('example.txt')
    readfile('input.txt')

if __name__ in '__main__':
    main()
