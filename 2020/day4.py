#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 12:51:02 2020

@author: max
"""

# Helpers
def validate_value(value, length, lower, upper):
    if length is None:
        length = len(value)
    if len(value) == length:
        try:
            x = int(value)
            if not lower <= x <= upper:
                return False
        except:
            return False
    else:
        return False
    return True

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
    
    if len(passport) == 8: # all fields?
        p1_valid = True
    elif len(passport) == 7 and 'cid' not in passport: # all fields, except 'cid'?
        p1_valid = True
    
    # Criteria for part 1 is met: Count and continue with part 2 criteria
    if p1_valid: 
        ans1 += 1
        
        # Part 2 criteria
        if not validate_value(passport['byr'], 4, 1920, 2002) \
            or not validate_value(passport['iyr'], 4, 2010, 2020) \
            or not validate_value(passport['eyr'], 4, 2020, 2030) \
            or ('cm' in passport['hgt'] and not validate_value(passport['hgt'].replace('cm', ''), None, 150, 193)) \
            or ('in' in passport['hgt'] and not validate_value(passport['hgt'].replace('in', ''), None, 59, 76)) \
            or not any([u in passport['hgt'] for u in {'cm', 'in'}]) \
            or (len(passport['hcl']) != 7 or passport['hcl'][0] != '#'
                or not all([c in '0123456789abcdef' for c in passport['hcl'][1:]])) \
            or not any([passport['ecl'] == c for c in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}]) \
            or (len(passport['pid']) != 9 or not all([d in '0123456789' for d in passport['pid']])):
                continue
        else:
            ans2 += 1
            
print("/ part 1: ", ans1)
print("/ part 2: ", ans2)