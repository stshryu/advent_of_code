def readfile(filename):
    import pdb
    with open(filename) as f:
        lines = [list(map(int, i.split())) for i in f.read().strip().split("\n")]

    t = 0
    for level in lines:
        if safe(level):
            t += 1
        else:
            for i in range(len(level)):
                x = level[:i] + level[i+1:]
                if safe(x):
                    t += 1
                    break
    print(f"{t=}")

def safe(level):
    safe = True 
    if level == sorted(level):
        asc = True
    elif level == sorted(level, reverse=True):
        asc = False
    else:
        return False
    prev = level[0]
    for i in range(1, len(level)):
        if prev == level[i] or abs(prev - level[i]) > 3:
            safe = False
            break
        prev = level[i]
    return safe

def main():
    readfile("example.txt")
    readfile("input.txt")

if __name__ in "__main__":
    main()
