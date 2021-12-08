#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 12:39:50 2021

@author: max
"""

def load_data(path):
    return list( open(path, "r") )

# Day 8 / Part 1
data = load_data('data/day08.txt')

# Count occurance of patterns indicating digits 1, 4, 7, or 8
num_segments = [2, 3, 4, 7]
counter = 0
sumo = 0

def get_diff(first, second):
    first_set, second_set = set(first), set(second)
    return len((first_set | second_set) - (first_set & second_set))

def get_same(first, second):
    first_set, second_set = set(first), set(second)
    return len(first_set & second_set)

for line in data:
    pattern, display = line.strip('\n').split(' | ')
    codes = {}
    
    # Part 1
    for digit in display.split(' '):
        if any(len(digit) == num for num in num_segments):
            counter += 1
        
    # Part 2
    codes = {}
    segments, digits = line.strip().split(' | ')
    
    splitted_segments = list(map(''.join, map(sorted, segments.split())))
    splitted_digits = list(map(''.join, map(sorted, digits.split())))
    
    for segment in splitted_segments:
        if len(segment) == 2:
            codes[1] = segment
        elif len(segment) == 3:
            codes[7] = segment
        elif len(segment) == 4:
            codes[4] = segment
        elif len(segment) == 7:
            codes[8] = segment
    for segment in splitted_segments:
        if len(segment) == 5:
            if get_diff(codes[1], segment) == 3:
                codes[3] = segment
            elif get_diff(codes[4], segment) == 3:
                codes[5] = segment
            else:
                codes[2] = segment
        elif len(segment) == 6:
            if get_same(codes[1], segment) == 1:
                codes[6] = segment
            elif get_same(codes[4], segment) == 4:
                codes[9] = segment
            else:
                codes[0] = segment
    
    inverse_codes = {value: str(key) for key, value in codes.items()}
    sumo += int(''.join([inverse_codes[digit] for digit in splitted_digits]))

print(f'>> Day 8 / Part 1: {counter}')
print(f'>> Day 8 / Part 1: {sumo}')