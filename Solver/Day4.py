# module: Solver for day 4

solverName = "Day4"
description = "Solver "+solverName
filePath = "Inputs\\"+solverName+".txt"

def Part1():
    print(description+" Part 1")

    with open(filePath, "r") as file:
        generatedNumbers = list(map(int,file.readline().rstrip("\n").split(",")))
        
        boards = readBoards(file)
        hasWon, index = False, 0
        
        while hasWon == False:
            for b in boards:
                b.mark(generatedNumbers[index])

            for b in boards:
                    if(b.hasWon):
                        hasWon = True
                        winningBoard = b
                        break
            index += 1
        else:
            print("We have a BINGO!")
            print(f"Last number called was {generatedNumbers[index-1]}")
            print(f"Sum of all unmarked numbers on this board {winningBoard.unmarkedSum}")
            print(f"Result (last Number * Sum of all unmarked) {generatedNumbers[index-1] * winningBoard.unmarkedSum}")
        
    print(description+" Part 1 Done")

def readBoards(file):
    boards = list()

    board_rows, i = [""] * 5, 0
    for x in list(file.readlines())[1:]:
        if x == "\n":
            continue

        board_rows[i] = x.rstrip("\n")
        if i == 4:
            boards.append(Board(board_rows))
            i=0
        else:
            i += 1
    print(f"Read {len(boards)} boards")
    return boards

class Board:
    def __init__(self, rowsAsString):
        self.rows = self._parseRows(rowsAsString)

    def _parseRows(self, string):
        temp = list()
        for x in string:
            temp.append( list( map(self.asNumber,x.rstrip("\n").lstrip(" ").replace("  "," ").split(" ")) ) )
        return temp

    def asNumber(self, number):
        return (int(number),False)

    def get_win(self):
        for x in self.rows:
            if all(y[1] for y in x ):
                return True
        for x in self.cols:
            if all(y[1] for y in x ):
                return True
        return False

    def get_cols(self):
        cols = []
        for x in range(len(self.rows)):
            cols.append(list())
            for y in self.rows:
                cols[x].append(y[x])
        return cols

    def mark(self, number):
        for index_x, x in enumerate(self.rows):
            for index_y, y in enumerate(x):
                if number == y[0]:
                    self.rows[index_x][index_y] = (number, True)

    def get_unmarkedSum(self):
        sum = 0
        for x in self.rows:
            for y in x:
                if not y[1]:
                    sum += y[0]
        return sum

    hasWon = property(get_win)
    cols = property(get_cols)
    unmarkedSum = property(get_unmarkedSum)
    

def Part2():
    print(description+" Part 2")

    with open(filePath, "r") as file:
        generatedNumbers = list(map(int,file.readline().rstrip("\n").split(",")))
        
        boards = readBoards(file)
        index = 0
        
        while len(boards)>0 and index < 100:
            for b in boards:
                b.mark(generatedNumbers[index])

            for b in boards:
                    if(b.hasWon):
                        lastBoard = b
                        boards.remove(b)
            index += 1
        else:
            print("We have a BINGO!")
            print(f"Last number called was {generatedNumbers[index-1]}")
            print(f"Sum of all unmarked numbers on this board {lastBoard.unmarkedSum}")
            print(f"Result (last Number * Sum of all unmarked) {generatedNumbers[index-1] * lastBoard.unmarkedSum}")

    print(description+" Part 2 Done")