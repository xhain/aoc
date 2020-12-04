# -*- coding: utf-8 -*-

# Advent of Code 2020
# Day 2, part 1 & 2
# https://adventofcode.com/2020/day/2

data = list( open("data/input2.txt", "r") )

def main():
    c1, c2 = 0, 0
    for line in data:
        c1 += part1(line)
        c2 += part2(line)
    print("p1: ", c1, "/ p2: ", c2)
    

def part1(line):
    min_freq, max_freq, letter, pword = readLine(line)
    if min_freq <= pword.count(letter) <= max_freq:
        return 1
    return 0

def part2(line):
    first, second, letter, pword = readLine(line)
    if (pword[first - 1] == letter) != (pword[second - 1] == letter):
        return 1
    return 0

def readLine(line):
    content = line.rstrip().split(' ')
    pos1, pos2 = map(int, content[0].split('-'))
    letter = content[1][0]
    pword = content[2]
    return pos1, pos2, letter, pword
    
main()