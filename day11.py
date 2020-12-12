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

data = [line.rstrip() for line in list(open("data/input11.txt", "r"))]
original = data.copy()


def count_neighbours():
    count = 0
    for row in data:
        for seat in row:
            if seat == '#':
                count += 1
    return count


def count_surround(row,col):
    count = 0
    curRow = data[row]
    
    # Right
    if col+1 <= len(curRow)-1:
        if curRow[col+1] == '#': count += 1

    # Left
    if col-1 >= 0:
        if curRow[col-1] == '#': count += 1

    # Bottom row
    if row+1 <= len(data)-1:
        botRow = data[row+1]
        if botRow[col] == '#': count += 1
        
        if col-1 >= 0:
            if botRow[col-1] == '#': count += 1
        
        if col+1 <= len(botRow)-1:
            if botRow[col+1] == '#': count += 1
    # Top row
    if row-1 >= 0:
        topRow = data[row-1]
        if topRow[col] == '#': count += 1
        
        if col-1 >= 0:
            if topRow[col-1] == '#': count += 1
        
        if col+1 <= len(topRow)-1:
            if topRow[col+1] == '#': count += 1
    
    return count


def count_view(row, col):
    count = 0

    # i is for row, j for col
    iU, iD, jR, jL = row-1, row+1, col+1, col-1
    N, S, E, W, NE, SE, NW, SW = False, False, False, False, False, False, False, False

    while not (N and S and W and E and NE and SE and NW and SW):
        # North
        if not N and iU >= 0:
            if data[iU][col] == '#':
                count += 1
                N = True
            elif data[iU][col] == 'L':
                N = True
        else:
            N=True
            
        # South
        if not S and iD <= len(data)-1:
            if data[iD][col] == '#':
                count += 1
                S = True
            elif data[iD][col] == 'L':
                S = True
        else:
            S=True

        # East
        if not E and jR <= len(data[row])-1:
            if data[row][jR] == '#':
                count += 1
                E = True
            elif data[row][jR] == 'L':
                E = True
        else:
            E = True

        # West
        if not W and jL >= 0:
            if data[row][jL] == '#':
                count += 1
                W = True
            elif data[row][jL] == 'L':
                W = True
        else:
            W = True

        # North West
        if not NW and iU >= 0 and jL >= 0:
            if data[iU][jL] == '#':
                count += 1
                NW = True
            elif data[iU][jL] == 'L':
                NW = True
        else:
            NW = True

        # South West
        if not SW and iD <= len(data)-1 and jL >= 0:
            if data[iD][jL] == '#':
                count += 1
                SW = True
            elif data[iD][jL] == 'L':
                SW = True
        else:
            SW = True

        # North East
        if not NE and iU >= 0 and jR <= len(data[row])-1:
            if data[iU][jR] == '#':
                count += 1
                NE = True
            elif data[iU][jR] == 'L':
                NE = True
        else:
            NE = True

        # South East
        if not SE and iD <= len(data)-1 and jR <= len(data[row])-1:
            if data[iD][jR] == '#':
                count += 1
                SE = True
            elif data[iD][jR] == 'L':
                SE = True
        else:
            SE=True

        iU -= 1
        iD += 1
        jR += 1
        jL -= 1

    return count
        

def check_rules(tolerance):
    newPlan = []

    for row in range(len(data)):
        curRow = data[row]
        newRow = []

        for col in range(len(curRow)):
            if curRow[col] == '.':
                newRow.append('.')
                continue

            nCount = 0
            if tolerance == 4:
                nCount = count_surround(row, col)
                
            elif tolerance == 5:
                nCount = count_view(row, col)

            if curRow[col] == 'L' and nCount == 0:
                newRow.append('#')
            
            elif curRow[col] == '#' and nCount >= tolerance:
                newRow.append('L')

            else:
                newRow.append(curRow[col])
        newPlan.append(newRow)

    # Update global data
    for i in range(len(data)):
        data[i] = newPlan[i]


def solve(tolerance):
    prev = data.copy()
    check_rules(tolerance)

    while data != prev:
        prev = data.copy()
        check_rules(tolerance)
    
    return count_neighbours()


# Solutions with help from "Dylan Codes"
print("/ part 1: ", solve(4))

data = original.copy()
print("/ part 2: ", solve(5))
