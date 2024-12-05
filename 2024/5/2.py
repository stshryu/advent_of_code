def readfile(filename):
    with open(filename) as f:
        lines = [i for i in f.read().strip().split("\n")]
    for i in range(len(lines)):
        if not lines[i]:
            _rules = lines[:i+1][:-1]
            _out = lines[i:][1:]
    t1 = 0
    t2 = 0
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
        temp = []
        h = len(inst)//2
        for x in inst:
            if x in rules:
                temp.append((len(set(inst) & rules[x]), x))
            else:
                temp.append((0, x))
        if temp == sorted(temp, key=lambda x: x[0], reverse=True):
            t1 += temp[h][1]
        else:
            for i in temp:
                if i[0] == h:
                    t2 += i[1] print(f"{t1=}")
    print(f"{t2=}")

def main():
    readfile("example.txt")
    readfile("input.txt")

if __name__ in "__main__":
    main()
