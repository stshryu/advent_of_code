def readfile(filename):
    with open(filename) as f:
        lines = [list(i) for i in f.read().strip().split("\n")]
    parse_grid(lines)

def parse_grid(grid: list):
    node_locations = [] 
    for y in range(0, len(grid)):
        for x in range(0, len(grid[0])):
            if grid[y][x] != ".":
                node_locations.append((x, y, grid[y][x])) # (x, y) for readability instead of (y, x)
    find_antinodes(node_locations, grid)

def find_antinodes(node_locations: list, grid: list):
    dimension_x, dimension_y = len(grid[0]), len(grid)
    antinode_locations = set()
    grouped_nodes = {}
    for i in node_locations:
        grouped_nodes.setdefault(i[2], []).append((i[0], i[1]))
    for k, v in grouped_nodes.items():
        for i in range(len(v)):
            unvisited_nodes = v[i+1:]
            for j in unvisited_nodes:
                i_x = v[i][0] 
                i_y = v[i][1] 
                j_x = j[0] 
                j_y = j[1] 
                dist_x = abs(i_x - j_x)
                dist_y = abs(i_y - j_y)
                anode1, anode2 = [0,0], [0,0]
                if i_x < j_x:
                    if i_y < j_y:
                        anode1 = [i_x - dist_x, i_y - dist_y]
                        anode2 = [j_x + dist_x, j_y + dist_y]
                    else:
                        anode1 = [i_x - dist_x, i_y + dist_y]
                        anode2 = [j_x + dist_x, j_y - dist_y]
                else:
                    if i_y < j_y:
                        anode1 = [i_x + dist_x, i_y - dist_y]
                        anode2 = [j_x - dist_x, j_y + dist_y]
                    else:
                        anode1 = [i_x + dist_x, i_y + dist_y]
                        anode2 = [j_x - dist_x, j_y - dist_y]
                if anode1[0] in range(0, dimension_x) and anode1[1] in range(0, dimension_y):
                    grid[anode1[1]][anode1[0]] = "#"
                    antinode_locations.add(tuple(anode1))
                if anode2[0] in range(0, dimension_x) and anode2[1] in range(0, dimension_y):
                    grid[anode2[1]][anode2[0]] = "#"
                    antinode_locations.add(tuple(anode2))
    print(len(antinode_locations))

def main():
    readfile("example.txt")
    readfile("input.txt")

if __name__ in "__main__":
    main()
