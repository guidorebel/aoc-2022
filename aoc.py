
import os
import math


class PuzzleData:

    """ Puzzle data class for Advent of Code """

    def __init__(self, scriptfname:str) -> None:

        """
        Create the data class with a reference to the script file (for example, use ___file___).
        The data file is expected with the same basename but the extention .txt and in the folder ..\input.
        For example: a reference to \day05\day05.py will expect the data file in \input\day05.txt.
        """

        self.today: str
        self.today = os.path.basename(scriptfname)
        self.today = self.today.replace(".py", "")

        self.scriptdir: str
        self.scriptdir = os.path.dirname(scriptfname)

        self.datafile: str
        self.datafile = self.today+".txt"
        self.datafile = os.path.join (self.scriptdir, "..\\input\\", self.datafile)
        self.datafile = os.path.abspath (self.datafile)


    def getData(self) -> str:

        """
        Get the raw data from the file.
        """

        data: str = ""
        with open (self.datafile, "r") as f:
            data = f.read()
        return data


    def getStrList(self) -> list[str]:

        """
        Get the data as a list of strings.
        Each line in the data file is an item in the list.
        """

        data=self.getData()
        return data.split("\n")


    def getIntGrid(self) -> list[list[int]]:

        """
        Get the data as a grid (list of lists) of integers.
        """

        data = self.getData()
        datalist = data.split("\n")

        grid = []
        for line in datalist: grid.append([int(i) for i in line])
        return grid

