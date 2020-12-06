#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 23:07:06 2020

@author: max
"""

# Advent of Code 2020
# Day 6, part 1 & 2
# https://adventofcode.com/2020/day/6

data = [line.rstrip() for line in list(open("data/input6.txt", "r"))]

# Part 1 Solution
ans1 = 0
group = ""
for line in data:
    if len(line) > 0:
        group = group + line
    else:
        ans1 += len(''.join(set(group)))
        group = ""
print("/ part 1: ", ans1)


# Part 2 Solution
ans2 = 0
group, num_ppl = {}, 0
for line in data:
    if len(line) > 0:
        num_ppl += 1
        for char in [char for char in line]:
            if char not in group:
                group[char] = 1
            else:
                group[char] += 1
    else:
        for key in group:
            if group[key] == num_ppl:
                ans2 += 1
        group, num_ppl = {}, 0
print("/ part 2: ", ans2)
