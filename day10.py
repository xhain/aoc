#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 17:01:17 2020

@author: max
"""

import numpy as np

# Advent of Code 2020
# Day 10, part 1 & 2
# https://adventofcode.com/2020/day/10


data = sorted([int(line.rstrip()) for line in list(open("data/input10.txt", "r"))])


# Part 1 solution (2738)
data.insert(0, 0)
data.append(max(data)+3)
diff = np.diff(data)
print("/ check: all deltas <= 3?", max(diff) == 3)

c1 = 0
c3 = 0
for line in diff:
    if line == 1:
        c1 += 1
    elif line == 3:
        c3 += 1
print("/ part 1: ", c1 * c3)


# Part 2 solution
tracker = {}
def get_amount_for_idx(idx):
    if idx == len(data)-1:
        return 1
    elif idx in tracker:
        return tracker[idx]
    result = 0
    
    for j in range(idx+1, len(data)):
        if data[j]-data[idx] <= 3:
            result += get_amount_for_idx(j)
    tracker[idx] = result
    return result

print("/ part 2: ", get_amount_for_idx(0))
    
