
from aoc import PuzzleData
import math

# Implemention of a Breadth First Search algorithm
# Based on information from:
# https://favtutor.com/blogs/breadth-first-search-python
# https://www.redblobgames.com/pathfinding/a-star/introduction.html
# https://stackabuse.com/courses/graphs-in-python-theory-and-implementation/lessons/breadth-first-search-bfs-algorithm/


class HeightMap:

    def __init__(self) -> None:

        # Get the data
        puzzle = PuzzleData(__file__)        
        grid = puzzle.getStrGrid()
        grid_rows = len(grid)
        grid_cols = len(grid[0])

        # List of candiates for the start of the scenic tour.
        self.scenicStartPoints = []

        # Find the start and end positions. Afterwards,
        # change the 'S' and 'E' values in the grid to 'a' and 'z' 
        for r in range(grid_rows):
            for c in range(grid_cols):

                if grid[r][c] == "S":
                    self.start = (r,c)
                    grid[r][c] = "a"

                if grid[r][c] == "E":
                    self.end = (r,c)
                    grid[r][c] = "z"

                if grid[r][c] == "a":
                    self.scenicStartPoints.append((r,c))

        # Setup the graph for the BSF algorith.
        # This will tell how we can move arround between positions. 
        # The graph is a dictionary from coordinate (int, int) to a list of coordinates (int, int)
        self.graph: dict[tuple[int,int], list[tuple[int, int]]] = {}

        for r in range(grid_rows):
            for c in range(grid_cols):

                # Start with an empty list
                self.graph[(r,c)] = []

                # Can we go north, south, west, or east?
                if r-1 >= 0        and self.canClimb(grid[r][c], grid[r-1][c]):  self.graph[(r,c)].append((r-1,c))
                if r+1 < grid_rows and self.canClimb(grid[r][c], grid[r+1][c]):  self.graph[(r,c)].append((r+1,c))
                if c-1 >= 0        and self.canClimb(grid[r][c], grid[r][c-1]):  self.graph[(r,c)].append((r,c-1))
                if c+1 < grid_cols and self.canClimb(grid[r][c], grid[r][c+1]):  self.graph[(r,c)].append((r,c+1))


    # Helper function to determine if we can climb from one position to another
    def canClimb(self, valueFrom: str, valueTo: str) -> bool:
        return True if ord(valueTo) - ord(valueFrom) <= 1 else False



# The Breadth First Search (BFS) function
class BreadthFirstSearch:

    def search (self,
                graph: dict[tuple[int,int], list[tuple[int, int]]],
                start: tuple[int,int],
                end: tuple[int,int]):

        # List of visited positions 
        visited = []
        visited.append(start)

        # List of the front positions
        queue = []
        queue.append(start)

        # Keep track of the position where we came from (breadcrumbs)
        parent = {}
        parent[start] = None

        found = False
        while queue:
            
            # Get the next position from the queue
            position = queue.pop(0)

            # Break out of loop if this is the target destination
            if position == end:
                found = True
                break

            # Get all neigbors for this position.
            # If the neigbor was not visited yet, add it to the queue
            for neighbor in graph[position]:
                if neighbor not in visited:
                    visited.append(neighbor)
                    queue.append(neighbor)
                    parent[neighbor] = position

        # We have now visited all positions in the graph.
        path = []
        if found:

            # Start at the end, and follow the parents (breadcrumbs) back to the start.
            path.append(end)
            while parent[end] is not None:
                end = parent[end]
                path.append(end)

            # Reverse the path to have the positions from the start to the end.
            path.reverse()

        return path


map = HeightMap()
bfs = BreadthFirstSearch()

# Part 1.
# Search the map from start to end position.
# The nr of steps = positions - 1
path = bfs.search (map.graph, map.start, map.end)
print (len(path)-1)

# Part 2. Using brute force, will take a little while.
# Search the map from each candiate start position for the scenic tour to end position.
length = math.inf
for start in map.scenicStartPoints:
    path = bfs.search (map.graph, start, map.end)
    if len(path)-1 > -1: length = min (length, len(path)-1)
print (length) 
