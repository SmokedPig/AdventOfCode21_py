# module: Solver for day 11
solverName = "Day11"
description = "Solver "+solverName
filePath = "Inputs\\"+solverName+".txt"
testPath = "Inputs\\"+solverName+"_test.txt"

def Part1():
    print(description+" Part 1")

    with open(testPath, "r") as file:
        octopuses = Octopuses(file)

    octopuses.simulateSteps(10)
    assert octopuses.flashes == 204
    octopuses.simulateSteps(90)
    assert octopuses.flashes == 1656

    with open(filePath, "r") as file:
        octopuses = Octopuses(file)

    octopuses.simulateSteps(100)
    print(f"Result: {octopuses.flashes}")

    print(description+" Part 1 Done")

def Part2():
    print(description+" Part 2")

    with open(testPath, "r") as file:
        octopuses = Octopuses(file)

    sync = octopuses.simulateSteps(200)
    assert sync == 195

    with open(filePath, "r") as file:
        octopuses = Octopuses(file)

    sync = octopuses.simulateSteps(1000)
    print(f"Result: {sync}")

    print(description+" Part 2 Done")

class Octopuses():
    def __init__(self, file):
        self.array = []
        self.steps = 0
        self.flashes = 0

        self.firstSync = 0

        for x in file.readlines():
            temp = []
            for y in x.rstrip('\n'):
                temp.append(int(y))
            self.array.append(temp)

    def simulateSteps(self, targetSteps):
        stepDict = dict()
        for step in range(targetSteps):
            if len(stepDict) == 100:
                return self.steps

            stepDict = dict()
            self.steps += 1

            self.increaseAllOctopuses()
            flashedOctopuses = self.findAllOctopusesFlashing(stepDict)
            while len(flashedOctopuses) > 0:
                self.increaseNeighbors(stepDict, flashedOctopuses)
                flashedOctopuses = self.findAllOctopusesFlashing(stepDict)

    def increaseNeighbors(self, stepDict, flashedOctopuses = None):
        maxRowsCount = len(self.array)-1
        maxCellCount = len(self.array[0])-1

        if flashedOctopuses != None:
            temp = flashedOctopuses
        else:
            temp = stepDict

        for x in temp:
            if x[0] < maxRowsCount:
                self.tryIncrease(x[0]+1,x[1],stepDict)
                if x[1] < maxCellCount:
                    self.tryIncrease(x[0]+1,x[1]+1,stepDict)
                if x[1] > 0:
                    self.tryIncrease(x[0]+1,x[1]-1,stepDict)
            if x[0] > 0:
                self.tryIncrease(x[0]-1,x[1],stepDict)
                if x[1] < maxCellCount:
                    self.tryIncrease(x[0]-1,x[1]+1,stepDict)
                if x[1] > 0:
                    self.tryIncrease(x[0]-1,x[1]-1,stepDict)
            if x[1] < maxCellCount:
                self.tryIncrease(x[0],x[1]+1,stepDict)
            if x[1] > 0:
                self.tryIncrease(x[0],x[1]-1,stepDict)

    def tryIncrease(self,x,y,stepDict):
        try:
            if stepDict[(x,y)] == 1:
                pass
        except:
            self.array[x][y] += 1
            pass

    def findAllOctopusesFlashing(self, stepDict):
        flashedOctopuses = list()
        for x, x_val in enumerate(self.array):
            for y in range(len(x_val)):
                if self.array[x][y] > 9:
                    try:
                        if stepDict[(x,y)] == 1:
                            continue
                    except:
                        stepDict.update({(x,y):1})
                        self.flashes += 1
                        flashedOctopuses.append((x,y))
                        self.array[x][y] = 0
                        continue
        return flashedOctopuses

    def increaseAllOctopuses(self):
        for x, x_val in enumerate(self.array):
            for y in range(len(x_val)):
                self.array[x][y] += 1