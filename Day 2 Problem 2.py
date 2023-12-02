## Advent of Code 2023 Day 2 - Problem 1

def cubechecker(input):
    alldrawsarray = (input.split(":")[1]).split(";")
    redcubes = 0
    bluecubes = 0
    greencubes = 0
    for i in range(len(alldrawsarray)):
        drawarray = alldrawsarray[i].split(",")
        for j in range(len(drawarray)):
            drawarray[j] = drawarray[j].strip()
            if drawarray[j].split()[1] == "red":
                if redcubes < int(drawarray[j].split()[0]):
                    redcubes = int(drawarray[j].split()[0])
            if drawarray[j].split()[1] == "blue":
                if bluecubes < int(drawarray[j].split()[0]):
                    bluecubes = int(drawarray[j].split()[0])
            if drawarray[j].split()[1] == "green":
                if greencubes < int(drawarray[j].split()[0]):
                    greencubes = int(drawarray[j].split()[0])
    return redcubes * bluecubes * greencubes    

total = 0
file = open("C:\\Users\\A0853564\\OneDrive - Aon\\Documents\\Advent of Code\\Day 2 - Input.txt", "r")
while True:
    line = file.readline()
    if not line:
        break
    total += cubechecker(line)

print(total)