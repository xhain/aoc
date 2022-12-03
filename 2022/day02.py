# -*- coding: utf-8 -*-

def load_data(path):
    return list( open(path, "r") )

# Day 2 / Part 1
data = load_data("data/day02.txt")

lookup = {
  "X": "✂️",
  "Y": "🪨",
  "Z": "📄",
  "A": "✂️",
  "B": "🪨",
  "C": "📄",
}

def evaluate_day1(P1, P2):
    # A Rock, B Paper, C Scissors
    # X Rock, Y Paper, Z Scissors
    score = 0
    result = "N.A."

    # score for gesture
    if P2 == "✂️":
        score += 1
    elif P2 == "🪨":
        score += 2
    elif P2 == "📄":
        score += 3

    # score for win
    if P1 == P2:
        score += 3
        result = "DRAW"
    elif P2 == "✂️" and P1 == "📄":
        score += 6
        result = "WIN"
    elif P2 == "🪨" and P1 == "✂️":
        score += 6
        result = "WIN"
    elif P2 == "📄" and P1 == "🪨":
        score += 6
        result = "WIN"
    else:
        result = "LOST"

    return score, result

result = 0
for row in data:
    P1, P2 = row.strip('\n').split(' ')
    P2 = lookup[P2]
    P1 = lookup[P1]
    score, res = evaluate_day1(P1, P2)
    result += score
    #print(f"Elve {P1} vs. {P2} Me  >> {res} >> {score} >> {result}")

print(f">> Day 1 / Part 1 Solution: {result}")


# Day 2 / Part 2

def evaluate_day2(P1, P2):
    # A ✂️, B 🪨, C 📄
    # X Loose, Y Draw, Z Win

    score = 0

    # LOOSE
    if P2 == "X":
        score += 0
        if P1 == "✂️":
            # 📄
            score += 3
        elif P1 == "🪨":
            # ✂️
            score += 1
        elif P1 == "📄":
            # 🪨
            score += 2

    # DRAW
    elif P2 == "Y":
        score += 3
        if P1 == "✂️":
            score += 1
        elif P1 == "🪨":
            score += 2
        elif P1 == "📄":
            score += 3

    # WIN
    elif P2 == "Z":
        score += 6
        if P1 == "✂️":
            # 🪨
            score += 2
        elif P1 == "🪨":
            # 📄
            score += 3
        elif P1 == "📄":
            # ✂️
            score += 1

    return score

result = 0
for row in data:
    P1, P2 = row.strip('\n').split(' ')
    P1 = lookup[P1]
    result += evaluate_day2(P1, P2)

print(f">> Day 1 / Part 2 Solution: {result}")
