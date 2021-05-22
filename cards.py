Names = ["RABBIT", "ROOSTER", "CRANE", "GOOSE", "BOAR", "OX", "MONKEY", "ELEPHANT", "DRAGON", "CRAB", "FROG", "EEL", "COBRA", "TIGER", "MANTIS", "HORSE"]
Colors = ["B", "R", "B", "B", "R", "B", "B", "R", "R", "B", "R", "B", "R", "B", "R", "R"]
Shapes = [["     ",
           "   X ",
           "  O X",
           " X   ",
           "     "],
          ["     ",
           "   X ",
           " XOX ",
           " X   ",
           "     "],
          ["     ",
           "  X  ",
           "  O  ",
           " X X ",
           "     "],
          ["     ",
           " X   ",
           " XOX ",
           "   X ",
           "     "],
          ["     ",
           "  X  ",
           " XOX ",
           "     ",
           "     "],
          ["     ",
           "  X  ",
           "  OX ",
           "  X  ",
           "     "],
          ["     ",
           " X X ",
           "  O  ",
           " X X ",
           "     "],
          ["     ",
           " X X ",
           " XOX ",
           "     ",
           "     "],
          ["     ",
           "X   X",
           "  O  ",
           " X X ",
           "     "],
          ["     ",
           "  X  ",
           "X O X",
           "     ",
           "     "],
          ["     ",
           " X   ",
           "X O  ",
           "   X ",
           "     "],
          ["     ",
           " X   ",
           "  OX ",
           " X   ",
           "     "],
          ["     ",
           "   X ",
           " XO  ",
           "   X ",
           "     "],
          ["  X  ",
           "     ",
           "  O  ",
           "  X  ",
           "     "],
          ["     ",
           " X X ",
           "  O  ",
           "  X  ",
           "     "],
          ["     ",
           "  X  ",
           " XO  ",
           "  X  ",
           "     "],
          ]

class Card:
    def __init__(self,name,color,shape):
        self.name = name
        self.color = color
        self.shape = shape
        self.moves = []
        r = -2
        for row in shape:
            indices = [i for i, x in enumerate(row) if x == "X"]
            for i in indices:
                self.moves.append([i-2,r])
            r += 1
    def __repr__(self):
        return self.name
cardlist = []

for i in range(16):
    cardlist.append(Card(Names[i], Colors[i], Shapes[i]))
