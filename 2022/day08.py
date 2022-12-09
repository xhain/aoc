#!/usr/local/bin/asicpy
# -*- coding: utf-8 -*-

def load_data(path):
    return list( open(path, "r") )

# Day 8 / Part 1
raw_data = load_data("data/day08.txt")
result = 0

for idx in range(len(raw_data)):
    for jdx in range(len(raw_data[0])):
        print(raw_data[idx][jdx])


print(f">> Day 6 / Part 1 Solution: {result}")


# Day 8 / Part 2

print(f">> Day 6 / Part 1 Solution: {result}")

