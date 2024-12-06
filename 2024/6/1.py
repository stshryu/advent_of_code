def readfile(filename):
    with open(filename) as f:
        lines = [i for i in f.read().strip().split("\n")]
    start = (-1, -1)
    for i in range(len(lines[0])):
        if "^" in lines[i]: start = (lines[i].index("^"), i)
    t = find_path(lines, start, len(lines[0]), len(lines))
    print(f"{t=}")

def find_path(layout, start, xmax, ymax):
    directions = [(0,-1),(1,0),(0,1),(-1,0)]
    dir_index = 0
    search_direction = directions[dir_index]
    visited_locations = {start}
    cursor = start 
    while(True):
        next_step = (cursor[0] + search_direction[0], cursor[1] + search_direction[1])
        if xmax > next_step[0] >= 0 and ymax > next_step[1] >= 0:
            if layout[next_step[1]][next_step[0]] == "#":
                dir_index = dir_index + 1 if dir_index < 3 else 0
                search_direction = directions[dir_index]
            else:
                cursor = next_step
                visited_locations.add(cursor) 
        else: 
            break
    return len(visited_locations)

def main():
    readfile("example.txt")
    readfile("input.txt")

if __name__ in "__main__":
    main()
