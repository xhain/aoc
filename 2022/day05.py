# -*- coding: utf-8 -*-

def load_data(path):
    return list( open(path, "r") )

# Day 5 / Part 1
data = load_data("data/day05.txt")


# get initial stack data from file
stacks = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
for line in data[:8]:
    idx, stack_id = 0, 0
    line = line.strip('\n')
    for char in line:
        if idx%4 == 1:
            stack_id = stack_id%9
            if char != " ":
                stacks[stack_id + 1].append(char)
            stack_id += 1
        idx += 1

# correct order in stacks
for idx in range(len(stacks)):
    stacks[idx + 1].reverse()

# save an original copy
from copy import deepcopy
init_stacks = deepcopy(stacks)

# run commands
for line in data[10:]:
    _, num, _, origin, _, destination = line.strip('\n').split(' ')
    for i in range(int(num)):
        stacks[int(destination)].append(stacks[int(origin)].pop())

# print solution (top item on each stack)
print(">> Day 4 / Part 1 Solution: ")
for stack in stacks:
    print(stacks[stack].pop())


# Day 5 / Part 2
stacks = deepcopy(init_stacks)
for line in data[10:]:
    _, num, _, origin, _, destination = line.strip('\n').split(' ')
    stacks[int(destination)].extend(stacks[int(origin)][-int(num):])
    stacks[int(origin)] = stacks[int(origin)][:-int(num)]

print(">> Day 4 / Part 2 Solution: ")
for stack in stacks:
    print(stacks[stack].pop())
