# Day four can be found here: https://adventofcode.com/2023/day/4

import pdb, cProfile

# The master dictionary will hold all copies of the card we currently own. If the card doesn't exist (card 1 for example) we will set
# the value to one. If the card already exists (we have already received copies for example, we add one to the existing copies and 
# continue evaluating down the card stack).
def parseline(line, master_dict):
    card, win_and_pulls = line.rstrip().split(":")
    card_id = int(card.split()[-1])
    winning_numbers, pulled_numbers = win_and_pulls.split("|")

    win_num = [x for x in winning_numbers.split() if x]
    pull_num = [x for x in pulled_numbers.split() if x] 

    master_dict[card_id] = 1 if card_id not in master_dict else master_dict[card_id] + 1

    return sum_winnings(win_num, pull_num, master_dict, card_id)

# You could use set intersection() to find common elements, but there's no guarantee that the pulled numbers is unique per value added
# since uniqueness is not guaranteed, we will use dictionaries instead to sum our count. 
def sum_winnings(win_num, pull_num, master_dict, card_id):
    count = 0
    win_key = {}
    for num in win_num:
        win_key[num] = 0

    for num in pull_num:
        if num in win_key:
            count += 1

    if not count:
        return 0

    add_won_cards(count, card_id, master_dict, master_dict[card_id])

    # The old version of code here is left for posterity. This version simply iterates through the add_won_cards() based on the current
    # number of cards you own of id, card_id. This resulted in over 2.8 million function calls to add_won_cards(). By instead multiplying
    # the card number by one and adding that value to the master dictionary we can skip iterations and bring the number of calls to
    # add_won_cards() to 178.
    #
    # Old code is below:
    #
    # for i in range(0, master_dict[card_id]):
    #     add_won_cards(count, card_id, master_dict)
    
def add_won_cards(count, card_id, master_dict, multiplier):
    for i in range(1, count + 1):
        master_dict[card_id + i] = multiplier if card_id + i not in master_dict else master_dict[card_id + i] + multiplier

        # Old code below:
        #
        # master_dict[card_id + i] = 1 if card_id + i not in master_dict else master_dict[card_id + i] + 1

def readfile(filename):
    total_sum = 0
    master_dict = {}

    with open(filename) as f:
        for line in f:
            parseline(line, master_dict)

    for key in list(master_dict.keys()):
        total_sum += master_dict[key]

    print(f"Total sum of cards: {total_sum}")

with cProfile.Profile() as pr:
    readfile('example.txt')
    pr.print_stats()
with cProfile.Profile() as pr:
    readfile('input.txt')
    pr.print_stats()
