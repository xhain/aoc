#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 13:24:40 2021

@author: max
"""

import numpy as np

def load_data(path):
    return [[int(num) for num in line] for line in open(path, "r").read().split()]

# Day 11 / Part 1

octo = np.array(load_data('data/day11.txt'))
flashes = 0

def get_adjacents(octopus_map, position):
    # https://stackoverflow.com/a/51657308/4888669
    
    i, j = position
    i_max, j_max = octopus_map.shape
    adjacents = set()
    
    if i != 0: 
        adjacents.add((i-1,j)) #above
    if i != i_max - 1:
        adjacents.add((i+1,j)) #below
    if j != 0:
        adjacents.add((i,j-1)) #left
    if j != j_max - 1:
        adjacents.add((i,j+1)) #right
    if i != 0 and j != 0:             #above-left
        adjacents.add((i-1,j-1))       #above-left
    if i != 0 and j != j_max - 1:     #above-right
        adjacents.add((i-1,j+1))       #above-right
    if i != i_max - 1 and j != 0:     #below-left
        adjacents.add((i+1,j-1))       #below-left
    if i != i_max - 1 and j != j_max - 1:  #below-right
        adjacents.add((i+1,j+1))       #below-right
    return adjacents


class Octopus:
    def __init__(self, octopus_map):
        self.map = octopus_map.copy()
        self.total_flashes = 0
        self.epoch = 0
        self.i_max, self.j_max = octopus_map.shape
    
    # Part 1
    def increase_epoch(self, n_epochs):
        for t in range(n_epochs):
            flashed = set()
            self.map += np.ones((10,10), dtype=int)
            self.epoch += 1
            add_flashes = True if np.count_nonzero(self.map > 9) > 0 else False
            self.total_flashes += np.count_nonzero(self.map > 9)
            self.map = np.where(self.map > 9, 0, self.map)
            while add_flashes == True:
                add_flashes = False
                for i in range(self.i_max):
                    for j in range(self.j_max):
                        adjacents = get_adjacents(self.map, (i,j))
                        for adj in adjacents - flashed:
                            if self.map[i,j] != 0 and self.map[adj] == 0:
                                self.map[i,j] += 1
                        # Make flashes and count extra flashes
                if np.count_nonzero(self.map > 9) > 0:
                    add_flashes = True
                self.total_flashes += np.count_nonzero(self.map > 9)
                flashed.update([x for x in zip(np.where(self.map == 0)[0], np.where(self.map == 0)[1])])
                self.map = np.where(self.map > 9, 0, self.map)
     
    # Part 2
    def find_synchonisation(self):
        while self.map.sum() != 0:
            self.increase_epoch(1)
        return(self.epoch)


oct_1 = Octopus(octo)
oct_1.increase_epoch(100)

print(f">> Day 11 / Part 1 is: {oct_1.total_flashes}")

oct_2 = Octopus(octo)
total_epochs = oct_2.find_synchonisation()

print(f">> Day 11 / Part 1 is: {total_epochs}")
    