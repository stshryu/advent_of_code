# Day seven can be found here: https://adventofcode.com/2023/day/7

import pdb, cProfile

def readfile(filename):
    # index higher = more power
    overall_hand_power = {} 

    with open(filename) as f:
        for line in f:
            hand, bid = line.split() 
            power = get_hand_power(hand)
            overall_hand_power = sorting_hat_powers(power, hand, bid, overall_hand_power)

    rank = 1
    total_winnings = 0
    for key in sorted(list(overall_hand_power.keys())):
        for hand in overall_hand_power[key]:
            total_winnings += rank * hand[1]
            rank += 1

    print(f"Total winnings for {filename} is: {total_winnings}")

def get_hand_power(hand):
    unique = {}

    for c in hand:
        if c in unique:
            unique[c] += 1
        else:
            unique[c] = 1

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

def sorting_hat_powers(power, hand, bid, overall_hand_power):
    bid = int(bid)

    if power in overall_hand_power:
        overall_hand_power[power] = rank_hands(hand, bid, overall_hand_power[power])
    else:
        overall_hand_power[power] = [(hand, bid)]
    return overall_hand_power

def rank_hands(hand, bid, sorted_hands): 
    card_power = "23456789TJQKA"
    
    if len(sorted_hands) == 0:
        sorted_hands.append((hand, bid))
        return sorted_hands
    
    for j in range(0, len(sorted_hands)):
        for i in range(0,5):
            if card_power.index(sorted_hands[j][0][i]) > card_power.index(hand[i]):
                sorted_hands.insert(j, (hand, bid))
                return sorted_hands
            elif card_power.index(sorted_hands[j][0][i]) < card_power.index(hand[i]):
                break

    sorted_hands.append((hand, bid))
    return sorted_hands

readfile('example.txt')
readfile('input.txt')
