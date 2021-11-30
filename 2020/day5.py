#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 17:26:53 2020

@author: max
"""

import numpy as np

# Advent of Code 2020
# Day 5, part 1 & 2
# https://adventofcode.com/2020/day/5

# Part 1 Solution
seatIDs = []
for line in list( open("data/input5.txt", "r") ):
    seatIDs.append(int(''.join([{'F': '0', 'L': '0', 'B': '1', 'R': '1'}[c] for c in line.rstrip()]), base=2))
seatIDs.sort()
print("/ part 1: ", seatIDs[-1])
    
# Part 2 Solution
myMask = np.where(np.diff(seatIDs + [seatIDs[-1]+1]) > 1, True, False)
print("/ part 2: ", np.max(np.array(seatIDs) * myMask + 1))
