

class Puzzle(object):


    def __init__(self, day) -> None:
        
        self.day = day
        self.input = f"..\\input\\{self.day}.txt"



    def rawdata(self):

        data=[]

        with open(self.input, "r") as f:
            for line in f.readlines():
                data.append(line.strip())
        
        return data

