# module: Solver for day 13
solverName = "Day13"
description = "Solver "+solverName
filePath = "Inputs\\"+solverName+".txt"
testPath = "Inputs\\"+solverName+"_test.txt"

isX = True
isY = False

def Part1():
    print(description+" Part 1")

    with open(testPath, "r") as file:
        puzzleInput = PuzzleInput(file)

    puzzleInput.fold(7,False)
    puzzleInput.print()
    assert len(puzzleInput.dots) == 17

    with open(filePath, "r") as file:
        puzzleInput = PuzzleInput(file)

    puzzleInput.fold(655,True)
    # puzzleInput.print()

    print(f"Result: {len(puzzleInput.dots)}")
    print(description+" Part 1 Done")

def Part2():
    print(description+" Part 2")

    with open(testPath, "r") as file:
        puzzleInput = PuzzleInput(file)

    puzzleInput.fold(puzzleInput.folds[0][1],puzzleInput.folds[0][0])
    assert len(puzzleInput.dots) == 17

    puzzleInput.fold(puzzleInput.folds[1][1],puzzleInput.folds[1][0])
    puzzleInput.print()


    with open(filePath, "r") as file:
        puzzleInput = PuzzleInput(file)

    for fold in puzzleInput.folds:
        puzzleInput.fold(fold[1],fold[0])

    puzzleInput.print()

    print(description+" Part 2 Done")

class PuzzleInput():
    def __init__(self, file):
        self.dots = dict()
        self.folds = list()
        self.size_x, self.size_y = 0, 0
        for x in file.readlines():
            x = x.rstrip("\n")
            if x == "":
                continue
            elif 'fold along ' in x:
                if 'x' in x:
                    tmp_x = int(x.split("=")[1])
                    self.folds.append((isX,tmp_x))
                if 'y' in x:
                    tmp_y = int(x.split("=")[1])
                    self.folds.append((isY,tmp_y))
            else:
                tmp_x = int(x.split(",")[0])
                tmp_y = int(x.split(",")[1])
                if tmp_y > self.size_y:
                    self.size_y = tmp_y
                if tmp_x > self.size_x:
                        self.size_x = tmp_x
                self.dots.update({(int(tmp_x),int(tmp_y)):''})

    def print(self):
        for y in range(self.size_y+1):
            x_str=''
            for x in range(self.size_x+1):
                try:
                    self.dots[(x,y)]
                    x_str += '#'
                except:
                    x_str += '.'
            print(x_str)

    def fold(self, line, isXFold):
        if not isXFold:
            for index, y in enumerate(range(line,self.size_y+1)):
                for x in range(self.size_x+1):
                    try:
                        if y == line:
                            self.dots.pop((x,y))
                        self.dots[(x,y)]
                        self.dots.update({(x, line - index):''})
                        self.dots.pop((x,y))
                    except:
                        pass
            self.size_y = line-1
        else:
            for index, x in enumerate(range(line, self.size_x+1)):
                for y in range(self.size_y+1):
                    try:
                        if x == line:
                            self.dots.pop((x,y))
                        else:
                            self.dots[(x,y)]
                            self.dots.update({(line - index, y):''})
                            self.dots.pop((x,y))
                    except:
                        pass
            self.size_x = line-1
