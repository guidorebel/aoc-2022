
from aoc import PuzzleData
from math import sqrt
from collections import defaultdict

puzzle = PuzzleData(__file__)
data = puzzle.getStrList()


class Knot:

    x: int
    y: int
    id: int 

    def __init__(self, x, y, id) -> None:

        self.x = x
        self.y = y
        self.id = id


    def __repr__(self) -> str:
        
        return f"Knot ({self.id}) at pos ({self.x},{self.y})"


    def move(self, direction: str) -> None:

        match direction:
            case 'R': self.x += 1 
            case 'L': self.x -= 1 
            case 'U': self.y += 1
            case 'D': self.y -= 1 


    def follow(self, other: "Knot") -> None:
        
        dx = other.x - self.x 
        dy = other.y - self.y 
       
        if abs(dx) <= 1 and abs(dy) <= 1:   # No need to move if we are touching other
            pass 

        elif dx == 0:                       # Move vertically
            if   dy >  1: self.y += 1
            elif dy < -1: self.y -= 1 

        elif dy == 0:                       # Move horizontally
            if   dx >  1: self.x += 1
            elif dx < -1: self.x -= 1
        
        else:                               # Move diagonally
            if   dy > 0: self.y += 1
            elif dy < 0: self.y -= 1 
            
            if   dx > 0: self.x += 1
            elif dx < 0: self.x -= 1


    def position(self) -> tuple[int, int]:

        return (self.x, self.y)



def processData (data: list[str], ropeLength: int) -> int:
    
    # Create a list of Knots to form the rope
    knots = [Knot(0, 0, i) for i in range(0, ropeLength)]
    tailPositions = set()

    for line in data:

        direction, steps = line.split()

        for step in range(int(steps)):
            
            # Update head position
            knots[0].move(direction)

            # All other knots follow the head.
            # Create a zip from start to end / start+1 to end
            # This will yield tuples of knots that are adjecent to each other.
            for a, b in zip(knots, knots[1:]):
                b.follow(a) 
          
            tailPositions.add(b.position())

    return len(tailPositions)


print(processData(data, 2))
print(processData(data, 10))
