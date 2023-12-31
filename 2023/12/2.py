# Day twelve can be found here: https://adventofcode.com/2023/day/12

import pdb, cProfile

def readfile(filename):
    total_sum = 0

    with open(filename) as f:
        for line in f:
            springs, records = line.strip().split(" ")
            springs = '?'.join([x for x in [springs] * 5])
            records = [int(x) for x in records.split(",")]
            records = records * 5
            total_sum += get_combinations(springs, records, 0, 0, 0, {})

    print(f"Total sum of outcomes for {filename} is: {total_sum}")

def get_combinations(springs, records, si, ri, counter, master):
    # Currently visited outcomes (since our lines continually repeat) can be expressed as current spring, current record, and current counter.
    # This is a dynamic programming approach to the solution to save the state once we've found it to help us continue calculating down the line.
    # Thanks to Gavin for spoiling this part of the problem, thanks Gavin. Initially struggled with the state and how to recall it, ended up 
    # taking inspiration from https://github.com/jonathanpaulson/AdventOfCode/blob/master/2023/12.py. This method works for P1 as well, which
    # is much cleaner than the brute force method.
    key = (si, ri, counter)
    if key in master:
        return master[key]

    if si == len(springs):
        # If we reach the end of our springs and we're out of records and we're not iterating a counter
        if ri == len(records) and counter == 0:
            return 1
        # If we reach the end of our springs and we're on the last record with a counter equal to that record
        elif ri == len(records) - 1 and records[ri] == counter:
            return 1
        return 0

    total = 0
    # If a '?' exists we can either be a '#' or a '.' so run the outcomes for both, otherwise just run the outome for whatever the current spring is
    results = ['.', '#'] if springs[si] == '?' else springs[si]
    for result in results:
        # If our previous value was a '.' (counter = 0) increment our springs while staying on the same block
        if result == '.' and counter == 0:
            total += get_combinations(springs, records, si + 1, ri, 0, master)
        # If we started counting, and are ending a counter with a '.' where our current record matches a counter increment our springs AND record and reset counter 
        elif result == '.' and counter > 0 and len(records) > ri and records[ri] == counter:
            total += get_combinations(springs, records, si + 1, ri + 1, 0, master)
        # If we have either start, or continue a '#' section increment our springs and increase counter by one
        elif result == '#':
            total += get_combinations(springs, records, si + 1, ri, counter + 1, master)

    master[key] = total
    return total

readfile('example.txt')
readfile('input.txt')
