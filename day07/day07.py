
from aoc import PuzzleData

puzzle = PuzzleData(__file__)
data = puzzle.rawdata()


class Directory():

    def __init__(self, parent = None):

        self.parent = parent

        self.size = 0
        self.files = {}
        self.dirs = {}


    def addFile(self, name, size):
        self.files[name] = size
        self.size += size
        
        parent = self.parent
        while parent:
            parent.size += size
            parent = parent.parent


def parseInstructions(data) -> Directory:

    filesystem = Directory()

    cwd = filesystem

    for line in data:
        match line.split():
            case ["$", "ls"]:
                pass # nothing to do here
            case ["$", "cd", "/"]:
                cwd = filesystem
            case ["$", "cd", ".."]:
                cwd = cwd.parent
            case ["$", "cd", name]:
                cwd = cwd.dirs[name]
            case ["dir", name]:
                cwd.dirs[name] = Directory(cwd)
            case [size, name]:
                cwd.addFile(name, int(size))
            case _:
                print ("now what?")

    return filesystem


def getDirSize(dir: Directory, limit: int) -> int:

    total = dir.size if dir.size <= limit else 0

    for name, subdir in dir.dirs.items():
        total += getDirSize(subdir, limit)

    return total


def getDirToDeleteSize(dir: Directory, target: int) -> int:

    size = None

    if dir.size > target:

        size = dir.size

        for name, subdir in dir.dirs.items():
            subdirsize = getDirToDeleteSize(subdir, target)
            if subdirsize: size = min(size, subdirsize)

    return size


filesystem = parseInstructions(data)

# Part 1
print (getDirSize (filesystem, 100000))

# Part 2
target = 30000000 - (70000000 - filesystem.size)
print (getDirToDeleteSize(filesystem, target))
