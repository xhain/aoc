# -*- coding: utf-8 -*-

# Advent of Code 2020
# Day 1, part 1
# https://adventofcode.com/2020/day/1

data = list( open("data/input.txt", "r") )

# for line1 in data:
#     for line2 in data:
#         number1 = int(line1)
#         number2 = int(line2)
#         if number1 == number2:
#             break
#         elif number1+number2 == 2020:
#             print(number1, number2)
#             print(number1 + number2)
#             print(number1*number2)
    
    
# Day 1, part 2
for line1 in data:
    for line2 in data:
        for line3 in data:
            number1 = int(line1)
            number2 = int(line2)
            number3 = int(line3)
            if number1 == number2 or number1 == number3 or number2 == number3:
                break
            elif number1+number2+number3 == 2020:
                print(number1, number2, number3)
                print(number1 + number2 + number3)
                print(number1*number2*number3)
