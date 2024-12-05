def readfile(filename):
    with open(filename) as f:
        lines = [i for i in f.read().strip().split("\n")]
    for i in range(len(lines)):
        if not lines[i]:
            _rules = lines[:i+1][:-1]
            _out = lines[i:][1:]
    t = 0
    rules = {}
    for i in _rules:
        l, r = [int(i) for i in i.split("|")]
        if l not in rules:
            rules[l] = {r}
        else:
            rules[l].add(r)
    valid = True
    for i in _out:
        inst = [int(i) for i in i.split(",")]
        for x in range(len(inst)):
            check = set(inst[:x])
            if inst[x] in rules:
                if rules[inst[x]] & check:
                    valid = False
        if valid:
            t += inst[len(inst)//2]
        valid = True
    print(f"{t=}")

def main():
    readfile("example.txt")
    readfile("input.txt")

if __name__ in "__main__":
    main()
