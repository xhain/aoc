# -*- coding: utf-8 -*-

def load_data(path):
    return list( open(path, "r") )

# Day 5 / Part 1
data = load_data("data/day06.txt")

def find_start(data, num_chars=4):
    result = None
    for line in data:
        for idx in range(len(line)):
            chars = line[idx:idx + num_chars]
            if len(chars)==len(set(chars)):
                result = idx + num_chars
                break
    return result

print(f">> Day 6 / Part 1 Solution: {find_start(data, num_chars=4)}")


# Day 6 / Part 2

print(f">> Day 6 / Part 1 Solution: {find_start(data, num_chars=14)}")

