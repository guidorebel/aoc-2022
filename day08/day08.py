
from aoc import PuzzleData

puzzle = PuzzleData(__file__)
data: list[list[int]] = puzzle.getIntGrid()

rowMax: int = len(data)
colMax: int = len(data[0])


def isTreeVisible(row: int, col: int) -> bool:

	tree: int = data[row][col]

	# Check all trees in upward direction
	for i in range(row - 1, -1, -1):
		if data[i][col] >= tree:
			break
	else:
		return True
	
	# Check all trees in downward direction
	for i in range(row + 1, len(data), 1):
		if data[i][col] >= tree:
			break
	else:
		return True
		
	# Check all trees to the left
	for neighbour in data[row][:col]:
		if neighbour >= tree:
			break
	else:
		return True
	
	# Check all trees to the right
	for neighbour in data[row][col + 1:]:
		if neighbour >= tree:
			break	
	else:
		return True	
	
	return False



def scenicScore (row: int, col: int) -> int:

    tree: int = data[row][col]
	
    up: int = 0
    down: int = 0
    left: int = 0
    right: int = 0
	
	# Check all trees in upward direction
    for i in range(row - 1, -1, -1):
        up += 1
        if data[i][col] >= tree:
            break
	
	# Check all trees in downward direction
    for i in range(row + 1, len(data)):
        down += 1
        if data[i][col] >= tree:
            break
		
	# Check all trees to the left
    for neighbour in reversed(data[row][:col]):
        left += 1
        if neighbour >= tree:
            break

	# Check all trees to the right
    for neighbour in data[row][col + 1:]:
        right += 1
        if neighbour >= tree:
            break	

    return up * down * right * left


#-----------------------------------------------------------------

# All outer trees are visible
visibleTrees: int = rowMax*2 + colMax*2 - 4

# All outer trees have a scenic score of 0
maxScenicScore: int = 0

# Check all inner trees
for row in range(1, rowMax - 1):
    for col in range(1, colMax - 1):

        # Part 1
        if isTreeVisible(row, col): visibleTrees += 1

        # Part 2
        maxScenicScore = max(scenicScore(row, col), maxScenicScore)


print(visibleTrees)
print(maxScenicScore)
