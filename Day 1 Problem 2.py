## Advent of Code 2023 Day 1 - Problem 2

substring = ['zero','one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def number_check(input):
    for i in range(len(substring)):
        if substring[i] in input:
            return True

def calibration_number(input):
    number_mapping = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
                      'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    
    checkstring = ''

    global first_digit
    global last_digit

    for i in range(len(input)):
        checkstring += input[i]
        if number_check(checkstring):
            break
        if input[i].isnumeric():
            break
    if number_check(checkstring):
        for w in substring:
            if w in checkstring:
                numberword = w
                break
        first_digit = number_mapping[numberword]
    if input[i].isnumeric():        
        first_digit = input[i]
    del checkstring
    checkstring = ''

    for i in range(len(input) - 1, -1, -1):
        checkstring += input[i]
        if number_check(checkstring[::-1]):
            break   
        if input[i].isnumeric():
            break
    if number_check(checkstring[::-1]):
        for w in substring:
            if w in checkstring[::-1]:
                numberword = w
                break
        last_digit = number_mapping[numberword]
    if input[i].isnumeric():        
        last_digit = input[i]
    calibration_number = int(first_digit + last_digit)

    print(first_digit, last_digit)

    return calibration_number

total = 0
file = open("C:\\Users\\A0853564\\OneDrive - Aon\\Documents\\Advent of Code\\Day 1 - Input.txt", "r")
while True:
    line = file.readline()
    if not line:
        break
    print(line)
    total += calibration_number(line)

print(total)