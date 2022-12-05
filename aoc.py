
import os

class PuzzleData():

    def __init__(self, scriptfname:str) -> None:

        self.today = os.path.basename(scriptfname)
        self.today = self.today.replace(".py", "")

        self.dirname = os.path.dirname(scriptfname)


    def rawdata(self, exampleData = False):

        datafile = self.today
        if exampleData: datafile += "-example"
        datafile += ".txt"

        datafile = os.path.join (self.dirname, "..\\input\\", datafile)
        datafile = os.path.abspath(datafile)

        data=[]
        with open(datafile, "r") as f:
            for line in f.readlines():
                data.append(line.replace("\n",""))
        return data