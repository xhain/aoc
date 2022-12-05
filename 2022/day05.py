# -*- coding: utf-8 -*-

def load_data(path):
    return list( open(path, "r") )

# Day 5 / Part 1
data = load_data("data/day05.txt")


# get stack data from file
initial_stack = data[:8]
stacks = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
for line in initial_stack:
    idx, stack_id = 0, 0
    line = line.strip('\n')
    for char in line:
        if idx%4 == 1:
            stack_id = stack_id%9
            if char != " ":
                stacks[stack_id+1].append(char)
            stack_id += 1
        idx += 1

# correct order in stacks
for idx in range(len(stacks)):
    stacks[idx+1].reverse()

# run commands
for line in data[10:]:
    _, num, _, origin, _, destination = line.strip('\n').split(' ')
    for i in range(int(num)):
        stacks[int(destination)].append(stacks[int(origin)].pop())

print(">> Day 4 / Part 1 Solution: ")
for stack in stacks:
    print(stacks[stack].pop())



# Day 5 / Part 2
result = 0

print(f">> Day 4 / Part 2 Solution: {result}")
