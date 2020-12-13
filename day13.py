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

def factorization(n):
    factors = []
    def get_factor(n):
        x_fixed = 2
        cycle_size = 2
        x = 2
        factor = 1

        while factor == 1:
            for count in range(cycle_size):
                if factor > 1: break
                x = (x * x + 1) % n
                factor = gcd(x - x_fixed, n)

            cycle_size *= 2
            x_fixed = x

        return factor

    while n > 1:
        next = get_factor(n)
        factors.append(next)
        n //= next

    return factors


def multiplyList(myList) :
     
    # Multiply elements one by one
    result = 1
    for l in myList:
        for x in l:
            result = result * x 
    return result 

# Get candidates and delay deltas
d = 0
options, offsets, factors = list(), list(), list()
for char in notes:
        if not char == "x":
            options.append(int(char))
            offsets.append(d)
            factors.append(factorization(int(char)))
        d += 1
        
first_common_product = multiplyList(factors)


# BRUTE FORCE >_<
# result = 0
# y = 836856048822287
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
                  
        