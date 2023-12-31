# Day sixteen can be found here: https://adventofcode.com/2023/day/16

import pdb
from pprint import pprint

def readfile(filename):
    with open(filename) as f:
        contraption = f.read().strip().replace("\\", "Y").split("\n") # replace escaped \\ with the char Y because I'm lazy

    # Part One 
    total_energy = len(beam(contraption))
    print(f"Total tiles energized for {filename} is: {total_energy}")

    # Part Two
    left = [((i, 0), 'R') for i in range(len(contraption))]
    right = [((i, len(contraption[0]) - 1), 'L') for i in range(len(contraption))]
    bottom = [((0, i), 'D') for i in range(len(contraption[0]))]
    top = [((len(contraption) - 1, i), 'U') for i in range(len(contraption[0]))]
    highest_energy = 0
    for start in left + right + bottom + top:
        energy = len(beam(contraption, start[0], start[1]))
        highest_energy = energy if highest_energy < energy else highest_energy
    print(f"Highest energy total for {filename} is: {highest_energy}")

def beam(contraption, start_loc=(0,0), initial_move='R'):
    move = { 'R': (0, 1), 'L': (0, -1), 'U': (-1, 0), 'D': (1, 0) }
    outcomes = { 
                'D' : { '|': ['D'], '-': ['L', 'R'], '/': ['L'], 'Y': ['R'] },
                'R' : { '|': ['U', 'D'], '-': ['R'], '/': ['U'], 'Y': ['D'] },
                'L' : { '|': ['U', 'D'], '-': ['L'], '/': ['D'], 'Y': ['U'] },
                'U' : { '|': ['U'], '-': ['L', 'R'], '/': ['R'], 'Y': ['L'] }}

    visited_beam = {*()} 
    beams = [(start_loc, initial_move)]
    while(len(beams) > 0):
        for beam in beams:
            current_beam = beam[0]
            cardinal = beam[1]
            beam_key = (tuple(current_beam), cardinal)
            if beam_key in visited_beam:
                beams.remove(beam)
                break
            visited_beam.add(beam_key)
            current_loc = contraption[current_beam[0]][current_beam[1]]
            if current_loc in outcomes[cardinal]:
                new_beam = outcomes[cardinal][current_loc]
                for _beam in new_beam:
                    destination_beam = (current_beam[0] + move[_beam][0], current_beam[1] + move[_beam][1])
                    if destination_beam[0] < 0 or destination_beam[1] < 0 or destination_beam[0] >= len(contraption) or destination_beam[1] >= len(contraption[0]):
                        pass
                    else:
                        if (destination_beam, _beam) not in beams:
                            beams.append((destination_beam, _beam))
            else:
                destination_beam = (current_beam[0] + move[cardinal][0], current_beam[1] + move[cardinal][1])
                if destination_beam[0] < 0 or destination_beam[1] < 0 or destination_beam[0] >= len(contraption) or destination_beam[1] >= len(contraption[0]):
                    pass
                else:
                    if (destination_beam, cardinal) not in beams:
                        beams.append((destination_beam, cardinal))
            beams.remove(beam)

    visited_coords = {i[0] for i in visited_beam}
    return(visited_coords)

readfile('example.txt')

import cProfile
from pstats import Stats

with cProfile.Profile() as pr:
    readfile('input.txt')
    stats = Stats(pr)
    stats.sort_stats('cumtime').print_stats(5)
