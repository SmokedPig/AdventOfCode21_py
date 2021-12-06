# module: Solver for day 6
solverName = "Day6"
description = "Solver "+solverName
filePath = "Inputs\\"+solverName+".txt"
testPath = "Inputs\\"+solverName+"_test.txt"

def Part1():
    print(description+" Part 1")

    with open(testPath, "r") as file:
        fishSchool = FishSchool(file)
    
    fishSchool.simulateGrowthCycles(18)
    assert fishSchool.NumberOfFish == 26
    fishSchool.simulateGrowthCycles(80-18)
    assert fishSchool.NumberOfFish == 5934

    with open(filePath, "r") as file:
        fishSchool = FishSchool(file)
    
    fishSchool.simulateGrowthCycles(80)

    print(f"Fishcount: {fishSchool.NumberOfFish}")
    
    print(description+" Part 1 Done")

def Part2():
    print(description+" Part 2")

    with open(testPath, "r") as file:
        fishSchool = FishSchool(file)
    
    fishSchool.simulateGrowthCycles(18)
    assert fishSchool.NumberOfFish == 26
    fishSchool.simulateGrowthCycles(80-18)
    assert fishSchool.NumberOfFish == 5934
    fishSchool.simulateGrowthCycles(256-80)
    assert fishSchool.NumberOfFish == 26984457539

    with open(filePath, "r") as file:
        fishSchool = FishSchool(file)
    
    fishSchool.simulateGrowthCycles(256)

    print(f"Fishcount: {fishSchool.NumberOfFish}")

    print(description+" Part 2 Done")

class FishSchool:
    def __init__(self, file):
        self.fishDict = dict.fromkeys(range(10),0)
        self.cycles = 0
        for x in list(file.readlines()):
            self.listOfFish = list(map(lambda a: self.fishDict.update({int(a):self.fishDict[int(a)]+1}), x.split(",")))

    def simulateGrowthCycles(self, cycles):
        #print(f"Cycle {self.cycles} -> 0: {self.fishDict[0]}, 1: {self.fishDict[1]}, 2: {self.fishDict[2]}, 3: {self.fishDict[3]}, 4: {self.fishDict[4]}, 5: {self.fishDict[5]}, 6: {self.fishDict[6]}, 7: {self.fishDict[7]}, 8: {self.fishDict[8]}, 9: {self.fishDict[9]}")
        for x in range(cycles):
            for daysLeftToBirth, fish_count in self.fishDict.items():
                if daysLeftToBirth == 0:
                    self.fishDict[9] = fish_count
                    self.fishDict[7] += fish_count
                elif daysLeftToBirth == 9:
                    self.fishDict[9] = 0
                    self.fishDict[8] = fish_count
                else:
                    self.fishDict[daysLeftToBirth-1] = fish_count
            
            self.cycles += 1
            #print(f"After {self.cycles} day -> 0: {self.fishDict[0]}, 1: {self.fishDict[1]}, 2: {self.fishDict[2]}, 3: {self.fishDict[3]}, 4: {self.fishDict[4]}, 5: {self.fishDict[5]}, 6: {self.fishDict[6]}, 7: {self.fishDict[7]}, 8: {self.fishDict[8]}, 9: {self.fishDict[9]}")
        pass

    def get_fishCount(self):
        return sum(self.fishDict.values())

    NumberOfFish = property(get_fishCount)

    def get_cycles(self):
        return self.cycles

    Cycles = property(get_cycles)