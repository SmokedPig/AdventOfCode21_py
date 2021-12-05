# module: Solver for day 5
solverName = "Day5"
description = "Solver "+solverName
filePath = "Inputs\\"+solverName+".txt"

def Part1():
    print(description+" Part 1")

    with open(filePath, "r") as file:
        vents = readSimpleVents(file)

        scannedArea = Area(vents)
        count = len( list( filter(moreThanOneVent, scannedArea.points.values()) ) )

    print(f"Points overlapping: {count}")
    print(description+" Part 1 Done")

def readSimpleVents(file):
    vents = list()

    for x in list(file.readlines()):
        vents.append(Vent(x))
    print(f"Read {len(vents)} vents")
    return vents

def readAllVents(file):
    vents = list()

    for x in list(file.readlines()):
        vents.append(specialVent(x))
    print(f"Read {len(vents)} vents")
    return vents

def moreThanOneVent(x):
  if x > 1:
    return True
  else:
    return False

class Vent:
    def __init__(self, rawString):
        temp =  self._parseCord(rawString)
        self.x1, self.y1, self.x2, self.y2 = temp[0], temp[1], temp[2], temp[3]

    def _parseCord(self, rawString):
        cleanString = rawString.replace(" ","").rstrip("\n")
        temp = cleanString.split("->")
        start = temp[0].split(",")
        end = temp[1].split(",")

        return (int(start[0]),int(start[1]),int(end[0]),int(end[1]))

    def generatePointsMask(self):
        temp = list()
        if self.x1 == self.x2:
            for z in range( abs(self.y1-self.y2)+1 ):
                temp.append((self.x1, z+min(self.y1,self.y2)))
        elif self.y1 == self.y2:
            for z in range( abs(self.x1-self.x2)+1 ):
                temp.append((z+min(self.x1,self.x2), self.y1))
        else:
            print("WTF Dude")
        return temp

    def get_coveredArea(self):
        if self.x1 == self.x2 or self.y1 == self.y2:
            return self.generatePointsMask()
        else:
            return None

    coveredArea = property(get_coveredArea)

class specialVent(Vent):
    def generateDiagPointsMask(self):
        temp = list()
        for z in range( abs(self.x1-self.x2) + 1):
            temp.append(
                (self.x1 + (z * (-1 if self.x1-self.x2 > 0 else 1)),
                self.y1 + (z * (-1 if self.y1-self.y2 > 0 else 1)))
            )
        return temp

    def get_coveredArea(self):
        if self.x1 == self.x2 or self.y1 == self.y2:
            return self.generatePointsMask()
        elif abs(self.x1-self.x2) == abs(self.y1-self.y2):
            return self.generateDiagPointsMask()
        else:
            return None

    coveredArea = property(get_coveredArea)
    
class Area:
    def __init__(self, vents):
        self.vents = vents

    def nonDiag(self, x):
        return x != ""

    def get_points(self):
        temp = dict()
        for x in self.vents:
            if x.coveredArea == None:
                continue

            for z in x.coveredArea:
                val = temp.setdefault(z, 0)
                if val >= 0:
                    temp.update({z: val+1})
        return temp

    points = property (get_points)

def Part2():
    print(description+" Part 2")

    with open(filePath, "r") as file:
        vents = readAllVents(file)

        scannedArea = Area(vents)
        count = len( list( filter(moreThanOneVent, scannedArea.points.values()) ) )

    print(f"Points overlapping: {count}")

    print(description+" Part 2 Done")