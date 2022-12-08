
from aoc import PuzzleData

puzzle = PuzzleData(__file__)
data = puzzle.getStrList()

count1 = 0
count2 = 0

for assignment in data:

    c1, c2 = assignment.split(",")
    c1start, c1stop = [int(i) for i in c1.split("-")]
    c2start, c2stop = [int(i) for i in c2.split("-")]
    
    if c1start <= c2start <= c1stop and c1start <= c2stop <= c1stop:
        count1+=1
    elif c2start <= c1start <= c2stop and c2start <= c1stop <= c2stop:
        count1+=1

    if c1start <= c2start <= c1stop or c1start <= c2stop <= c1stop:
        count2+=1
    elif c2start <= c1start <= c2stop or c2start <= c1stop <= c2stop:
        count2+=1

print (count1)
print (count2)
