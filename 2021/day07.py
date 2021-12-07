#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 13:37:37 2021

@author: max
"""

# Day 7 / Part 1

import numpy as np

def load_data(path):
    return [int(num) for num in open(path, "r").read().split(',')]

start_pos = np.array(load_data('data/day07.txt'))

# Day 7 / Part 1
def optimal_fuel(pos):
    optimum = np.median(pos)
    return np.sum(np.abs(pos - optimum)).astype(int)

print(f'>> Day 7 / Part 1: {optimal_fuel(start_pos)}')


# Day 7 / Part 2
def optimal_fuel_p2(pos):
    opt_dist = np.floor(np.mean(pos))
    # upper bound: (n^2 + n)/2
    return np.sum((np.abs(pos - opt_dist) ** 2 + np.abs(pos - opt_dist)) / 2).astype(int)

print(f'>> Day 7 / Part 1: {optimal_fuel_p2(start_pos)}')
