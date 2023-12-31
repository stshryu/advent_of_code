# Day four can be found here: https://adventofcode.com/2023/day/4

import pdb

def parseline(line):
    card, win_and_pulls = line.rstrip().split(":")
    card_id = card.split()[-1]
    winning_numbers, pulled_numbers = win_and_pulls.split("|")

    win_num = [x for x in winning_numbers.split() if x]
    pull_num = [x for x in pulled_numbers.split() if x] 

    return sum_winnings(win_num, pull_num)

# You could use set intersection() to find common elements, but there's no guarantee that the pulled numbers is unique per value added
# since uniqueness is not guaranteed, we will use dictionaries instead to sum our count.
def sum_winnings(win_num, pull_num):
    count = 0
    win_key = {}
    for num in win_num:
        win_key[num] = 0

    for num in pull_num:
        if num in win_key:
            count += 1

    if not count:
        return 0

    total_sum = 1
    for i in range(1,count):
        total_sum *= 2
    
    return total_sum

def readfile(filename):
    total_sum = 0

    with open(filename) as f:
        for line in f:
            total_sum += parseline(line)

    print(f"Total sum for {filename} is: {total_sum}")

readfile('example.txt')
readfile('input.txt')
