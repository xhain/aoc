# -*- coding: utf-8 -*-

def load_data(path):
    return list( open(path, "r") )

# Day 1 / Part 1
data = load_data("data/day01.txt")

calories_max, calories_cur = 0, 0
for row in data:
    if row == '\n':
        if calories_cur > calories_max:
            calories_max = calories_cur
        calories_cur = 0
    else:
        calories_cur += int(row)
        
print(f">> Day 1 / Part 1 Solution: {calories_max}")


# Day 1 / Part 2
top_N = 3
calories = []
calories_cur = 0
for row in data:
    if row == '\n':
        calories.append(calories_cur)
        calories_cur = 0
    else:
        calories_cur += int(row)

print(f">> Day 1 / Part 2 Solution: {sum(sorted(calories, reverse=True)[:3])}")
