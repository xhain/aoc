#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 11:41:38 2021

@author: max
"""

# Day 6 / Part 1
import copy

f = open("data/day06.txt", "r")
data = [int(i) for i in f.read().split(',')]

# Parse starting population age
pop_start_age = [0 for i in range (9)]
for i in data:
    pop_start_age[i] += 1

# Run simulation
def simulate_population(pop_age, days):
    pop_age_local = copy.deepcopy(pop_age)
    for i in range(days):
        # Check how many births & reset (pop)
        births = pop_age_local.pop(0)
        pop_age_local.append(births)
        pop_age_local[6] += births
    return sum(pop_age_local)

print(f'>> Day 6 / Part 1: {simulate_population(pop_start_age, 80)}')
print(f'>> Day 6 / Part 2: {simulate_population(pop_start_age, 256)}')