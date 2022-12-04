# -*- coding: utf-8 -*-

def load_data(path):
    return list( open(path, "r") )

# Day 4 / Part 1
data = load_data("data/day04.txt")

result = 0
for line in data:
    a, b = line.split(',')
    a1, a2 = map(int, a.split('-'))
    b1, b2 = map(int, b.split('-'))
    if (a1 >= b1) and (a2 <= b2):
        result += 1
    elif (a1 <= b1) and (a2 >= b2):
        result += 1

print(f">> Day 4 / Part 1 Solution: {result}")


# Day 4 / Part 2
result = 0

print(f">> Day 4 / Part 2 Solution: {result}")
