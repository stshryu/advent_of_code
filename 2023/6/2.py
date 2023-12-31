# Day six can be found here: https://adventofcode.com/2023/day/6

import pdb, cProfile

def readandparse(filename):
    with open(filename) as f:
        file = f.read()        

    times, dists = [line.split()[1:] for line in file.split("\n")[:-1]]
    time = [''.join([item for item in times])]
    dist = [''.join([item for item in dists])]
    outcome_pow = calculate_outcomes(time, dist)

    print(f"Power of outcomes for {filename} is: {outcome_pow}")

def calculate_outcomes(times, dists):
    outcome_pow = 1
    for i in range(len(times)):
        time = int(times[i])
        dist = int(dists[i])
        
        outcome_pow *= get_min_max_channel(time, dist)

    return outcome_pow

# The formula for distance as a method of channel time is:
#
# dist = channel * (time - channel)
# 
# using that you can find the first egress into distance which should allow you to 
# find the other egress point. It's easy to visualize if you imagine the formula 
# in a graph as y = x * (const - x) which is an inverse parabola. You can imagine
# the egress points for distance as a constant y = dist_to_beat. A straight line
# through a parabola has 2 points, all distinct values between those two points 
# should constitute a valid winning time.
# 
# Keep in mind that if you actually just solved the equation for the given distance
# you need to beat you can do this in O(1) time, BUT requires you to import the math
# library in order to achieve this. This is a purely base python implementation.
def get_min_max_channel(time, dist):
    for i in range(0, time+1):
        tot_dist = i * (time - i)
        if tot_dist > dist:
            return len(range(i,time-i+1))

readandparse('example.txt')
readandparse('input.txt')
