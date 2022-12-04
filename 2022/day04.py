# -*- coding: utf-8 -*-

def load_data(path):
    return list( open(path, "r") )

# Day 4 / Part 1
data = load_data("data/day04.txt")

result = 0
for line in data:
    a, b = line.split(',')
    min1, max1 = map(int, a.split('-'))
    min2, max2 = map(int, b.split('-'))
    if (min1 >= min2) and (max1 <= max2):
        result += 1
    elif (min1 <= min2) and (max1 >= max2):
        result += 1

print(f">> Day 4 / Part 1 Solution: {result}")


# Day 4 / Part 2
result = 0
for line in data:
    a, b = line.split(',')
    min1, max1 = map(int, a.split('-'))
    min2, max2 = map(int, b.split('-'))
    if min2 <= max1 and min1 <= max2:
        result += 1

print(f">> Day 4 / Part 2 Solution: {result}")
