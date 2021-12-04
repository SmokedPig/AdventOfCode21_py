# module: Solver for day 2
solverName = "Day2"
description = "Solver "+solverName
filePath = "Inputs\\"+solverName+".txt"

def Part1():
    print(description+" Part 1")

    pos, depth = 0,0
    with open(filePath, "r") as file:
        for x in file.readlines():
            splitString = x.split(" ")
            cmd = splitString[0]
            value = int(splitString[1].rstrip("\n"))
            if cmd == "forward":
                pos += value
            elif cmd == "down":
                depth += value
            elif cmd == "up":
                depth -= value

    print("Pos: " + str(pos))
    print("Depth: " + str(depth))        
    print("Solution (Pos*Depth): "+str(pos*depth))
    print(description+" Part 1 Done")

def Part2():
    print(description+" Part 2")

    pos, depth, aim = 0,0,0
    with open(filePath, "r") as file:
        for x in file.readlines():
            splitString = x.split(" ")
            cmd = splitString[0]
            value = int(splitString[1].rstrip("\n"))
            if cmd == "forward":
                pos += value
                depth += value * aim
            elif cmd == "down":
                aim += value
            elif cmd == "up":
                aim -= value

    print("Pos: " + str(pos))
    print("Depth: " + str(depth))        
    print("Solution (Pos*Depth): "+str(pos*depth))

    print(description+" Part 2 Done")