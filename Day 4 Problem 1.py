##Advent of Code 2023 Day 4 - Problem 1

import re

file = open("C:\\Users\\A0853564\\OneDrive - Aon\\Documents\\AdventofCode\\Day 4 - Input.txt", "r")

cards = file.readlines()

grandtotal = 0

for i in range (0, len(cards)):
    winningnums = re.findall(r'(\d+)', cards[i].split("|")[0])
    yournums = re.findall(r'(\d+)', cards[i].split("|")[1])
    total = -1
    for nums in yournums:
        if nums in winningnums[1:]:
            total += 1
    if total > -1:
        grandtotal += 2 ** total
    else:
        grandtotal += 0

print(grandtotal)