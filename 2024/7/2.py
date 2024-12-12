def readfile(filename):
    with open(filename) as f:
        lines = [(
            int(i.split(":")[0].strip()), 
            [int(x) for x in i.split(":")[1].strip().split()]) 
            for i in f.read().strip().split("\n")
        ]
    t = 0
    for i in lines:
        if isvalid(i): t += i[0]
    print(f"{t=}")

def isvalid(inputs):
    test_val, operands = inputs
    outcomes = {
        operands[0] + operands[1], 
        operands[0] * operands[1],
        concats(operands[0], operands[1])
    }
    for i in range(2, len(operands)):
        new_outcomes = set() 
        for left_operand in outcomes:
            right_operand = operands[i]
            new_outcomes.add(left_operand + right_operand)
            new_outcomes.add(left_operand * right_operand)
            new_outcomes.add(concats(left_operand, right_operand))
        outcomes = new_outcomes 
    return True if test_val in outcomes else False

def concats(left, right):
    return int(str(left) + str(right))

def main():
    readfile("example.txt")
    readfile("input.txt")

if __name__ in "__main__":
    main()
