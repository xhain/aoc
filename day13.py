#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 18:04:36 2020

@author: max
"""

from math import gcd

# Advent of Code 2020
# Day 13, part 1 & 2
# https://adventofcode.com/2020/day/13

data = [line.rstrip() for line in open("data/input13.txt", "r")]

target = int(data[0])
notes = data[1].split(',')


# Part 1 solution

def find_next_time(n, target):
    # returns time and delta for next future stop
    dMin = target % n
    tMin = target - dMin
    tMax = tMin + n
    dMax = tMax - target
    return [n, tMax, dMax]
 
def solve_p1():
    candidates = list()
    for char in notes:
        if not char == 'x':
            candidates.append(find_next_time(int(char), target))  
    resultIdx = candidates.index(min(candidates, key=lambda x: x[2]))
    return candidates[resultIdx][0] * candidates[resultIdx][2]
    
print("/ part 1: ", solve_p1())


# Part 2 solution
# solution = for_all(c = n * option + offset) == True

def list_product(l):
    ret = 1
    for x in l:
        ret *= x
    return ret

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, r, s = egcd(b % a, a)
        return (gcd, s - (b // a) * r, r)   

# Get candidates and delay deltas
d = 0
options, offsets = list(), list()
for char in notes:
        if not char == "x":
            options.append(int(char))
            offsets.append(-d)
        d += 1

# Apply chinese remainder theorem
LCM = list_product(options)
N = [LCM / bus for bus in options]
M = [egcd(N[i], options[i])[1] for i in range(len(options))]
t = sum([int(offsets[i] * M[i] * N[i]) for i in range(len(options))]) % LCM
print("/ part 2: ", t)


# BRUTE FORCE >_<
# result = 0
# 100000000000000, 836856048822287
# while True:
#     checksum = 0
#     for n, d in zip(options, offsets):
#         if (y + d) % n == 0:
#             checksum += 1 
#     if checksum == 9:
#         print(y)
#         break
#     else:
#         y += 1
                          