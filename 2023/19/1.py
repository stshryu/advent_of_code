# Day nineteen can be found here: https://adventofcode.com/2023/day/19

import pdb

def readfile(filename):
    with open(filename) as f:
        workflow, parts = [i.split("\n") for i in f.read().strip().split("\n\n")]
    workflow_dict = create_workflow(workflow)
    parts_list = create_parts(parts)
    #accepted_sum = run_workflow(workflow_dict, parts_list)
    print(f"{accepted_sum=}")
    initial_state = ('in', {c: (1, 4000) for c in 'xmas'})
    trace_paths(workflow_dict, initial_state)

def run_workflow(workflow_dict, parts_list):
    accepted_parts = [] 
    for i in range(len(parts_list)):
        current_key = "in"
        while(True):
            if current_key == 'A':
                accepted_parts.append(parts_list[i])
                break
            elif current_key == 'R':
                break
            current = workflow_dict[current_key]
            for j in range(len(current)):
                if j == len(current) - 1:
                    current_key = current[j]
                    break
                partkey = current[j][0:1]
                operator = current[j][1:2]
                compare, dest = current[j][2:].split(":")
                partvalue = parts_list[i][partkey]
                if operator == '<':
                    if partvalue < int(compare):
                        current_key = dest
                        break
                    else:
                        continue
                elif operator == '>':
                    if partvalue > int(compare):
                        current_key = dest
                        break
                    else:
                        continue
    return sum([sum(parts.values()) for parts in accepted_parts])

def create_workflow(workflow):
    workflow_dict = {}
    for i in range(len(workflow)):
        key, value = workflow[i].split("{")
        value = value[:-1].split(",")
        workflow_dict[key] = value
    return workflow_dict

def create_parts(parts):
    parts_list = []
    for i in range(len(parts)):
        parts_list.append({ kv.split("=")[0]: int(kv.split("=")[1]) for kv in parts[i][1:-1].split(",") })
    return parts_list

def add_constraint(constraints, condition):
    key, op, val = condition
    lo, hi = constraints.get(key, (1, 4000))
    if op == '>':
        if val >= hi:
            return None
        lo = val + 1
    else:
        if val <= lo:
            return None
        hi = val - 1
    return dict(constraints, **{key: (lo, hi)})

def invert(condition):
    key, op, val = condition
    return (key, '>', val - 1) if (op == '<') else (key, '<', val + 1)

def trace_paths(workflows, state):
    pdb.set_trace()
    workflow_name, constraints = state

def main():
    readfile('example')
    readfile('input')

if __name__ in '__main__':
    main()
