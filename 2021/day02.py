# -*- coding: utf-8 -*-

def load_data(path):
    return list( open(path, "r") )

# Day 2 / Part 1
data = load_data("data/day02.txt")

x, depth = 0, 0
for line in data:
    direction, amount = line.replace('\n', '').split(' ')
    amount = int(amount)
    
    if direction == 'forward':
        x += amount
    elif direction == 'down':
        depth += amount
    elif direction == 'up':
        depth -= amount
        
print(f">> Day 2 / Part 1 Solution: {x*depth}")


# Day 2 / Part 2
data = load_data("data/day02.txt")

x, depth, aim = 0, 0, 0
for line in data:
    direction, amount = line.replace('\n', '').split(' ')
    amount = int(amount)
    
    if direction == 'forward':
        x += amount
        depth += aim * amount
    elif direction == 'down':
        aim += amount
    elif direction == 'up':
        aim -= amount       
    
print(f">> Day 2 / Part 2 Solution: {x*depth}")