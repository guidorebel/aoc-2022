
import os

class PuzzleData():

    def __init__(self, scriptfname:str) -> None:

        self.today = os.path.basename(scriptfname)
        self.today = self.today.replace(".py", "")

        self.scriptdir = os.path.dirname(scriptfname)


    def getData(self):

        datafile = self.today
        datafile += ".txt"

        datafile = os.path.join (self.scriptdir, "..\\input\\", datafile)
        datafile = os.path.abspath (datafile)

        data = []
        with open (datafile, "r") as f:
            data = f.read()
        return data


    def getStrList(self):

        data=self.getData()
        return data.split("\n")


    def getIntGrid(self):

        data = self.getData()
        data = data.split("\n")

        grid = []
        for line in data: grid.append([int(i) for i in line])
        return grid

