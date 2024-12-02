def readfile(filename):
    import pdb
    with open(filename) as f:
        lines = [list(map(int, i.split())) for i in f.read().strip().split("\n")]

    t = 0
    for level in lines:
        _aord, arindex = aord(level)
        _validl, vrindex = validl(level)
        if _aord and _validl:
            if arindex and vrindex:
                common = set(arindex) & set(vrindex)
                if common:
                    for i in common:
                        temp = level[:i] + level[i+1:]
                        a, _ = aord(temp, 1)
                        b, _ = validl(temp, 1)
                        if a and b:
                            t += 1
                            break
            elif arindex and not vrindex:
                for i in arindex:
                    temp = level[:i] + level[i+1:]
                    a, _ = aord(temp, 1)
                    b, _ = validl(temp, 1)
                    if a and b:
                        t += 1
                        break
            elif not arindex and vrindex:
                for i in vrindex:
                    temp = level[:i] + level[i+1:]
                    a, _ = aord(temp, 1)
                    b, _ = validl(temp, 1)
                    if a and b:
                        t += 1
                        break
            else:
                t += 1
    print(f"{t=}")
                

def validl(level, r=None):
    prev = level[0]
    for i in range(1, len(level)):
        if prev == level[i] or abs(prev-level[i]) > 3:
            if r: return (False, [])
            temp = []
            res, _ = validl(level[:i] + level[i+1:], 1)
            if res:
                temp.append(i)
            res2, _ = validl(level[:i-1] + level[i:], 1)
            if res2:
                temp.append(i-1)
            return (True, temp) if temp else (False, [])
        prev = level[i]
    return (True, [])

def aord(level, r=None):
    if level == sorted(level):
        return (True, [])
    elif level == sorted(level, reverse=True):
        return (True, [])
    else:
        if r: return (False, [])
        temp = []
        for i in range(len(level)):
            x = level[:i] + level[i+1:]
            if x == sorted(x):
                temp.append(i)
            if x == sorted(x, reverse=True):
                temp.append(i)
        return (True, temp) if temp else (False, [])

def main():
    readfile("example.txt")
    readfile("input.txt")

if __name__ in "__main__":
    main()
