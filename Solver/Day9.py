# module: Solver for day 9
solverName = "Day9"
description = "Solver "+solverName
filePath = "Inputs\\"+solverName+".txt"
testPath = "Inputs\\"+solverName+"_test.txt"

def Part1():
    print(description+" Part 1")

    with open(testPath, "r") as file:
        heightMap = HeightMap(file)

    sumOfLowPointRisks = sum(list(heightMap.getLowPointRiskLevel()))

    assert sumOfLowPointRisks == 15

    with open(filePath, "r") as file:
        heightMap = HeightMap(file)

    sumOfLowPointRisks = sum(list(heightMap.getLowPointRiskLevel()))

    print(f"Result: {sumOfLowPointRisks}")
    print(description+" Part 1 Done")

def Part2():
    print(description+" Part 2")

    with open(testPath, "r") as file:
        heightMap = HeightMap(file)

    lowPoints = heightMap.getLowPoints()

    basins = list()
    for x in lowPoints:
        basins.append(Basin(heightMap,x))

    basinSizes = sorted(list(map(lambda a: a.getBasinSize(),basins)),reverse=True)
    productOf3LargestBasinSizes = basinSizes[0] * basinSizes[1] * basinSizes[2]

    assert productOf3LargestBasinSizes == 1134

    with open(filePath, "r") as file:
        heightMap = HeightMap(file)

    lowPoints = heightMap.getLowPoints()

    basins = list()
    for x in lowPoints:
        basins.append(Basin(heightMap,x))
    basinSizes = sorted(list(map(lambda a: a.getBasinSize(),basins)),reverse=True)
    productOf3LargestBasinSizes = basinSizes[0] * basinSizes[1] * basinSizes[2]

    print(f"Result: {productOf3LargestBasinSizes}")
    print(description+" Part 2 Done")

class HeightMap():
    def __init__(self, file):
        self.points = self.readFile(file)

    def getLowPointRiskLevel(self):
        for x, pointRow in enumerate(self.points):
            for y, point in enumerate(pointRow):
                if point < min(map(lambda a: a[0],self.getNeigbors(x,y))):
                    yield point+1

    def getLowPoints(self):
        for x, pointRow in enumerate(self.points):
            for y, point in enumerate(pointRow):
                if point < min(map(lambda a: a[0],self.getNeigbors(x,y))):
                    yield (x,y)

    def getNeigbors(self, x, y):
        maxRowsCount = len(self.points)-1
        maxCellCount = len(self.points[0])-1

        tmp = list()
        if x < maxRowsCount:
            tmp.append((self.points[x+1][y],(x+1,y)))
        if x > 0:
            tmp.append((self.points[x-1][y],(x-1,y)))
        if y < maxCellCount:
            tmp.append((self.points[x][y+1],(x,y+1)))
        if y > 0:
            tmp.append((self.points[x][y-1],(x,y-1)))
        return tmp

    def readFile(self, file):
        pointsArray = []
        for x in file.readlines():
            temp = []
            for y in x.rstrip('\n'):
                temp.append(int(y))
            pointsArray.append(temp)
        return pointsArray

class Basin(HeightMap):
    def __init__(self, heightMap, pointCord):
        self.points = heightMap.points
        self.basinCord = pointCord
        self.knownPoints = dict()
        self.knownPoints.update({pointCord:""})

    def getBasinSize(self):
        return self.getBasinPoints(self.basinCord)
        

    def getBasinPoints(self, cord):
        tempbasinPoints = list(filter(lambda a:a[0] < 9, self.getNeigbors(cord[0],cord[1])))
        temp = 1
        for x in tempbasinPoints:
            try:
                self.knownPoints[x[1]] != ""
            except:
                self.knownPoints.update({x[1]:""})
                temp += self.getBasinPoints(x[1])
                continue

        return temp
