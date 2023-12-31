# Day twelve can be found here: https://adventofcode.com/2023/day/12

import pdb, cProfile

def readfile(filename):
    total_sum = 0

    with open(filename) as f:
        for line in f:
            springs, records = line.strip().split(" ")
            records = [int(x) for x in records.split(",")]
            total_sum += get_combinations(springs, records, 0)

    print(f"Total sum of outcomes for {filename} is: {total_sum}")

def valid(springs, records):
    current = 0
    seen = []
    for c in springs:
        if c == '.':
            if current > 0:
                seen.append(current)
            current = 0
        elif c == '#':
            current += 1
        else:
            return False
    if current > 0:
        seen.append(current)
    return seen == records 

def get_combinations(springs, records, counter):
    if counter == len(springs):
        return 1 if valid(springs, records) else 0
    if springs[counter] == '?':
        return (get_combinations(springs[:counter] + '#' + springs[counter+1:], records, counter + 1) + get_combinations(springs[:counter] + '.' + springs[counter + 1:], records, counter + 1))
    else:
        return get_combinations(springs, records, counter + 1)

readfile('example.txt')
readfile('input.txt')
