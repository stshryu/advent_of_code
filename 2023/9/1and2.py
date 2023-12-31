# Day[9] can be found here: https://adventofcode.com/2023/day/9

import pdb, cProfile

def parsefile(filename):
    total_sum = 0
    
    file = []
    with open(filename) as f:
        for line in f:
            file.append([int(val) for val in line.rstrip().split(" ")])

    for nums in file:
        # total_sum += extrapolate(nums) # This is part 1 solution
        total_sum += extrapolate(nums[::-1]) # This is part 2 solution

    print(f"Total sum for {filename} is: {total_sum}")

def extrapolate(nums):
    diffs = [nums[i+1] - nums[i] for i in range(len(nums) - 1)]
    return nums[-1] + (extrapolate(diffs) if any(diffs) else 0)

parsefile('example.txt')
parsefile('input.txt')
