def readfile(filename):
    with open(filename) as f:
        lines = [i for i in f.read().strip().split("\n")]
    _lines = ''.join(lines)
    t = parse(_lines, toggle(_lines))
    print(f"{t=}")
        
def parse(i, vrange):
    v = True
    cursor = 0
    flip_index = vrange[cursor]
    t = 0
    for x in range(len(i)):
        if x == flip_index:
            v = not v
            cursor += 1
            if cursor < len(vrange): 
                flip_index = vrange[cursor]
            else:
                flip_index = len(i)
        if v:
            temp = i[x:x+4]
            y = x + 5 
            if temp == 'mul(':
                while(True):
                    if y >= len(i):
                        y -= 1
                        break
                    if i[y] == ')':
                        y += 1
                        break
                    y += 1
                if y == -1: break
                check = i[x+4:y-1]
                if "," not in check: continue
                l, r = check.split(",", 1)
                if l.isnumeric() and r.isnumeric():
                    t += int(l) * int(r)
    return t

def toggle(i):
    status = True 
    vrange = []
    x = 0
    while(True):
        x = i.find('don\'t()', x) if status else i.find('do()', x)
        if x == -1: break
        x += 6 if status else 4
        vrange.append(x)
        status = not status
    return vrange

def main():
    #readfile("example.txt")
    readfile("example2.txt")
    readfile("input.txt")

if __name__ in "__main__":
    main()
