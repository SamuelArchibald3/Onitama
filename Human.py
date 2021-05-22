from Player import Player


class Human(Player):
    def getMove(self,board,myCards,oppCards,middleCard):
        def flip(b):
            new = []
            for i in range(4, -1, -1):
                new.append(b[i][::-1])
            return new
        def toCoords(square):
            col = ord(square[0].lower()) - ord('a')
            row = 5 - int(square[1])
            return [row,col]
        def islegal(move,card):
            start = toCoords(move[:2])
            end = toCoords(move[3:])
            # check that start and end are on the board
            # check that my piece is on start square
            # check that move is one of the card's moves
            # check that ending square is not my piece
            if all(map(lambda x: x in range(5),start+end)) and\
                board[start[0]][start[1]].upper() == self.side and\
                board[end[0]][end[1]].upper() != self.side and\
                [end[1]-start[1],end[0]-start[0]] in card.moves:
                return True
            else:
                return False
        if self.side == "O":
            board = flip(board)
        for c in oppCards:
            print(c)
        print(middleCard)
        for row in board:
            print(row)
        for c in myCards:
            print(c)
        cardName,move = input("Type the card you'd like to play and the move you'd like to make: ").split(" ")
        while True:
            if cardName.upper() in map(lambda x: x.name, myCards):
                card = [c for c in myCards if c.name == cardName.upper()][0]
                if islegal(move,card):
                    break
            cardName,move = input("Type the card you'd like to play and the move you'd like to make: ").split(" ")

        for i in range(2):
            if myCards[i].name == cardName.upper():
                index = i
            i += 1
        middleCard,myCards[index] = myCards[index],middleCard
        start = toCoords(move[:2])
        end = toCoords(move[3:])
        board[end[0]][end[1]] = board[start[0]][start[1]]
        board[start[0]][start[1]] = " "
        if self.side == "O":
            board = flip(board)
        return [board,myCards,oppCards,middleCard]


