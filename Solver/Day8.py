# module: Solver for day 8
solverName = "Day8"
description = "Solver "+solverName
filePath = "Inputs\\"+solverName+".txt"
testPath = "Inputs\\"+solverName+"_test.txt"

import statistics
from time import time

def Part1():
    print(description+" Part 1")

    with open(testPath, "r") as file:
        digits = readScrambledDigit(file)

    easyDigitsCount = countEasyDigits(digits)
        
    assert easyDigitsCount == 26

    with open(filePath, "r") as file:
        digits = readScrambledDigit(file)

    easyDigitsCount = countEasyDigits(digits)
    
    print(f"Result: {easyDigitsCount}")
    print(description+" Part 1 Done")

def readScrambledDigit(file):
    tempList = list()
    for x in list(file.readlines()):
        tmp = x.split("|")
        tempList.append((tmp[0].rstrip(" ").split(" "),tmp[1].lstrip(" ").rstrip("\r\n").split(" ")))
    return tempList

def countEasyDigits(digits):
    tmp = 0
    for x in digits:
        for y in x[1]:
            if len(y) == 2 or len(y) == 3 or len(y) == 4 or len(y) == 7:
                tmp += 1
    return tmp

def Part2():
    print(description+" Part 2")

    with open(testPath, "r") as file:
        digits = readScrambledDigit(file)

    descrampler = Descrambler(digits)
    assert descrampler.unscrambleOutput() == 61229

    with open(filePath, "r") as file:
        digits = readScrambledDigit(file)

    descrampler = Descrambler(digits)
    result = descrampler.unscrambleOutput()
    print(f"Result: {result}")

    print(description+" Part 2 Done")

class Descrambler():
    def __init__(self, digits):
        self.digits = digits

    def unscrambleOutput(self):
        output = 0
        for digit in self.digits:
            sortedList = sorted(digit[0], key=lambda a:len(a))

            _1 = sortedList[0]
            assert len(_1) == 2
            _7 = sortedList[1]
            assert len(_7) == 3
            _4 = sortedList[2]
            assert len(_4) == 4
            _8 = sortedList[9]
            assert len(_8) == 7
            
            a = (self.missingDigit(_1, _7))[0]
            
            abdeg = self.missingDigit(_1, _8)

            edc = (self.missingDigit(sortedList[6], _8) 
            + self.missingDigit(sortedList[7], _8) 
            + self.missingDigit(sortedList[8], _8))

            c = (self.missingDigitLeft(edc,abdeg))[0]

            for x in sortedList[6:9]:
                if c not in x:
                    _6 = x

            for x in sortedList[3:6]:
                if c not in x:
                    _5 = x

            f = (self.missingDigit(_1,c))[0]

            for x in sortedList[3:6]:
                if len(self.missingDigit(_1,x)) == 3:
                    _3 = x

            for x in sortedList[3:6]:
                if _5 not in x and _3 not in x:
                    _2 = x

            for x in filter(lambda a: a not in _6,sortedList[6:9]):
                if len(self.missingDigitLeft(x,_5)) < 2:
                    _9 = x
                elif len(self.missingDigitLeft(x,_6)) < 2:
                    _0 = x

            digitList =[(_0, 0), (_1, 1), (_2, 2), (_3, 3), (_4, 4), (_5, 5), (_6, 6), (_7, 7), (_8, 8), (_9, 9)]

            tmp = ""
            for x in digit[1]:
                for z in digitList:
                    if len(self.missingDigit(z[0], x, False)) == 0:
                        tmp += str(z[1])
            output += int(tmp)
        return output

    def missingDigit(self, a, b, assertForEmpty = True):
        tmp = list()
        for x in a:
            if x not in b:
                tmp.append(x)
        for x in b:
            if x not in a:
                tmp.append(x)
        if assertForEmpty:
            assert len(tmp) > 0
        return tmp

    def missingDigitLeft(self, a, b):
        tmp = list()
        for x in a:
            if x not in b:
                tmp.append(x)
        assert len(tmp) > 0
        return tmp