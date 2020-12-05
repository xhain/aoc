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
# 0-127 (128 rows)
# 0-7   (8 columns)

# Test data
# BFFFBBFRRR: row 70, column 7, seat ID 567.
# FFFBBBFRRR: row 14, column 7, seat ID 119.
# BBFFBBFRLL: row 102, column 4, seat ID 820
test = ["BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]

# Import data
raw_data = list( open("data/input5.txt", "r") )
data = []
for line in raw_data:
    data.append(line.rstrip())
    
# Helper functions
def get_id_for_line(line):
    tok_row, tok_col = get_token(line)
    row = get_row(tok_row)
    col = get_col(tok_col)
    return row, col, get_id(row, col)

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


# Part 1 Solution
seatPos, seatIDs = [], []
for line in data:
    row, col, seatID = get_id_for_line(line)
    seatPos.append([row, col])
    seatIDs.append(seatID)
    

# Part 2 Solution
seatPos = sorted(seatPos, key=lambda x: x[0], reverse=False)
minRow = min([x[0] for x in seatPos])
maxRow = max([x[0] for x in seatPos])

# get all possible seats
rows = np.arange(minRow+1, maxRow).astype(int)
cols = np.arange(0, 7+1).astype(int)
posSeats = []
for row in rows:
    for col in cols:
        posSeats.append([row, col])

# find the one missing from the possible combos
mySeat = []
for posSeat in posSeats:
    if posSeat not in seatPos:
        mySeat.append(posSeat)


# Print results
print("/ part 1: ", max(seatIDs))
print("/ part 2: Seat:", mySeat[0], "/ ID: ", get_id(mySeat[0][0], mySeat[0][1]))
    
