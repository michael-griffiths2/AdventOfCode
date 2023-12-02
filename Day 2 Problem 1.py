## Advent of Code 2023 Day 2 - Problem 1

def cubechecker(input):
    gameid = int((input.split()[1]).split(":")[0])
    alldrawsarray = (input.split(":")[1]).split(";")
    drawpossible = [True] * len(alldrawsarray)
    for i in range(len(alldrawsarray)):
        redcubes = 0
        bluecubes = 0
        greencubes = 0
        drawarray = alldrawsarray[i].split(",")
        for j in range(len(drawarray)):
            drawarray[j] = drawarray[j].strip()
            if drawarray[j].split()[1] == "red":
                redcubes = int(drawarray[j].split()[0])
                if redcubes > 12:
                    drawpossible[i] = False
            if drawarray[j].split()[1] == "blue":
                bluecubes = int(drawarray[j].split()[0])
                if bluecubes > 14:
                    drawpossible[i] = False
            if drawarray[j].split()[1] == "green":
                greencubes = int(drawarray[j].split()[0])
                if greencubes > 13:
                    drawpossible[i] = False
    
    if all(drawpossible) == False:
        return 0
    else:
        return gameid

total = 0
file = open("C:\\Users\\A0853564\\OneDrive - Aon\\Documents\\Advent of Code\\Day 2 - Input.txt", "r")
while True:
    line = file.readline()
    if not line:
        break
    total += cubechecker(line)

print(total)