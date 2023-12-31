# Day two can be found here: https://adventofcode.com/2023/day/2

import pdb

def partone(line):
    game_id, result = parse_line(line)
    return game_id if result else None

def parse_line(line):
    # Can potentially use regex '\d+' to find all the digits, but since we know the string format, why bother
    preprocessing_line = line.split(":")
    game_id = int(preprocessing_line[0].replace("Game ", ""))

    # Multiple line delineations based on our string format, first with ";" then second with ",", once we have
    # each individual game, stript the whitelines and format the string like "{num} {color}" for easier parsing
    games = preprocessing_line[1].split(";")
    for game in games:
        res = { "red": 0, "blue": 0, "green": 0 }
        outcomes = [s.strip() for s in game.split(',')]
        for outcome in outcomes:
            num, color = outcome.split(" ")
            res[color] += int(num)

        if not is_valid_game(res):
            return game_id, False

    return game_id, True
    
def is_valid_game(res):
    valid_game = { "red": 12, "blue": 14, "green": 13 }
    for key in list(valid_game.keys()):
        if valid_game[key] <  res[key]:
            return False
    return True

def parse_line_parttwo(line):
    preprocessing_line = line.split(":")
    games = preprocessing_line[1].split(";")

    # Only thing we care about is the minimum valid cube configuration for each game in our overall games so the 
    # dictionary comes out and we compare to ensure only the largest value for each valid configuration is saved
    res = { "red": 0, "blue": 0, "green": 0 }
    for game in games:
        outcomes = [s.strip() for s in game.split(',')]
        for outcome in outcomes:
            num, color = outcome.split(" ")
            num = int(num)
            res[color] = num if num > res[color] else res[color]

    total_power = 1
    for key in list(res.keys()):
        total_power *= res[key]

    return total_power
    
def read_and_parse(filename):
    total_sum = 0

    with open(filename) as f:
        for line in f:
            result = partone(line)
            total_sum = (total_sum + result) if result else total_sum

    print(f"Total sum of game ids for part one: {total_sum}")

def read_and_parse_parttwo(filename):
    total_power = 0

    with open(filename) as f:
        for line in f:
            result = parse_line_parttwo(line)
            total_power += result

    print(f"Total sum of each game power is: {total_power}")

read_and_parse("example.txt")
read_and_parse("input.txt")

read_and_parse_parttwo("example2.txt")
read_and_parse_parttwo("input.txt")
