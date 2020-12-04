#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 12:51:02 2020

@author: max
"""

# Advent of Code 2020
# Day 4, part 1 & 2
# https://adventofcode.com/2020/day/4

# Part 1:
# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)
# ...all IDs = 8

man_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
opt_fields = ['cid']

raw_data = list( open("data/input4.txt", "r") )
data, entry = [], {}

# Parse data
for line in raw_data:
    line = line.rstrip()
    if line:
        tokens = line.split(" ")
        for token in tokens:
            field, value = token.split(":")
            entry[field] = value  
    else:
        data.append(entry)
        entry = {}
        
# Check data
ans1, ans2 = 0, 0
for passport in data:
    p1_valid = False
    p2_valid = True
    if len(passport) == 8: # all fields?
        p1_valid = True
    elif len(passport) == 7 and 'cid' not in passport: # all fields, except 'cid'?
        p1_valid = True
        
    if p1_valid: 
        ans1 += 1
        
        # Part 2:
        # byr (Birth Year) - four digits; at least 1920 and at most 2002.
        # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        # hgt (Height) - a number followed by either cm or in:
        # If cm, the number must be at least 150 and at most 193.
        # If in, the number must be at least 59 and at most 76.
        # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        # pid (Passport ID) - a nine-digit number, including leading zeroes.
        # cid (Country ID) - ignored, missing or not.
        if not 1920 <= int(entry['byr']) <= 2002:
            p2_valid = False
        if not 2010 <= int(entry['iyr']) <= 2020:
            p2_valid = False
        if not 2020 <= int(entry['eyr']) <= 2030:
            p2_valid = False
        if entry['hgt'][-len('cm'):] == 'cm':
            try:
                height = int(entry['hgt'][:-len('cm')])
                if not 150 <= height <= 193:
                    p2_valid = False
            except ValueError:
                p2_valid = False
        if entry['hgt'][-len('in'):] == 'in':
            try:
                height = int(entry['hgt'][:-len('in')])
                if not 59 <= height <= 76:
                    p2_valid = False
            except ValueError:
                p2_valid = False
            
    
    if p2_valid:
        ans2 += 1
            
print("/ part 1: ", ans1)
print("/ part 2: ", ans2)