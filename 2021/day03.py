#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 12:18:53 2021

@author: max
"""

def load_data(path):
    return list( open(path, "r") )

def split(string):
    return [char for char in string]

# Day 3 / Part 1
data = load_data("data/day03.txt")

num_of_lines = len(data)
sum_of_lines = [0]*12
for line in data:
    chars = split(line.replace('\n', ''))
    for idx in range(len(chars)):
        sum_of_lines[idx] += int(chars[idx])

gamma, epsilon = str(), str()
for idx in range(len(sum_of_lines)):
    num = sum_of_lines[idx]  / (num_of_lines/2)
    gamma += "0" if num < 1 else "1"
    epsilon += "0" if num > 1 else "1"
    
gamma_int = int(gamma, 2)
epsilon_int = int(epsilon, 2)

print(f">> Day 3 / Part 1 Solution: {gamma_int * epsilon_int}")

# Day 3 / Part 2
