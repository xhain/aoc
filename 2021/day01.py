# -*- coding: utf-8 -*-

def load_data(path):
    return list( open(path, "r") )

# Day 1 / Part 1
data = load_data("data/day01.txt")
data = list(map(int, data))

increased1 = 0
for idx in range(len(data)-1):
    if data[idx+1] - data[idx] > 0:
        increased1 += 1
        
print(f">> Day 1 / Part 1 Solution: {increased1}")


# Day 1 / Part 2
increased2 = 0
for idx in range(len(data)-2):
    if sum(data[idx:idx+3]) < sum(data[idx+1:idx+1+3]):
        increased2 += 1

print(f">> Day 1 / Part 2 Solution: {increased2}")