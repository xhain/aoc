#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 23:23:40 2020

@author: max
"""


# Advent of Code 2020
# Day 15, part 1 & 2
# https://adventofcode.com/2020/day/15


data = [0, 1, 4, 13, 15, 12, 16]


mem = {}

def solve(target):
    spoken = data[-1]
    mem = {num: i for i, num in enumerate(data[:-1], 1)}
    
    for idx in range(len(data), target):
    
        if spoken not in mem:
            mem[spoken], spoken = idx, 0
        else:
            mem[spoken], spoken = idx, idx - mem[spoken]
    
    return spoken


# Solution part 1  
print("/ part 1: ", solve(2020))


# Solution part 2
print("/ part 2: ", solve(30000000))

        
        