def readfile(filename):
    with open(filename) as f:
        lines = [i for i in f.read().strip().split("\n")]
    t = 0
    xmax = len(lines[0])
    ymax = len(lines)
    _dir = [[-1,1],[1,-1]]
    _dir2 = [[-1,-1],[1,1]]
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == 'A':
                r = False
                l = False
                temp = []
                for a in _dir:
                    _x, _y = x, y
                    dx, dy = a
                    _x += dx
                    _y += dy
                    if 0 <= _x < xmax and 0 <= _y < ymax:
                        temp.append(lines[_y][_x])
                    if temp == ['M','S'] or temp == ['S','M']:
                        r = True
                temp = []
                for a in _dir2:
                    _x, _y = x, y
                    dx, dy = a
                    _x += dx
                    _y += dy
                    if 0 <= _x < xmax and 0 <= _y < ymax:
                        temp.append(lines[_y][_x])
                    if temp == ['M','S'] or temp == ['S','M']:
                        l = True
                if l and r:
                    t += 1

    print(f"{t=}")

def main():
    readfile("example.txt")
    readfile("input.txt")

if __name__ in "__main__":
    main()
