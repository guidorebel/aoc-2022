
import os

# The PuzzleData is a dataclass
# See https://www.pythontutorial.net/python-oop/python-dataclass/
from dataclasses import dataclass


@dataclass
class PuzzleData:

    scriptfname: str
    
    """
    Puzzle data class for Advent of Code

    Create the data class with a reference to the script file (for example, use PuzzleData(___file___)).
    The data file is expected with the same basename but the extention .txt and in the folder ..\input.
    For example: a reference to \day05\day05.py will expect the data file in \input\day05.txt.
    """

    def __post_init__(self) -> None:

        self.today: str
        self.today = os.path.basename(self.scriptfname)
        self.today = self.today.replace(".py", "")

        self.scriptdir: str
        self.scriptdir = os.path.dirname(self.scriptfname)

        self.datafile: str
        self.datafile = self.today+".txt"
        self.datafile = os.path.join (self.scriptdir, "..\\input\\", self.datafile)
        self.datafile = os.path.abspath (self.datafile)


    def __repr__(self) -> str:

        return f"{self.__class__.__name__} - {self.today}"


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


    def getStrGrid(self) -> list[list[str]]:

        """
        Get the data as a grid (list of lists) of characters.
        """

        data = self.getData()
        datalist = data.split("\n")

        grid = []
        for line in datalist: grid.append([i for i in line])
        return grid


    def getIntList(self) -> list[int]:

        """
        Get the data as a list of integers.
        Each line in the data file is an item in the list.
        """

        data=self.getData()
        return [int(i) for i in data.split("\n")]


    def getIntGrid(self) -> list[list[int]]:

        """
        Get the data as a grid (list of lists) of integers.
        """

        data = self.getData()
        datalist = data.split("\n")

        grid = []
        for line in datalist: grid.append([int(i) for i in line])
        return grid

