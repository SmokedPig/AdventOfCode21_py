# module: Solver for day 7
solverName = "Day7"
description = "Solver "+solverName
filePath = "Inputs\\"+solverName+".txt"
testPath = "Inputs\\"+solverName+"_test.txt"

from os import stat
import statistics

def Part1():
    print(description+" Part 1")

    with open(testPath, "r") as file:
        crapSwarm = CrapSwarm(file)

    pos = crapSwarm.bestLocation()
    assert pos == 2
    assert crapSwarm.fuelNeededForPos(pos) == 37

    with open(filePath, "r") as file:
        crapSwarm = CrapSwarm(file)

    pos = crapSwarm.bestLocation()
    result = crapSwarm.fuelNeededForPos(pos)
    
    print(f"Result: {result}")
    print(description+" Part 1 Done")

def Part2():
    print(description+" Part 2")

    with open(testPath, "r") as file:
        crapSwarm = realCrapSwarm(file)

    pos = crapSwarm.bestLocation()
    assert pos == 5
    assert crapSwarm.fuelNeededForPos(pos) == 168

    with open(filePath, "r") as file:
        crapSwarm = realCrapSwarm(file)

    result=99999999999999999
    for x in range(max(crapSwarm.crapDict.keys())+1):
        fuel = crapSwarm.fuelNeededForPos(x)
        if result > fuel:
            result = fuel
            temp = x

    print(f"Result: {result}")

    print(description+" Part 2 Done")

class CrapSwarm:
    def __init__(self, file):
        self.crapDict = dict()
        for x in list(file.readlines()):
            self.listOfCraps = list(map(int,x.split(",")))
            for y in self.listOfCraps:
                self.updateOrCreateCrapDict(y)

    def updateOrCreateCrapDict(self, number):
        try:
            self.crapDict.update({int(number):self.crapDict[int(number)]+1})
        except KeyError:
            self.crapDict.update({int(number):1})

    def fuelNeededForPos(self, pos):
        if type(pos) != 'int':
            pos = int(pos)

        fuelNeeded = 0
        for x, y in self.crapDict.items():
            fuelNeeded += abs(x - pos)*y
        return fuelNeeded

    def bestLocation(self):
        return statistics.median(self.listOfCraps)

class realCrapSwarm(CrapSwarm):
    def fuelNeededForPos(self, pos):
        if type(pos) != 'int':
            pos = int(pos)

        fuelNeeded = 0
        for x, y in self.crapDict.items():
            fuelNeeded += sum(range(abs(x - pos)+1))*y
        return fuelNeeded

    def bestLocation(self):
        weightedPos = 0
        for cPos, cNumber in self.crapDict.items():
            weightedPos += cNumber*cPos


        return round(weightedPos / sum(self.crapDict.values()))