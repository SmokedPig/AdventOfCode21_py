# module: Solver for day 12
solverName = "Day12"
description = "Solver "+solverName
filePath = "Inputs\\"+solverName+".txt"
testPath = "Inputs\\"+solverName+"_test.txt"

def Part1():
    print(description+" Part 1")

    with open(testPath, "r") as file:
        caveSystem = CaveSystem(file)

    tmp = caveSystem.getAllPossibleRoutes().split(';')
    
    #Becaues I can't be arsed to debug this
    for x in list(tmp):
        if x == '':
            tmp.remove(x)

    assert len(tmp) == 226

    with open(filePath, "r") as file:
        caveSystem = CaveSystem(file)

    tmp = caveSystem.getAllPossibleRoutes().split(';')
    
    for x in list(tmp):
        if x == '':
            tmp.remove(x)

    print(f"Result: {len(tmp)}")
    print(description+" Part 1 Done")

def Part2():
    print(description+" Part 2")

    with open(testPath, "r") as file:
        caveSystem = CaveSystem(file)

    tmp = list()
    for x in filter(lambda a: not a.isBig,caveSystem.caves.values()):
        tmp += caveSystem.getAllPossibleRoutes(specialSmallCave=x.Id).split(';')
    
    #Becaues I can't be arsed to debug this
    for x in list(tmp):
        if x == '':
            tmp.remove(x)

    magicRemoveDuplicates = list(set(tmp))
    assert len(magicRemoveDuplicates) == 3509

    with open(filePath, "r") as file:
        caveSystem = CaveSystem(file)

    tmp = list()
    for x in filter(lambda a: not a.isBig,caveSystem.caves.values()):
        tmp += caveSystem.getAllPossibleRoutes(specialSmallCave=x.Id).split(';')
    
    #Becaues I can't be arsed to debug this
    for x in list(tmp):
        if x == '':
            tmp.remove(x)

    magicRemoveDuplicates = list(set(tmp))

    print(f"Result: {len(magicRemoveDuplicates)}")
    print(description+" Part 2 Done")

class CaveSystem():
    def __init__(self, file):
        self.caves = dict()

        for x in file.readlines():
            tunnel = x.rstrip('\n').split('-')
            self.addOrUpdateCave(tunnel)

        for x in dict(self.caves):
            if x == 'start':
                self.start = self.caves[x]
                self.caves.pop(x)
            if x == 'end':
                self.end = self.caves[x]
                self.caves.pop(x)

    def addOrUpdateCave(self, tunnel):
        try:
            cave = self.caves[tunnel[0]]
        except:
            self.caves.update({tunnel[0]:Cave(tunnel[0])})
            cave = self.caves[tunnel[0]]
        cave.tunnels.append(tunnel[1])

        try:
            cave = self.caves[tunnel[1]]
        except:
            self.caves.update({tunnel[1]:Cave(tunnel[1])})
            cave = self.caves[tunnel[1]]
        cave.tunnels.append(tunnel[0])

    def getAllPossibleRoutes(self, startCave = None, forbiddenCaves = '', specialSmallCave = ''):
        assert startCave == None or type(startCave) == Cave
        assert forbiddenCaves == None or type(forbiddenCaves) == str

        if startCave == None:
            startCave = self.start

        possibleCaves = list()
        for x in startCave.tunnels:
            if x == 'start':
                continue
            possibleCaves.append(x)

        allowedCaves = list()
        for x in possibleCaves:
            if x in specialSmallCave:
                allowedCount = 2
            else:
                allowedCount = 1
            if x != 'end' and not(self.caves[x].isBig) and forbiddenCaves != None and forbiddenCaves.count(x) == allowedCount:
                continue
            else:
                allowedCaves.append(x)

        workingRoutes = ''
        for x in allowedCaves:
            newForbiddenCaves = forbiddenCaves
            if(x == 'end'):
                workingRoutes += f'{forbiddenCaves}{startCave.Id},end;'
            newForbiddenCaves += startCave.Id + ','
            if x != 'end':
                tmp = self.getAllPossibleRoutes(self.caves[x], newForbiddenCaves,specialSmallCave)
                if tmp != None:
                    workingRoutes += tmp
        return workingRoutes if workingRoutes != '' else None

class Cave():
    def __init__(self, id):
        self.Id = id
        self.tunnels = list()
        self.isBig = self.checkSize(id)

    def checkSize(self, id):
        for x in id:
            if x.islower():
                return False
        return True