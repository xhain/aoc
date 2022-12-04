# -*- coding: utf-8 -*-

def load_data(path):
    return list( open(path, "r") )

# Day 2 / Part 1
data = load_data("data/day03.txt")

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = 0
for line in data:
    C1, C2 = set(line[:len(line)//2]), set(line[len(line)//2:])
    equal_char = list(C1.intersection(C2))[0]
    result += chars.index(equal_char) + 1

print(f">> Day 1 / Part 1 Solution: {result}")


# Day 2 / Part 2
result = 0
groupsize = 3
for idx in range(0, len(data), groupsize):
    group = [set(line.strip('\n')) for line in data[idx:idx+groupsize]]
    common_item = group[0] & group[1] & group[2]
    result += chars.index(list(common_item)[0]) + 1

print(f">> Day 1 / Part 2 Solution: {result}")
