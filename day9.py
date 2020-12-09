#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 13:26:14 2020

@author: max
"""

from itertools import combinations as combo

# Advent of Code 2020
# Day 9, part 1 & 2
# https://adventofcode.com/2020/day/9


data = [int(line.rstrip()) for line in list(open("data/input9.txt", "r"))]


# Part 1 solution
i = 26
target = None
while i < len(data):
    
    vals = data[i-25:i]
    sumto = data[i]
    found = False
    
    for nums in combo(vals, 2):
        if sum(nums) == sumto and found != True:
            found = True
            continue
    
    if not found:
        target = sumto
        print("/ part 1: ", target)
        break 
    i += 1
    
# Part 2 solution
found = False
for i in range(len(data)):
    for N in range(len(data)):
        
        if sum(data[i:i+N]) == target:
            found = True
            print("/ part 2: ", min(data[i:i+N])+max(data[i:i+N]))
            break
    if found:
        break

# This could be optimized ;)