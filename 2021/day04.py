#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 13:12:35 2021

@author: max
"""

# Day 4 / Part 1

with open("data/day04.txt", "r") as f:
    lines = f.readlines()


bingo_numbers = [int(num) for num in lines.pop(0).split(",")]
assert len(lines) % 6 == 0
n_boards = len(lines) // 6
bingo_boards = [
    [[int(num) for num in line.split()] for line in lines[6 * i + 1 : 6 * (i + 1)]]
    for i in range(n_boards)
]

# Check
def has_won(board, called_numbers):
    return any(all(num in called_numbers for num in line) for line in [*board, *zip(*board)])


def score(board, called_numbers, last_number):
    return last_number * sum(num for line in board for num in line if num not in called_numbers)


# Recursively
def find_score_of_first_bingo_winner_r(boards, called_numbers, remaining_numbers):
    if not remaining_numbers:
        return -1
    current_number = remaining_numbers[0]
    called_numbers.add(current_number)
    for board in boards:
        if has_won(board, called_numbers):
            return score(board, called_numbers, current_number)
    return find_score_of_first_bingo_winner_r(boards, called_numbers, remaining_numbers[1:])


def find_score_of_last_bingo_winner_r(boards, called_numbers, remaining_numbers):
    if not remaining_numbers:
        return -1
    current_number = remaining_numbers[0]
    called_numbers.add(current_number)
    if len(boards) == 1 and has_won(boards[0], called_numbers):
        return score(boards[0], called_numbers, current_number)
    return find_score_of_last_bingo_winner_r(
        [b for b in boards if not has_won(b, called_numbers)], called_numbers, remaining_numbers[1:]
    )

print(">> Day 4 / Part 1: ", find_score_of_first_bingo_winner_r(bingo_boards, set(), bingo_numbers))
print(">> Day 4 / Part 2: ", find_score_of_last_bingo_winner_r(bingo_boards, set(), bingo_numbers))