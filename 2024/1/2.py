def readfile(filename):
    a = [[] for _ in range(2)]
    with open(filename) as f:
        for line in f.read().strip().split("\n"):
            left_in, right_in = line.split("   ")
            a[0].append(int(left_in))
            a[1].append(int(right_in))
    return a

def t_count(a):
    t = 0
    for i in a[0]:
        t += i * a[1].count(i)
    return t

def t_hash(a):
    d = {}
    t = 0
    for i in a[1]:
        d[i] = d[i] + 1 if i in d else 1
    for i in a[0]:
        if i in d: t += (i * d[i])
    return t

def main():
    a = readfile("example.txt")
    b = readfile("input.txt")
    c = readfile("inputjorge.txt")
    print(t_count(b))
    print(t_count(c))

if __name__ in "__main__":
    main()
