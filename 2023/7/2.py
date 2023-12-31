# Day seven can be found here: https://adventofcode.com/2023/day/7

import pdb, cProfile

def readfile(filename):
    card_power = 'J23456789TQKA'
    # index higher = more power
    overall_hand_power = {} 

    with open(filename) as f:
        for line in f:
            hand, bid = line.split() 
            power = get_hand_power(hand, card_power)
            overall_hand_power = sorting_hat_powers(power, hand, bid, overall_hand_power, card_power)

    rank = 1
    total_winnings = 0
    for key in sorted(list(overall_hand_power.keys())):
        for hand in overall_hand_power[key]:
            total_winnings += rank * hand[1]
            rank += 1
            
    print(f"Total winnings for {filename} is: {total_winnings}")

def get_hand_power(hand, card_power):
    unique = {}

    for c in hand:
        if c in unique:
            unique[c] += 1
        else:
            unique[c] = 1

    # create a new dictionary with all of our unique values and check to see if a Joker exists
    sorted_unique = {key: value for key, value in sorted(unique.items(), key=lambda x: x[1], reverse=True)}
    # if a joker exists replace our unique hand with the strongest possible hand with a wildcard joker
    if 'J' in sorted_unique:
        unique = replace_joker(sorted_unique, card_power)

    # get the hand power higher number = more power
    match len(unique.keys()):
        case 5: # high card
            return 1
        case 4: # one pair
            return 2
        case 3: # three of a kind or two pair
            return 4 if any(value == 3 for value in unique.values()) else 3
        case 2: # four of a kind or full house 
            return 6 if any(value == 4 for value in unique.values()) else 5
        case 1: # five of a kind
            return 7

def replace_joker(sorted_unique, card_power):
    jokers = sorted_unique.pop('J')
    # edge case for all 5 jokers (best hand is always AAAAA)
    if jokers == 5:
        sorted_unique['A'] = 5

    # if all cards have the same count, find the strongest card
    if len(list(set(list(sorted_unique.values())))) == 1:
        strongest_card = card_power[[card for card in sorted(card_power.index(key) for key in sorted_unique.keys())][-1]]
    # if there is a maximum value
    else:
        strongest_card = max(sorted_unique, key=lambda x: sorted_unique[x])

    sorted_unique[strongest_card] += jokers
    return sorted_unique
    
def sorting_hat_powers(power, hand, bid, overall_hand_power, card_power):
    bid = int(bid)

    if power in overall_hand_power:
        overall_hand_power[power] = rank_hands(hand, bid, overall_hand_power[power], card_power)
    else:
        overall_hand_power[power] = [(hand, bid)]
    return overall_hand_power

def rank_hands(hand, bid, sorted_hands, card_power): 
    # if there are no hands in our sorted_hands, we add our current hand into it
    if len(sorted_hands) == 0:
        sorted_hands.append((hand, bid))
        return sorted_hands
    
    for j in range(0, len(sorted_hands)):
        for i in range(0,5):
            # if our current card is beat by the card in the compared hand index insert our hand before the index
            if card_power.index(sorted_hands[j][0][i]) > card_power.index(hand[i]):
                sorted_hands.insert(j, (hand, bid))
                return sorted_hands
            # if our current card is beats the card in the compared hand index, break the loop and find the next hand 
            elif card_power.index(sorted_hands[j][0][i]) < card_power.index(hand[i]):
                # this break ensures that we only increment through each card in a hand if the cards are equal
                break

    # if at the end of the comparison no other hands beat our hand, add it to the end of our sorted_hands
    sorted_hands.append((hand, bid))
    return sorted_hands

with cProfile.Profile() as pr:
    readfile('example.txt')
    pr.print_stats()

with cProfile.Profile() as pr:
    readfile('input.txt')
    pr.print_stats()

with cProfile.Profile() as pr:
    readfile('gavininput.txt')
    pr.print_stats()
