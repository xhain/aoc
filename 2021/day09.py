#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 15:09:29 2021

@author: max
"""

import numpy as np
from scipy import ndimage as ndi

def load_data(path):
    return list( open(path, "r") )

# Day 9 / Part 1
data = load_data('data/day09.txt')

# Parse to array
hmap = []
for line in data:
    hmap.append(list(line.strip('\n')))
    
hmap = np.array(hmap).astype(int)

# Filter using kernel to compare point to adjacent points
fp = np.asarray([
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
    ])
mask = hmap > ndi.minimum_filter(hmap, footprint=fp, mode='nearest') 
result = np.sum(np.where(mask == False, hmap+1, 0))

print(f'>> Day 9 / Part 1: {result}')

# Day 9 / Part 2
from skimage import data, filters, color, morphology
from skimage.segmentation import flood, flood_fill


checkers = data.checkerboard()

# Fill a square near the middle with value 127, starting at index (76, 76)
filled_checkers = flood_fill(checkers, (76, 76), 127)

# WIP...
        