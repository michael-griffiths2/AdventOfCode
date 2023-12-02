## Advent of Code 2023 Day 1 - Problem 1

def calibration_number(input):

    for i in range(len(input)):
        if input[i].isnumeric():
            break
    first_digit = input[i]
    
    for i in range(len(input) - 1, -1, -1):
        if input[i].isnumeric():
            break
    last_digit = input[i]
    
    calibration_number = int(first_digit + last_digit)

    return calibration_number

calibration_number('1abc')

total = 0
file = open("C:\\Users\\A0853564\\OneDrive - Aon\\Documents\\Advent of Code\\Day 1 - Input.txt", "r")
while True:
    line = file.readline()
    if not line:
        break
    total += calibration_number(line)

print(total)
