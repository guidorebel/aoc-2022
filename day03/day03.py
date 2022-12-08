
from aoc import PuzzleData

puzzle = PuzzleData(__file__)
data = puzzle.getStrList()


total = 0

for rucksack in data:

    compartmentItems = int(len(rucksack)/2)
    c1 = rucksack[:compartmentItems]
    c2 = rucksack[compartmentItems:]

    item = None
    for c in c1:
        if c in c2:
            item = c
            break
    
    if item:
        if item.isupper(): score = ord(item)-ord("A")+27
        else:              score = ord(item)-ord("a")+1

    total += score
    print (f"{item} : {score} -> {total}")


print("")


total=0

nRucksack = int(len(data)/3)

for i in range(nRucksack):

    r1 = data[i*3+0]
    r2 = data[i*3+1]
    r3 = data[i*3+2]

    item = None
    for c in r1:
        if c in r2:
            if c in r3:
                item = c
                break
        
    if item:
        if item.isupper(): score = ord(item)-ord("A")+27
        else:              score = ord(item)-ord("a")+1

    total += score
    print (f"{item} : {score} -> {total}")

