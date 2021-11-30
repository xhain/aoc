#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 23:47:57 2020

@author: max
"""

import numpy as np

# Advent of Code 2020
# Day 16, part 1 & 2
# https://adventofcode.com/2020/day/16

data = [line.rstrip() for line in open("data/input16.txt", "r")]


# Solution part 1
raw_rules = data[:20]
raw_tickets = data[25:]

rules = []
for line in raw_rules:
    line = line.split(": ")[1].split(" or ")
    line = [x.split("-") for x in line]
    vals = []
    for val in line: 
        vals.append(list(map(int, val)))
    rules.append(vals)
    
tickets = []
for line in raw_tickets:
    line = line.split(",")
    line = [int(x) for x in line]
    tickets.append(line)

# 49427820 too high
result = 0
validTickets = []
for line in tickets:
    errorRate = 0
    ticketValid = False
    for val in line:
        valid = False
        for rule in rules:
            if rule[0][0] <= val <= rule[0][1] or \
                rule[1][0] <= val <= rule[1][1]:
                    valid = True
                    break
        if not valid:
            errorRate += val
    
    result += errorRate
    
    if errorRate == 0:
        validTickets.append(line)

print("/ part 1: ", result)
            
# Solution part 2
# ... WIP

            
        