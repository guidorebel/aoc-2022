
from aoc import PuzzleData


class CRT:

    width: int = 40
    display: str = ""

    def __repr__(self) -> str:
        return self.display

    def draw(self, register):

        for cycle, x in register.items():
        
            if (cycle-1) % self.width == 0: self.display += "\n"
            self.display += "■" if x-1 <= (cycle-1) % self.width <= x+1 else " "


class CPU:

    x: int = 1
    cycle: int = 1
    signal: dict[int, int] = {}
    register: dict[int, int] = {}

    def __repr__(self) -> str:
        return str(sum([self.signal[v] for v in [20,60, 100, 140, 180, 220]]))

    def noop(self):

        self.signal[self.cycle] = self.x * self.cycle
        self.register[self.cycle] = self.x
        self.cycle += 1

    def addx(self, value):

        self.noop()
        self.noop()        
        self.x += int(value)

    def process(self, data):

        for line in data:
            match line.split(" "):
                case ["noop"]: self.noop() 
                case ["addx", value]: self.addx(value)


class Handheld():

    cpu = CPU()
    crt = CRT()

    def startup(self):

        puzzle = PuzzleData(__file__)
        data = puzzle.getStrList()

        self.cpu.process(data)
        self.crt.draw(self.cpu.register)

        print (self.cpu)
        print (self.crt)


h = Handheld()
h.startup()