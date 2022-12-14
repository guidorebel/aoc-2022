
from aoc import PuzzleData
from collections import defaultdict
from math import inf


ROCK = 1
SAND = 2


class Cave():

    def __init__(self) -> None:
        
        self.world: dict = defaultdict (int)
        self.max_y = 0
        self.floor_y = inf

    def buildWorld (self, floor: bool = False) -> None:

        # Get the data
        puzzle = PuzzleData(__file__)
        data = puzzle.getStrList()

        for line in data:
            
            coords = line.split (" -> ")
            
            i = 0
            while i < len(coords)-1:

                s_x, s_y = [int(k) for k in coords[i].split(",")]
                e_x, e_y = [int(k) for k in coords[i+1].split(",")]

                self.max_y = max(self.max_y, s_y, e_y)

                self.world[(s_x, s_y)] = ROCK
                self.world[(e_x, e_y)] = ROCK

                if s_x == e_x:
                    for j in range(s_y, e_y, 1 if s_y < e_y else -1):
                        self.world[(s_x, j)] = ROCK

                elif s_y == e_y:
                    for j in range(s_x, e_x, 1 if s_x < e_x else -1):
                        self.world[(j, s_y)] = ROCK

                i+=1


        if floor:
            self.floor_y = self.max_y + 2
            self.max_y = inf


    def pourSand(self) -> int:
        
        drops = 0

        while True:
            if self.dropSand(500, 0) == False:  break
            else:                               drops+=1

        return drops


    def dropSand(self, pos_x, pos_y):

        # Is the start position already occupied? Then break recursion with False
        if (pos_x, pos_y) in self.world:
            return False

        old_x = pos_x
        old_y = pos_y

        # Drop down
        if not (pos_x, pos_y+1) in self.world and pos_y+1 < self.floor_y:
            pos_y+=1
        
        # Drop left and down
        elif not (pos_x-1, pos_y+1) in self.world and pos_y+1 < self.floor_y:
            pos_x-=1
            pos_y+=1

        # Drop right and down
        elif not (pos_x+1, pos_y+1) in self.world and pos_y+1 < self.floor_y:
            pos_x+=1
            pos_y+=1

        # Exceeding the max y? Then break recursion with False
        if pos_y > self.max_y:
            return False

        # Come to rest? The break recursion with True
        if old_x == pos_x and old_y == pos_y:
            self.world[(pos_x, pos_y)] == SAND
            return True

        # Continue dopping
        return self.dropSand(pos_x, pos_y)


cave = Cave()
cave.buildWorld()
print (cave.pourSand())

cave = Cave()
cave.buildWorld(True)
print (cave.pourSand())

