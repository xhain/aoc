#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 17:52:17 2020

@author: max
"""


# Advent of Code 2020
# Day 8, part 1 & 2
# https://adventofcode.com/2020/day/7

data = [line.rstrip() for line in list(open("data/input8.txt", "r"))]


# Part 1 solution
cmds = []
for line in data:
    cmd, val = line.split(" ")
    cmds.append([cmd, int(val), 0])
   
accum = 0
i = 0
run = True
while run:
    idx = i%len(cmds)
    cmd = cmds[idx]
    
    if cmd[2] == 0:
        if cmd[0] == "acc":
            accum += cmd[1]
            cmds[idx][2] = idx
            i += 1
        elif cmd[0] == "jmp":
            i += cmd[1]
            cmds[idx][2] = idx
        elif cmd[0] == "nop":
            i += 1
            cmds[idx][2] = idx
    else:
        run = False
        
print("/ part 1: ", accum)

# Part 2 Solution
lastCommand = max([cmd[2] for cmd in cmds])