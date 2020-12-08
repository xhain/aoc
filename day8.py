#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 17:52:17 2020

@author: max
"""

def modify(instruction, idx):
    global fixing
    if not fixing:
        if 'nop' in instruction and idx not in flipped['nop']:
            fixing = True
            flipped['nop'].add(idx)
            return instruction.replace('nop', 'jmp')
        if 'jmp' in instruction and idx not in flipped['jmp']:
            fixing = True
            flipped['jmp'].add(idx)
            return instruction.replace('jmp', 'nop')
    return instruction

# Advent of Code 2020
# Day 8, part 1 & 2
# https://adventofcode.com/2020/day/7


data = [line.rstrip() for line in list(open("data/input8.txt", "r"))]


# Part 1 solution
cmds = []
for line in data:
    cmd, val = line.split(" ")
    cmds.append([cmd, int(val), 0])

def solve(cmdsMod):
    accum = 0
    i = 0
    run = True
    done = set()
    while run:
        idx = i
        
        if idx >= len(cmdsMod):
            return accum, True
        
        cmd = cmdsMod[idx]
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
    # This is a bit hacky :
    # It doesn't check the inverse case, when swappign "nop" for "jmp"
    # But that would merely be another 8 lines
    if cmds[i][0] == 'jmp':
        cmds[i][0] = 'nop'
        accum, done = solve(cmds) 
        if done:
            print("/ part 2: ", accum)
            break
        else:
            cmds[i][0] = 'jmp'
    