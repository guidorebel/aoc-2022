
from aoc import PuzzleData

puzzle = PuzzleData(__file__)
data = puzzle.rawdata()

    
class Directory():

    def __init__(self, name) -> None:
        self.name = name
        self.dirList = []
        self.fileList = []

    def getsize(self):
        size = 0
        size += sum([item.getsize() for item in self.fileList])
        size += sum([item.getsize() for item in self.dirList])
        return size


class File():
    def __init__(self, name:str, size:int) -> None:
        self.name = name
        self.size = size

    def getsize(self):
        return self.size


def parseConsoleOutput(curdir:Directory, index:int):

    while True:

        index+=1
        if index >= len (data): break

        line = data[index]

        if   line.find ("dir") == 0: pass     # This is a reference to a dir in the current dir, ignore it
        elif line.find ("$ ls") == 0: pass    # This is a reference to a dir in the current dir, ignore it
        elif line.find("$ cd ..") == 0: break # This is a command to go one level up, break out of the recursion
        elif line.find("$ cd ") == 0:         # This is a command to go into a directory, enter recursion
     
            name = line.replace("$ cd ", "")
            newdir = Directory(name)
            curdir.dirList.append(newdir)
            index = parseConsoleOutput(newdir, index)

        else:                                 # This must be a file reference

            size, name = line.split(" ")
            size = int(size)
            newfile = File(name, size)
            curdir.fileList.append(newfile)

    return index


def printFileSystem(curdir:Directory, level:int):
    
    dirsize = 0
    answer = 0

    indent = level*" "
    for dir in curdir.dirList:
        print (f"{indent}- {dir.name} (dir)")
        d, a = printFileSystem(dir,level+1)
        dirsize += d
        answer += a

    for file in curdir.fileList:
        print (f"{indent}- {file.name} (file, size={file.size})")
        dirsize += file.size

    if dirsize < 100000:
        answer += dirsize

    return dirsize, answer


def findDir (curdir:Directory, needed, answer):

    dirsize = 0

    for dir in curdir.dirList:
        d, answer = findDir(dir, needed, answer)
        dirsize += d

    for file in curdir.fileList:
        dirsize += file.size

    if dirsize >= needed and dirsize < answer:
        answer = dirsize

    return dirsize, answer


root = Directory("/")
index = 0

parseConsoleOutput(root, index)

d, a = printFileSystem(root, 0)

print (a)

total = 70000000
used = d
available = total - used
required = 30000000
needed = required - available

d, a = findDir(root, needed, total)
print (a)
