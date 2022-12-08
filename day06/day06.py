
from aoc import PuzzleData

puzzle = PuzzleData(__file__)
data = puzzle.getData()

def findFirstMarker (data, length):

    marker = None
    i = 0

    while i < len(data)-length:

        chunk = data [i:i+length]   # Get a chunk from the data
        chunk = "".join(set(chunk)) # Remove all duplicate characters

        if len(chunk) == length:
            marker = i+length
            break

        i+=1

    return marker
    
print (findFirstMarker (data, 4))   # Part 1
print (findFirstMarker (data, 14))  # Part 2
