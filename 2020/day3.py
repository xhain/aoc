# -*- coding: utf-8 -*-

# Advent of Code 2020
# Day 3, part 1 & 2
# https://adventofcode.com/2020/day/3


# Import and clean data
raw_data = list( open("data/input3.txt", "r") )
data = []
for line in raw_data:
    data.append(line.rstrip())

# 1: Right 1, down 1.
# 2: Right 3, down 1. (This is the slope you already checked.)
# 3: Right 5, down 1.
# 4: Right 7, down 1.
# 5: Right 1, down 2.
slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]

ans = 1
scores = []
for (dc, dr) in slopes:
    r, c = 0, 0
    score = 0
    
    while r+1 < len(data):
        c += dc
        r += dr
        if data[r][c%len(data[r])] == "#":
            score += 1
    scores.append(score)
    ans *= score
    
print("/ part 1 result: ", scores[1])
print("/ part 2 result: ", ans)
    