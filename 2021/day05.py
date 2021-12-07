#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 19:03:00 2021

@author: max
"""

def load_data(path):
    return list( open(path, "r") )

# Day 5 / Part 1

from collections import Counter
import itertools
import sys

def parse_input(data):
    vectors = []
    for line in data:
        vector = [(int(x), int(y)) for (x,y) in tuple([point.split(',') for point in line.split(" -> ")])]
        vectors.append(vector)
    
    return vectors

def vec_to_pts(vector, include_diagonals):
    ((x1, y1), (x2, y2)) = vector
    if x1 == x2:
        return [(x1, y) for y in (range(y1, y2+1) if y1<y2 else range(y2, y1+1))]
    elif y2 == y1:
        return [(x, y1) for x in (range(x1, x2+1) if x1<x2 else range(x2, x1+1))]
    
    # Part 2
    elif include_diagonals:
        slope = round((y2-y1) / (x2-x1))
        intercept = y2-slope*x2
        return [(x, round(slope*x+intercept)) for x in (range(x1, x2+1) if x1<x2 else range(x2, x1+1))]
    else:
        return []
     
def find_overlaps(vectors, include_diagonals):
    all_points = itertools.chain(*[vec_to_pts(vector, include_diagonals) for vector in vectors])
    occurrences = Counter(all_points)
    return [(point, count) for (point, count) in occurrences.items() if count > 1]


data = load_data('data/day05.txt')
vecs = parse_input(data)

pt1_overlapped_points = find_overlaps(vecs, include_diagonals=False)
print(">> Day 5 / Part 1: {}".format(len(pt1_overlapped_points)))

pt2_overlapped_points = find_overlaps(vecs, include_diagonals=True)
print(">> Day 5 / Part 2: {}".format(len(pt2_overlapped_points)))
        
        
    