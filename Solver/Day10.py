# module: Solver for day 10
solverName = "Day10"
description = "Solver "+solverName
filePath = "Inputs\\"+solverName+".txt"
testPath = "Inputs\\"+solverName+"_test.txt"

def Part1():
    print(description+" Part 1")

    with open(testPath, "r") as file:
        testResult = sum( map(lambda a : getCorruptionPoints(a.rstrip("\n")),file.readlines()) )
    assert testResult == 26397

    with open(filePath, "r") as file:
        result = sum( map(lambda a : getCorruptionPoints(a.rstrip("\n")),file.readlines()) )
    print(f'Result: {result}')

    print(description+" Part 1 Done")

def Part2():
    print(description+" Part 2")

    incompleteLines = list()
    with open(testPath, "r") as file:
        for x in filter(lambda a : getCorruptionPoints(a.rstrip("\n")) == 0,file.readlines()):
            incompleteLines.append(x)
    
    testResults = map(lambda a: getAutoCompletionPoints(a),incompleteLines)
    sortedResults = sorted(testResults)
    
    assert sortedResults[ int((len(sortedResults)-1)/2) ] == 288957

    incompleteLines = list()
    with open(filePath, "r") as file:
        for x in filter(lambda a : getCorruptionPoints(a.rstrip("\n")) == 0,file.readlines()):
            incompleteLines.append(x)
    
    results = map(lambda a: getAutoCompletionPoints(a),incompleteLines)
    sortedResults = sorted(results)
    
    print(f"Results: {sortedResults[ int((len(sortedResults)-1)/2) ]}")
    print(description+" Part 2 Done")

def getAutoCompletionPoints(line):
    autocompleteString = getCorruptionPoints(line, False).rstrip('\n')[::-1]
    return getAutoCompletionScore(autocompleteString)

def getAutoCompletionScore(string):
    points = 0
    for x in string:
        if x == '(':
            points = (points*5 + 1)
        elif x == '[':
            points = (points*5 + 2)
        elif x == '{':
            points = (points*5 + 3)
        elif x == '<':
            points = (points*5 + 4)
    return points

def getCorruptionPoints(line, returnScore = True):
    removedChunk = True
    while removedChunk:
        removedChunk = False
        if '()' in line:
            line = line.replace('()','')
            removedChunk = True
        if '[]' in line:
            line = line.replace('[]','')
            removedChunk = True
        if '{}' in line:
            line = line.replace('{}','')
            removedChunk = True
        if '<>' in line:
            line = line.replace('<>','')
            removedChunk = True
    for x in line:
        if x == ')':
            assert returnScore
            return 3
        if x == ']':
            assert returnScore
            return 57
        if x == '}':
            assert returnScore
            return 1197
        if x == '>':
            assert returnScore
            return 25137
    return 0 if returnScore else line