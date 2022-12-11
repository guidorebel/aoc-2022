
from aoc import PuzzleData

import math


class Monkey:

    def __init__(self, data) -> None:

        self.id: str = data.replace(":", "")
        self.throws: int = 0

        self.items: list[int] = []
        self.operation: str = ""
        self.test: int = -1
        self.testTrue: int = -1
        self.testFalse: int = -1


    def __repr__(self) -> str:
        return self.id


    def init(self, data: list[str]) -> None:

        for line in data:
            line = line.strip()
            if line.find("Starting items:")==0:
                self.items = [int(i) for i in line.split(": ")[1].split(", ")]
            elif line.find("Operation: new = old") == 0:
                self.operation = line[21::]
            elif line.find("Test: divisible by")==0:
                self.test = int(line[19::])
            elif line.find("If true:")==0:
                self.testTrue = int(line[-1])
            elif line.find("If false:")==0:
                self.testFalse = int(line[-1])


    def trowItem(self, item, monkey, monkeys):
        monkeys[monkey].catchItem(item)


    def catchItem(self, item):
        self.items.append(item)


    def taketurn(self, monkeys, divFactor, modFactor):

        for item in self.items:

            evaluate = item

            # Do the operation with the specified operator and value
            if   self.operation == "* old": evaluate *= evaluate
            elif self.operation[0] == "*": evaluate *= int(self.operation[2::])
            elif self.operation[0] == "+": evaluate += int(self.operation[2::])

            # Divide by the specified value
            evaluate = int(evaluate / divFactor)
            
            # Take the modulo of the specified value
            # I had to lookup this trick on Reddit to know how to proceed...
            # When we do the modulo with self.text, we can already do a mudulo with 
            # the 'least common multiple' of all self.test values for all monkeys:
            # it will not affect the result!
            if modFactor: evaluate = evaluate % modFactor

            # Take the modulo of the test factor, and throw result to another monkey
            if evaluate % self.test == 0: self.trowItem(evaluate, self.testTrue, monkeys)
            else:                         self.trowItem(evaluate, self.testFalse, monkeys)

            # Increase nr of throws
            self.throws += 1

        self.items.clear()



class Game:

    def __init__(self) -> None:
        self.monkeys: list[Monkey] = []


    def init(self, data, worryDivFactor):

        # Create the list with monkeys
        i: int = 0
        while i < len(data):
            line = data[i]
            if line.find("Monkey")==0:
                monkey = Monkey(line)
                monkey.init(data[i+1:i+6])
                self.monkeys.append(monkey)
                i+=7

       # Store the worry division factor
        self.worryDivFactor = worryDivFactor
 
        # The worry modulo factor ('least common multiple') only applies if the devision factor equals 1
        self.worryModFactor = math.lcm(*[monkey.test for monkey in self.monkeys]) if self.worryDivFactor == 1 else 0
        

    def playRounds(self, rounds):

        for i in range(rounds):
            for monkey in self.monkeys:
                monkey.taketurn(self.monkeys, self.worryDivFactor, self.worryModFactor)


    def report(self):

        throws = []
        for monkey in self.monkeys:
            throws.append(monkey.throws)
        throws.sort(reverse=True)
        return math.prod(throws[0:2])



puzzle = PuzzleData(__file__)
data = puzzle.getStrList()

# Part 1
game = Game()
game.init(data, 3)
game.playRounds(20)
print (game.report())

# Part 2
game = Game()
game.init(data, 1)
game.playRounds(10000)
print (game.report())

