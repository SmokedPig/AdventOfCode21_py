# module: Solver for day 1
description = "Start Solver Day 1"

def Part1():
    print(description+" Part 1")

    old_value, counter = 0, 0
    with open("Inputs\\Day1.txt", "r") as file:
        lines = file.readlines()
        temp = lines[0]
        for x in lines[1:]:
            temp = int(x.rstrip("\n"))
            if old_value < temp:
                counter = counter + 1
            old_value = temp

    print("Counter: " + str(counter))
    print(description+" Part 1 Done")

def Part2():
    print(description+" Part 2")

    counter = 0
    with open("Inputs\\Day1.txt", "r") as file:
        lines = file.readlines()
        for x in range(len(lines)-3):
            group_A = sum(int(z) for z in lines[x:x+3])
            group_B = sum(map(int,lines[x+1:x+4]))
            if group_B > group_A:
                counter = counter + 1

    print("Counter: " + str(counter))
    print(description+" Part 2 Done")