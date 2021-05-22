from Player import Player
import random

class Computer(Player):
    def __init__(self,side,depth):
        self.side = side
        self.depth = depth

    def getMove(self,board,myCards,oppCards,middleCard): #returns Card, [piece,x,y], [x,y]
        def islegal(start, end):

            if all(map(lambda x: x in range(5), start + end)) and \
                    board[start[1]][start[0]].upper() == self.side and \
                    board[end[1]][end[0]].upper() != self.side:
                return True
            else:
                return False
        def findPieces(board):
            r = 0
            pieces = []
            for row in board:
                indices = [[x,i] for i, x in enumerate(row) if x.upper() == self.side]
                for x,i in indices:
                    pieces.append([x, i, r])
                r += 1
            return pieces
        myPieces = findPieces(board)
        possible_moves = []
        for piece in myPieces:
            for card in myCards:
                if self.side == "B":
                    moves = [[-1*x[0],-1*x[1]] for x in card.moves]
                else:
                    moves = card.moves
                for move in moves:
                    start = piece[1:]
                    end = [start[0] + move[0], start[1] + move[1]]
                    if islegal(start,end):
                        possible_moves.append([card,piece,end])
        print(possible_moves)
        return random.choice(possible_moves)
