#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 12:18:58 2021

@author: max
"""

def load_data(path):
    return list( open(path, "r") )

# Day 10 / Part 1
data = load_data('data/day10.txt')
lines = [line.rstrip() for line in data]

scores = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

autoCompleteScores = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

bracketPairs = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}

def isOpen(char):
    return char in ["(", "[", "{", "<"]

def isClose(char):
    return char in [")", "]", "}", ">"]

def isPair(opening, closing):
    if (opening, closing) in [("(", ")"), ("[", "]"), ("{", "}"), ("<", ">")]:
        return True
    return False

total_score = 0
autocomplete_scores = []

for line in lines:
    stack = []
    score = 0
    autocomplete_score = 0
    isIncomplete = True
    
    for char in line:
        if isOpen(char):
            stack.append(char)
            
        if isClose(char):
            if not isPair(stack[-1], char):
                isIncomplete = False
                score = scores[char]
                break
            else:
                stack.pop()
                
    if not isIncomplete:
        total_score += score
        
    else:
        while len(stack) > 0:
            currScore = autoCompleteScores[bracketPairs[stack.pop()]]
            autocomplete_score = 5 * autocomplete_score + currScore
        autocomplete_scores.append(autocomplete_score)

autocomplete_scores.sort()
numScores = len(autocomplete_scores)

print(f'>> Day 10 / Part 1: {total_score}') 
print(f'>> Day 10 / Part 2: {autocomplete_scores[numScores // 2]}')