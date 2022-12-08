
from aoc import PuzzleData

puzzle = PuzzleData(__file__)
data = puzzle.getStrList()

ROCK, PAPER, SCISSORS = [0, 1, 2]
LOSS, DRAW, WIN       = [0, 3, 6]

# Lookup a shape or result from the character in the data
Char2Shape  = {"A":ROCK, "B":PAPER, "C":SCISSORS, "X":ROCK, "Y":PAPER, "Z":SCISSORS}
Char2Result = {"X":LOSS, "Y":DRAW, "Z":WIN}

# Truth tables
scoreFromShape  = [DRAW, LOSS, WIN,   WIN, DRAW, LOSS,   LOSS, WIN, DRAW]
shapeFromResult = [SCISSORS, ROCK, PAPER,   ROCK,PAPER, SCISSORS,   PAPER, SCISSORS, ROCK]

score1 = 0  # For part 1
score2 = 0  # For part 2

for round in data:

    elf, me     = round.split()  # For part 1
    elf, result = round.split()  # For part 2

    me     = Char2Shape[me]
    elf    = Char2Shape[elf]
    result = Char2Result[result]

    score1 += me+1
    score1 += scoreFromShape [me*3+elf]

    me = shapeFromResult[result+elf]
    score2 += me+1
    score2 += scoreFromShape [me*3+elf]

print (score1) # For part 1
print (score2) # For part 2