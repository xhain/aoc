#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 23:29:25 2020

@author: max
"""

from math import sin, cos, radians

# Advent of Code 2020
# Day 12, part 1 & 2
# https://adventofcode.com/2020/day/12

data = [[line.rstrip()[0], int(line.rstrip()[1:])] for line in open("data/input12.txt", "r")]


# Solution part 1
class Marker():
    def __init__(self):
        self.Orientation = 0 # = East (right)
        self.North = 0
        self.East = 0
        
def solve_p1(ferry):
    for move in data:
        
        # Up (N) / Down (S)
        if move[0] == "N":
            ferry.North += move[1]
        elif move[0] == "S":
            ferry.North -= move[1]
            
        # Left (W) / Right (E)
        elif move[0] == "E":
            ferry.East += move[1]
        elif move[0] == "W":
            ferry.East -= move[1]
            
        # Turn
        elif move[0] == "R":
            ferry.Orientation = (ferry.Orientation + move[1])%360
        elif move[0] == "L":
            ferry.Orientation = (ferry.Orientation - move[1])%360
            
        # Forward
        elif move[0] == "F":
            if ferry.Orientation == 0: # right
                ferry.East += move[1]
            elif ferry.Orientation == 90: # down
                ferry.North -= move[1]
            elif ferry.Orientation == 180: # left
                ferry.East -= move[1]
            elif ferry.Orientation == 270: # right
                ferry.North += move[1]
    
    return abs(ferry.North) + abs(ferry.East)

Ferry1 = Marker()
print("/ part 1: ", solve_p1(Ferry1))


# Solution part 2
Ferry2 = Marker()
wp = Marker()
wp.East, wp.North = 10, 1

def solve_p2(Waypoint, Ferry):
    for move in data:
            # Up (N) / Down (S)
            if move[0] == "N":
                Waypoint.North += move[1]
            elif move[0] == "S":
                Waypoint.North -= move[1]
                
            # Left (W) / Right (E)
            elif move[0] == "E":
                Waypoint.East += move[1]
            elif move[0] == "W":
                Waypoint.East -= move[1]
                
            # Turn
            elif move[0] == "L":
                for _ in range(move[1]//90):
                    Waypoint.East, Waypoint.North = -Waypoint.North, Waypoint.East
            elif move[0] == "R":
                for _ in range(move[1]//90):
                    Waypoint.East, Waypoint.North = Waypoint.North, -Waypoint.East
     
            # Forward
            elif move[0] == "F":
                Ferry.East += move[1] * Waypoint.East
                Ferry.North += move[1] * Waypoint.North
 
    return abs(Ferry.North) + abs(Ferry.East)

print("/ part 2: ", solve_p2(wp, Ferry2))