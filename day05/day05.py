
from aoc import PuzzleData
from collections import defaultdict

p = PuzzleData("day05")
data = p.rawdata()

# Part 1
reverseOrder = True

# Part 2
#reverseOrder = False

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

def printTopCrates(stacks):

    count = len(stacks)
    for i in range (1, count+1):
        print (stacks[i][-1], end="")
    print ("")


#=============================================

stacks = defaultdict(list)

for line in data:

    if line.find("[") >= 0:

        # Build the stacks of crates

        i = 1
        for p in range (1, 37, 4):
            try:    value = line[p]
            except: value = " "
            if value!=" ": stacks[i].insert(0, line[p])
            i +=1


    elif line == "":

        # Print the stacks of crates

        printStacks(stacks)


    elif line.find("move") >= 0:

        # Move the crates arround

        # move 11 from 8 to 3
        move     = int(line.split(" from ")[0].replace ("move ", ""))
        movefrom = int(line.split(" from ")[1].split(" to ")[0])
        moveto   = int(line.split(" from ")[1].split(" to ")[1])

        print ("")
        print (line, " --> ", move, movefrom, moveto)
        print ("")

        tmp = []
        for i in range(move):
            item = stacks[movefrom].pop()
            tmp.append(item)

        if reverseOrder:
            for t in tmp:
                stacks[moveto].append(t)

        else:
            tmp.reverse()
            for t in tmp:
                stacks[moveto].append(t)

        print ("")
        printStacks(stacks)
        print ("")
        

printTopCrates(stacks)
