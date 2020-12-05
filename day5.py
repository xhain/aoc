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

raw_data = list( open("data/input5.txt", "r") )
data = []
for line in raw_data:
    data.append(line.rstrip())
    
# 0-127 (128 rows)
# 0-7   (8 columns)

# Test data
# BFFFBBFRRR: row 70, column 7, seat ID 567.
# FFFBBBFRRR: row 14, column 7, seat ID 119.
# BBFFBBFRLL: row 102, column 4, seat ID 820
test = ["BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]


def get_id_for_line(line):
    tok_row, tok_col = get_token(line)
    row = get_row(tok_row)
    col = get_col(tok_col)
    return get_id(row, col)

def get_id(row, col):
    return row * 8 + col

def get_token(line):
    return (line[:7], line[-4:])
    
def get_row(token):
    rows = np.linspace(0, 127, num=128).astype(int)
    for char in token:
        if char == "F":
            rows = rows[:len(rows)//2]
        elif char == "B":
            rows = rows[-len(rows)//2:]
    return int(rows)
    
def get_col(token):
    cols = np.linspace(0, 7, num=8).astype(int)
    for char in token:
        if char == "L":
            cols = cols[:len(cols)//2]
        elif char == "R":
            cols = cols[-len(cols)//2:]
    return int(cols)

# Part 1
seatIDs = []
for line in data:
    seatIDs.append(get_id_for_line(line))

print("/ part 1: ", max(seatIDs))
    
