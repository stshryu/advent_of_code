import pdb 

def readfile(filename):
    a = [[] for _ in range(2)]
    with open(filename) as f:
        for line in f.read().strip().split("\n"):
            left_in, right_in = line.split("   ")
            a[0].append(int(left_in))
            a[1].append(int(right_in))
    for i in a:
        i.sort()
    t = 0
    for i in range(0, len(a[0])):
        t += abs(a[0][i] - a[1][i])
    print(f"{t=}")

def main():
    readfile("example.txt")
    readfile("input.txt")

if __name__ in "__main__":
    main()
