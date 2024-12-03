def readfile(filename):
    with open(filename) as f:
        lines = [i for i in f.read().strip().split("\n")]
    t = 0
    for i in lines:
        t += parse(i)
    print(f"{t=}")
        
def parse(i):
    t = 0
    for x in range(len(i)):
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

def main():
    readfile("example.txt")
    readfile("input.txt")

if __name__ in "__main__":
    main()
