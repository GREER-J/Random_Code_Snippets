'''
Minesweeper

Cell
    Location
    State
    Revealed
    Neighbours
    Count
'''
class cell:
    def __init__(self, location, mine, revealed = False):
        self.location = location
        self.mine = mine
        self.revealed = revealed

    def display(self):
        return(self.location, self.mine, self.revealed)

def generateboard(maxX=11, maxY=11, mines=10):
    board = []
    for x in range(maxX):
        x = []
        for y in range(maxY):
            x.append(y)



