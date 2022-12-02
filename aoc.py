

class PuzzleData():

    def __init__(self, day, example=False) -> None:
        
        self.day = day

        datafile = day
        if example: datafile+="example"
        self.input = f"input\\{datafile}.txt"

        
    def rawdata(self):

        data=[]

        with open(self.input, "r") as f:
            for line in f.readlines():
                data.append(line.strip())
        
        return data

