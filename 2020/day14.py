#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 23:00:35 2020

@author: max
"""

def apply_mask(val, masker):
    result = ""
    for a, b in zip(val, masker):
        result += a if b == 'X' else b
    return result

def apply_float_mask(val, masker):
    result = ['']
    for x, y in zip(val, masker):
        
        if y == '0':
            for i in range(len(result)):
                result[i] += x
        elif y == '1':
            for i in range(len(result)):
                result[i] += y
        else:
            result.extend(result)
            for i in range(len(result)):
                result[i] += str((i < len(result) / 2) * 1)
    return result

# Advent of Code 2020
# Day 14, part 1 & 2
# https://adventofcode.com/2020/day/14

data = [line.rstrip() for line in open("data/input14.txt", "r")]


# Solution part 1
def solve_p1():
    mem = {}
    mask = data[0].split(' = ')[1]
    for line in data:
        
        if 'mask' in line:
            mask = line.split(' = ')[1]
        
        else:
            reg, val = line.split(' = ')
            reg = int(reg.replace('mem[', '').replace(']', ''))
            val = bin(int(val))[2:].zfill(36)
            
            mem[reg] = int(apply_mask(val, mask), 2)
            
    return sum([val for val in mem.values()])

print("/ part 1: ", solve_p1())


# Solution part 2
def solve_p2():
    mem = dict()
    mask = data[0].replace('mask = ', '')
    for line in data[1:]:
        
        if 'mask' in line:
            mask = line.replace('mask = ', '')
            
        else:
            pos, val = line.split(' = ')
            pos = pos.replace('mem[', '').replace(']', '')
            pos = bin(int(pos))[2:].zfill(36)
            registers = apply_float_mask(pos, mask)
            
            for regs in registers:
                mem[int(regs, 2)] = int(val)
                
    return sum([val for val in mem.values()])

print("/ part 1: ", solve_p2())
