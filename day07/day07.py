
from aoc import PuzzleData
from typing import Any, Optional

puzzle = PuzzleData(__file__)
data = puzzle.getStrList()


class Directory():

    def __init__(self, parent: "Directory" | None) -> None: 

        self.parent: Directory | None = parent

        self.size: int = 0
        self.files: dict = {}
        self.dirs: dict = {}


    def addFile(self, name: str, size: int) -> None:
        self.files[name] = size
        self.size += size
        
        parent = self.parent
        while parent:
            parent.size += size
            parent = parent.parent


def parseInstructions(data: list[str]) -> Directory:

    filesystem = Directory(None)

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


def getDirToDeleteSize(dir: Directory, target: int) -> Any:

    size = None

    if dir.size > target:

        size = dir.size

        for name, subdir in dir.dirs.items():
            subdirsize = getDirToDeleteSize(subdir, target)
            if subdirsize: size = min(size, subdirsize)

    return size


filesystem: Directory = parseInstructions(data)

# Part 1
print (getDirSize (filesystem, 100000))

# Part 2
target = 30000000 - (70000000 - filesystem.size)
print (getDirToDeleteSize(filesystem, target))
