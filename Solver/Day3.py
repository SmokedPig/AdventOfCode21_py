# module: Solver for day 3
from os import terminal_size
from typing import Iterator


solverName = "Day3"
description = "Solver "+solverName
filePath = "Inputs\\"+solverName+".txt"

def Part1():
    print(description+" Part 1")

    gam_b,gam_d,eps_b,eps_d = "",0,"",0

    oneCount, zeroCount = [],[]
    with open(filePath, "r") as file:
        for x in file.readlines():
            cleanX = x.rstrip("\n")

            if len(oneCount) < len(cleanX):
                for x in range(len(cleanX) - len(oneCount)):
                    oneCount.append(0)

            if len(zeroCount) < len(cleanX):
                for x in range(len(cleanX) - len(zeroCount)):
                    zeroCount.append(0)

            for index, y in enumerate(cleanX):
                if y == '1':
                    oneCount[index] += 1
                else:
                    zeroCount[index] += 1
        
        if len(oneCount) != len(zeroCount):
            print("ERRRRRRRROR")
        else:
            for index, x in enumerate(oneCount):
                if x>zeroCount[index]:
                    gam_b += "1"
                else:
                    gam_b += "0"
        
        eps_b = ''.join(['1' if i == '0' else '0' for i in gam_b])
        gam_d = int(gam_b,2)
        eps_d = int(eps_b,2)
            
    print("Gamma: " + str(gam_b) + " (bin) "+str(gam_d)+" (dec)")
    print("Epsilon: " + str(eps_b) + " (bin) "+str(eps_d)+" (dec)")
    print("Solution (Gamma*Epsilon): "+str(gam_d*eps_d))

    print(description+" Part 1 Done")

def Part2():
    print(description+" Part 2")

    with open(filePath, "r") as file_:
        file = file_.readlines()

        oxy = filterList(file, False)
        co2 = filterList(file, True)

    print("Oxy: " + str(oxy[0]) + " (bin) "+str(oxy[1])+" (dec)")
    print("CO2: " + str(co2[0]) + " (bin) "+str(co2[1])+" (dec)")
    print("Solution (Oxy*CO2): "+str(oxy[1]*co2[1]))

    print(description+" Part 2 Done")

def filterList(listOfNumbers, invert):
    index = 0
    while len(listOfNumbers) > 1:
        listOfNumbers = filterByFirstBit(listOfNumbers,index,invert)
        index += 1
    else:
        bin = listOfNumbers[0].rstrip("\n").lstrip("0")
        dec = int(bin, 2)
        return (bin, dec)

def filterByFirstBit(listOfNumbers, index, invert):
    bitCount = [0] * 2
    for x in listOfNumbers:
        cleanX = x.rstrip("\n")
        if cleanX[index] == '1':
            bitCount[1] += 1
        else:
            bitCount[0] += 1
    if len(listOfNumbers[0].rstrip("\n")) == 1:
        return "0" if invert else "1"
    filterBit = '0' if (bitCount[0] > bitCount[1]) ^ invert else '1'
    return list(filter(lambda x: x[index]==filterBit, listOfNumbers))