
from aoc import PuzzleData

from collections import defaultdict

puzzle = PuzzleData(__file__)
data = puzzle.rawdata()


#=============================================

def buildStacks(stacks, line):

    i = 1
    for p in range (0, len(line), 4):
        value = line[p+1]
        if value!=" ": stacks[i].insert(0, value)
        i +=1

    return stacks

#=============================================

def printStacks(stacks):

    count = len(stacks)

    maxStackHight = 0
    for i in range (1, count+1):
        stack = stacks[i]
        maxStackHight = max (maxStackHight, len(stack))

    for j in range (maxStackHight-1,-1,-1):
        for i in range (1, count+1):
            stack = stacks[i]
            if j < len(stack): print (f" [{stack[j]}] ", end="")
            else:              print (f"     ", end="") 
        print ("")

#=============================================

def moveStacks(stacks, line, reversed):

    move     = int(line.split(" from ")[0].replace ("move ", ""))
    movefrom = int(line.split(" from ")[1].split(" to ")[0])
    moveto   = int(line.split(" from ")[1].split(" to ")[1])

    print ("")
    print (line, " --> ", move, movefrom, moveto)
    print ("")

    # Take items from the stack and store them in a temporary list
    tmp = []
    for i in range(move):
        item = stacks[movefrom].pop()
        tmp.append(item)

    # Put the items back in the requested order
    if not reversed: tmp.reverse()
    for t in tmp: stacks[moveto].append(t)

    print ("")
    printStacks(stacks)
    print ("")    

    return stacks

#=============================================

def printTopCrates(stacks):

    count = len(stacks)
    for i in range (1, count+1):
        print (stacks[i][-1], end="")
    print ("")


#=============================================
#=============================================

stacks = defaultdict(list)

for line in data:

    # Build the stacks of crates
    if line.find("[") >= 0: stacks = buildStacks(stacks, line)

    # Print the stacks of crates
    elif line == "": printStacks(stacks)

    # Move the crates arround
    #elif line.find("move") >= 0: stacks = moveStacks(stacks, line, True)  # Part1
    elif line.find("move") >= 0: stacks = moveStacks(stacks, line, False) # Part2

printTopCrates(stacks)
