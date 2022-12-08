
from aoc import PuzzleData

puzzle = PuzzleData(__file__)
data = puzzle.getStrList()

# Process the data
elfs = []
cals = 0

for i in data:
    if i == "":
        elfs.append(cals)
        cals = 0
    else:
        cals += int(i)

elfs.sort()

# Part 1
print (elfs[-1])

# Part 2
print (sum(elfs[-3:]))