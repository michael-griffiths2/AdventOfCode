##Advent of Code 2023 Day 4 - Problem 2

import re

file = open("C:\\Users\\A0853564\\OneDrive - Aon\\Documents\\AdventofCode\\Day 4 - Input.txt", "r")

cards = file.readlines()

totalcards = [1] * len(cards)
totalwins = [0] * len(cards)

for i in range (0, len(cards)):
    winningnums = re.findall(r'(\d+)', cards[i].split("|")[0])
    yournums = re.findall(r'(\d+)', cards[i].split("|")[1])
    for nums in yournums:
        if nums in winningnums[1:]:
            totalwins[i] += 1

for i in range(0, len(cards)):
    for j in range(i + 1, i + totalwins[i] + 1):
        if j > len(totalcards) - 1:
            continue
        else:
            totalcards[j] += totalcards[i]

print(sum(totalcards))