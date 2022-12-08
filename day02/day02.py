
from aoc import PuzzleData

puzzle = PuzzleData(__file__)
data = puzzle.getStrList()

ROCK, PAPER, SCISSORS = [1, 2, 3]
LOSS, DRAW, WIN       = [0, 3, 6]

Char2Shape  = {"A":ROCK, "B":PAPER, "C":SCISSORS, "X":ROCK, "Y":PAPER, "Z":SCISSORS}
Char2Result = {"X":LOSS, "Y":DRAW, "Z":WIN}


class RockPaperScissors (object):


    def MyScoreFromShape(self, other:int, me:int) -> int:

        if   other == me:                          return DRAW
        elif other == ROCK     and me == PAPER:    return WIN
        elif other == ROCK     and me == SCISSORS: return LOSS
        elif other == PAPER    and me == ROCK:     return LOSS
        elif other == PAPER    and me == SCISSORS: return WIN
        elif other == SCISSORS and me == ROCK:     return WIN
        elif other == SCISSORS and me == PAPER:    return LOSS
        else:                                      return -1
        
    def MyShapeFromResult(self, other:int, result:int) -> int:

        if   result == DRAW:        me = other
        elif result == WIN:
            if   other == ROCK:     me = PAPER
            elif other == PAPER:    me = SCISSORS
            elif other == SCISSORS: me = ROCK
        elif result == LOSS:
            if   other == ROCK:     me = SCISSORS
            elif other == PAPER:    me = ROCK
            elif other == SCISSORS: me = PAPER

        return me


rps = RockPaperScissors()

score1 = 0
score2 = 0

for round in data:

    elf, me     = round.split()  # For part 1
    elf, result = round.split()  # For part 2

    me     = Char2Shape[me]
    elf    = Char2Shape[elf]
    result = Char2Result[result]

    score1 += me
    score1 += rps.MyScoreFromShape (elf, me)

    me = rps.MyShapeFromResult (elf, result)
    score2 += me
    score2 += rps.MyScoreFromShape (elf, me)


print (score1) # For part 1
print (score2) # For part 2