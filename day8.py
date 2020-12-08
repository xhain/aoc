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
    cmds.append([cmd, int(val)])

def solve(cmds):
    accum, i = 0, 0
    run = True
    done = set()
    while run:
        idx = i
        
        if idx >= len(cmds):
            return accum, True
        
        cmd = cmds[idx]
        if idx not in done:
            if cmd[0] == "acc":
                accum += cmd[1]
                done.add(idx)
                i += 1
            elif cmd[0] == "jmp":
                i += cmd[1]
                done.add(idx)
            elif cmd[0] == "nop":
                i += 1
                done.add(idx)
        else:
            run = False
        
    return accum, False

print("/ part 1: ", solve(cmds)[0])


# Part 2 Solution
for i in range(len(cmds)):
    
    # Check jmp -> nop
    if cmds[i][0] == 'jmp':
        cmds[i][0] = 'nop'
        accum, done = solve(cmds) 
        if done:
            print("/ part 2: ", accum)
            break
        else:
            cmds[i][0] = 'jmp'
    
    # Check nop -> jmp     
    elif cmds[i][0] == 'nop':
        cmds[i][0] = 'jmp'
        accum, done = solve(cmds) 
        if done:
            print("/ part 2: ", accum)
            break
        else:
            cmds[i][0] = 'nop'