#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 20:39:31 2020

@author: max
"""

# from scipy.signal import convolve2d
# import numpy as np


# Advent of Code 2020
# Day 11, part 1 & 2
# https://adventofcode.com/2020/day/11

plan = [list(row) for row in open("data/input11.txt").read().splitlines()]

neighbours = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def solve(data, rules_func):
    rows, cols = len(data), len(data[0])
    data_new = [row[:] for row in data]
    done = True
    for r in range(rows):
        for c in range(cols):
            data_new[r][c] = rules_func(data, r, c)
            done = done and data[r][c] == data_new[r][c]
    return data_new, done

def try_solve(data, rules):
    data, done = solve(data, rules)
    while not done:
        data, done = solve(data, rules)
    return sum(row.count('#') for row in data)

def apply_rules_p1(data, row, col):
    rows, cols = len(data), len(data[0])
    count = 0
    for dr, dc in neighbours:
        if 0 <= row + dr < rows and 0 <= col + dc < cols:
            count += data[row + dr][col + dc] == '#'
    if data[row][col] == 'L' and count == 0:
        return '#'
    if data[row][col] == '#' and count >= 4:
        return 'L'
    return data[row][col]

def apply_rules_p2(data, row, col):
    rows, cols = len(data), len(data[0])
    count = 0
    for dr, dc in neighbours:
        cr, cc = row + dr, col + dc
        while 0 <= cr < rows and 0 <= cc < cols and data[cr][cc] == '.':
            cr += dr
            cc += dc
        count += 0 <= cr < rows and 0 <= cc < cols and data[cr][cc] == '#'
    if data[row][col] == 'L' and count == 0:
        return '#'
    if data[row][col] == '#' and count >= 5:
        return 'L'
    return data[row][col]


print("/ part 1: ", try_solve(plan, apply_rules_p1))
print("/ part 2: ", try_solve(plan, apply_rules_p2))
