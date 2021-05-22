from cards import cardlist
import pygame
import random
from Human import Human
from Computer import Computer



TILESIZE = 50
CARDHEIGHT = 75
CARDWIDTH = 75
BOARD_POS = (50, 125)
CARDGAP = 50
BLUECARD_POS = (75,25)
REDCARD_POS = (75, BOARD_POS[1] + 5*TILESIZE + 25)
MIDCARD_POS = (BOARD_POS[0] + 5*TILESIZE + 25, BOARD_POS[1] + (5/2)*TILESIZE - 1/2*CARDHEIGHT)
def dealCards():
    cards = random.sample(cardlist, 5)
    return [cards[:2],cards[2:4],cards[4]]

def gameOver(board):
    if board[0][2] == "R":
        return "Blue"
    elif board[4][2] == "B":
        return "Red"
    R = False
    B = False
    for row in board:
        if "R" in row:
            R = True
        if "B" in row:
            B = True
    if R and not B:
        return "Red"
    elif B and not R:
        return "Blue"
    else:
        return False




def create_board_surf():
    board_surf = pygame.Surface((TILESIZE*5, TILESIZE*5))
    dark = False
    for y in range(5):
        for x in range(5):
            if y == 0 and x == 2:
                rect = pygame.Rect(x * TILESIZE, y * TILESIZE, TILESIZE, TILESIZE)
                pygame.draw.rect(board_surf, pygame.Color('lightblue'), rect)
            elif y == 4 and x == 2:
                rect = pygame.Rect(x * TILESIZE, y * TILESIZE, TILESIZE, TILESIZE)
                pygame.draw.rect(board_surf, pygame.Color('pink'), rect)
            else:
                rect = pygame.Rect(x*TILESIZE, y*TILESIZE, TILESIZE, TILESIZE)
                pygame.draw.rect(board_surf, pygame.Color('white'), rect)

    for i in range(5):
        pygame.draw.line(board_surf, pygame.Color('black'), (i*TILESIZE, 0), (i*TILESIZE, TILESIZE*5))
        pygame.draw.line(board_surf, pygame.Color('black'), (0, i*TILESIZE), (TILESIZE*5, i*TILESIZE))
    pygame.draw.line(board_surf, pygame.Color('black'), (TILESIZE * 5-1, 0), (TILESIZE * 5-1, TILESIZE * 5))
    pygame.draw.line(board_surf, pygame.Color('black'), (0, TILESIZE * 5-1), (TILESIZE * 5, TILESIZE * 5-1))
    return board_surf

def create_board():
    board = []
    for y in range(5):
        board.append([])
        for x in range(5):
            board[y].append(" ")
    for x in range(5):
        if x == 2:
            board[0][x] = ('B')
        else:
            board[0][x] = ('b')
    for x in range(5):
        if x == 2:
            board[4][x] = ('R')
        else:
            board[4][x] = ('r')
    return board

def draw_pieces(screen, board):
    for y in range(5):
        for x in range(5):
            piece = board[y][x]
            if piece:
                king = False
                if piece.isupper():
                    king = True
                color = None
                if piece.lower() == "r":
                    color = pygame.Color('red')
                elif piece.lower() == "b":
                    color = pygame.Color('blue')
                xpos = BOARD_POS[0] + x * TILESIZE + 1
                ypos = BOARD_POS[1] + y * TILESIZE + 1
                if king:
                    pygame.draw.rect(screen, color, ((xpos + 9/25 * TILESIZE, ypos + 1/10 * TILESIZE), (7/25 * TILESIZE, 8/10 * TILESIZE)))
                    pygame.draw.rect(screen, color, ((xpos + 1/10 * TILESIZE, ypos + 9/25 * TILESIZE), (8/10 * TILESIZE, 7/25 * TILESIZE)))

                elif color:
                    pygame.draw.circle(screen, color, (xpos + TILESIZE/2, ypos + TILESIZE/2), TILESIZE/3)

def draw_cards(screen, redCards, blueCards, midCard):
    x,y = REDCARD_POS
    for card in redCards:
        img = pygame.image.load(r"C:\Users\samue\PycharmProjects\Onitama\OnitamaCards\\" + card.name.capitalize() + ".jpg")
        img = pygame.transform.smoothscale(img,(CARDWIDTH,CARDHEIGHT))
        screen.blit(img, (x, y))
        x += CARDGAP + CARDWIDTH
    x, y = BLUECARD_POS
    for card in blueCards:
        img = pygame.image.load(r"C:\Users\samue\PycharmProjects\Onitama\OnitamaCards\\" + card.name.capitalize() + ".jpg")
        img = pygame.transform.smoothscale(img, (CARDWIDTH, CARDHEIGHT))
        img = pygame.transform.flip(img,True,True)
        screen.blit(img, (x, y))
        x += CARDGAP + CARDWIDTH
    x,y = MIDCARD_POS
    img = pygame.image.load(r"C:\Users\samue\PycharmProjects\Onitama\OnitamaCards\\" + midCard.name.capitalize() + ".jpg")
    img = pygame.transform.smoothscale(img, (CARDWIDTH, CARDHEIGHT))
    screen.blit(img, (x, y))
    return
def draw_selected_card(screen, piece):
    if piece and piece in ["R1","B1","R2","B2","M"]:
        if piece == "B1":
            rect = (BLUECARD_POS[0], BLUECARD_POS[1], CARDWIDTH, CARDHEIGHT)
            pygame.draw.rect(screen, (0, 255, 0, 50), rect, 2)
        elif piece == "B2":
            rect = (BLUECARD_POS[0] + CARDWIDTH + CARDGAP, BLUECARD_POS[1], CARDWIDTH, CARDHEIGHT)
            pygame.draw.rect(screen, (0, 255, 0, 50), rect, 2)
        elif piece == "R1":
            rect = (REDCARD_POS[0], REDCARD_POS[1], CARDWIDTH, CARDHEIGHT)
            pygame.draw.rect(screen, (0, 255, 0, 50), rect, 2)
        elif piece == "R2":
            rect = (REDCARD_POS[0] + CARDWIDTH + CARDGAP, REDCARD_POS[1], CARDWIDTH, CARDHEIGHT)
            pygame.draw.rect(screen, (0, 255, 0, 50), rect, 2)
        elif piece == "M":
            rect = (MIDCARD_POS[0], MIDCARD_POS[1], CARDWIDTH, CARDHEIGHT)
            pygame.draw.rect(screen, (0, 255, 0, 50), rect, 2)
def draw_selector(screen, piece, x, y):
    if piece and piece in ["R1","B1","R2","B2","M"]:
        if piece == "B1":
            rect = (BLUECARD_POS[0], BLUECARD_POS[1], CARDWIDTH, CARDHEIGHT)
            pygame.draw.rect(screen, (255, 0, 0, 50), rect, 2)
        elif piece == "B2":
            rect = (BLUECARD_POS[0] + CARDWIDTH + CARDGAP, BLUECARD_POS[1], CARDWIDTH, CARDHEIGHT)
            pygame.draw.rect(screen, (255, 0, 0, 50), rect, 2)
        elif piece == "R1":
            rect = (REDCARD_POS[0], REDCARD_POS[1], CARDWIDTH, CARDHEIGHT)
            pygame.draw.rect(screen, (255, 0, 0, 50), rect, 2)
        elif piece == "R2":
            rect = (REDCARD_POS[0] + CARDWIDTH + CARDGAP, REDCARD_POS[1], CARDWIDTH, CARDHEIGHT)
            pygame.draw.rect(screen, (255, 0, 0, 50), rect, 2)
        elif piece == "M":
            rect = (MIDCARD_POS[0], MIDCARD_POS[1], CARDWIDTH, CARDHEIGHT)
            pygame.draw.rect(screen, (255, 0, 0, 50), rect, 2)
    elif x != None:
        rect = (BOARD_POS[0] + x * TILESIZE, BOARD_POS[1] + y * TILESIZE, TILESIZE, TILESIZE)
        pygame.draw.rect(screen, (255, 0, 0, 50), rect, 2)

def get_square_under_mouse(board):
    mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
    x,y = mouse_pos
    if y < BOARD_POS[1]:
        if BLUECARD_POS[1] <= y <= BLUECARD_POS[1] + CARDHEIGHT:
            if BLUECARD_POS[0] <= x <= BLUECARD_POS[0] + CARDWIDTH:
                return "B1", None, None
            elif BLUECARD_POS[0] + CARDWIDTH + CARDGAP <= x <= BLUECARD_POS[0] + 2*CARDWIDTH + 50:
                return "B2", None, None
            else:
                return None, None, None
        else:
            return None, None, None
    elif y > BOARD_POS[1] + 5*TILESIZE:
        if REDCARD_POS[1] <= y <= REDCARD_POS[1] + CARDHEIGHT:
            if REDCARD_POS[0] <= x <= REDCARD_POS[0] + CARDWIDTH:
                return "R1", None, None
            elif REDCARD_POS[0] + CARDWIDTH + CARDGAP <= x <= REDCARD_POS[0] + 2 * CARDWIDTH + 50:
                return "R2", None, None
            else:
                return None, None, None
        else:
            return None, None, None
    elif x > BOARD_POS[0] + 5*TILESIZE:

        if MIDCARD_POS[0] <= x <= MIDCARD_POS[0] + CARDWIDTH:
            if MIDCARD_POS[1] <= y <= MIDCARD_POS[1] + CARDHEIGHT:
                return "M", None, None
            else:
                return None, None, None
        else:
            return None, None, None
    else:
        bx, by = int((x-BOARD_POS[0])//TILESIZE), int((y-BOARD_POS[1])//TILESIZE)
        try:
            if bx >= 0 and by >= 0:
                return board[by][bx], bx, by
        except IndexError:
            print("ERROR")
            return None, None, None
    return None, None, None

def draw_drag(screen, board, selected_piece):
    if selected_piece:
        piece, x, y = get_square_under_mouse(board)
        if x != None and y != None:
            rect = (BOARD_POS[0] + x * TILESIZE, BOARD_POS[1] + y * TILESIZE, TILESIZE, TILESIZE)
            pygame.draw.rect(screen, (0, 255, 0, 50), rect, 2)
            king = False
            piecename = selected_piece[0]
            if not isinstance(piecename,str):
                return (x, y)
            if piecename.isupper():
                king = True
            color = None
            if piecename.lower() == "r":
                color = pygame.Color('red')
            elif piecename.lower() == "b":
                color = pygame.Color('blue')
            xpos = BOARD_POS[0] + x * TILESIZE + 1
            ypos = BOARD_POS[1] + y * TILESIZE + 1
            if king:
                pygame.draw.rect(screen, color, (
                    (xpos + 9 / 25 * TILESIZE, ypos + 1 / 10 * TILESIZE), (7 / 25 * TILESIZE, 8 / 10 * TILESIZE)))
                pygame.draw.rect(screen, color, (
                    (xpos + 1 / 10 * TILESIZE, ypos + 9 / 25 * TILESIZE), (8 / 10 * TILESIZE, 7 / 25 * TILESIZE)))

            elif color:
                pygame.draw.circle(screen, color, (xpos + TILESIZE / 2, ypos + TILESIZE / 2), TILESIZE / 3)
            pos = pygame.Vector2(pygame.mouse.get_pos())
            selected_rect = pygame.Rect(BOARD_POS[0] + selected_piece[1] * TILESIZE, BOARD_POS[1] + selected_piece[2] * TILESIZE, TILESIZE, TILESIZE)
            pygame.draw.line(screen, pygame.Color('red'), selected_rect.center, pos)
            return x, y

def print_turn(turn):
    if turn == "B":
        print("Blue player's turn")
    else:
        print("Red player's turn")

def main():
    def get_pos(card):
        i = 0
        for c in redCards:
            if c.name == card.name:
                print("R" + str(i+1))
                return "R" + str(i+1)
            i += 1
        i = 0
        for c in blueCards:
            if c.name == card.name:
                print("B" + str(i+1))
                return "B" + str(i+1)
            i += 1
    redPlayer = Human("R")
    bluePlayer = Computer("B",5)
    def islegal(move, card):
        start = move[0]
        end = move[1]
        # check that start and end are on the board
        # check that my piece is on start square
        # check that move is one of the card's moves
        # check that ending square is not my piece
        if turn == "B":
            cardmoves = [[-1*x[0],-1*x[1]] for x in card.moves]
        elif turn == "R":
            cardmoves = card.moves
        if all(map(lambda x: x in range(5), start + end)) and \
                board[start[1]][start[0]].upper() == turn and \
                board[end[1]][end[0]].upper() != turn and \
                [end[0] - start[0], end[1] - start[1]] in cardmoves:
            return True
        else:
            return False
    redCards, blueCards, middleCard = dealCards()
    turn = middleCard.color
    print_turn(turn)
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    board = create_board()
    board_surf = create_board_surf()
    clock = pygame.time.Clock()
    selected_piece = None
    drop_pos = None
    selected_card = None
    cardpos = None
    while True:
        if gameOver(board) == "Blue" or gameOver(board) == "Red":
            print(gameOver(board) + " player wins!")
            break
        piece, x, y = get_square_under_mouse(board)
        # if x and y:
        #     rect = (BOARD_POS[0] + x * TILESIZE, BOARD_POS[1] + y * TILESIZE, TILESIZE, TILESIZE)
        #     pygame.draw.rect(screen, (0, 255, 0, 50), rect, 2)
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                return
            elif turn == "R" and isinstance(redPlayer,Computer) or turn == "B" and isinstance(bluePlayer,Computer):
                if turn == "B":
                    selected_card, selected_piece, drop_pos = bluePlayer.getMove(board,blueCards,redCards,middleCard)
                else:
                    selected_card, selected_piece, drop_pos = bluePlayer.getMove(board, redCards, blueCards, middleCard)
                piece, old_x, old_y = selected_piece
                new_x, new_y = drop_pos
                move = (old_x, old_y), (new_x, new_y)
                cardpos = get_pos(selected_card)
                if islegal(move, selected_card):
                    board[old_y][old_x] = " "
                    board[new_y][new_x] = piece
                    if turn == "R":
                        turn = "B"
                    else:
                        turn = "R"
                    print_turn(turn)
                    if cardpos == "R1":
                        middleCard, redCards[0] = redCards[0], middleCard
                    elif cardpos == "R2":
                        middleCard, redCards[1] = redCards[1], middleCard
                    elif cardpos == "B1":
                        middleCard, blueCards[0] = blueCards[0], middleCard
                    elif cardpos == "B2":
                        middleCard, blueCards[1] = blueCards[1], middleCard
                    selected_card = None
                    cardpos = None
                else:
                    print("illegal move")
                selected_piece = None
                drop_pos = None
                break
            elif e.type == pygame.MOUSEBUTTONDOWN:
                if piece != None:
                    if piece in ["R1","B1","R2","B2","M"]:
                        if piece[0] == "R":
                            if turn != "R":
                                pass
                            elif piece[1] == "1":
                                selected_card = redCards[0]
                            else:
                                selected_card = redCards[1]
                        elif piece[0] == "B":
                            if turn != "B":
                                pass
                            elif piece[1] == "1":
                                selected_card = blueCards[0]
                            else:
                                selected_card = blueCards[1]
                        else:
                            selected_card = middleCard

                        cardpos = piece
                    elif selected_card:
                        selected_piece = piece, x, y
            elif e.type == pygame.MOUSEBUTTONUP:
                if drop_pos:

                    piece, old_x, old_y = selected_piece
                    new_x, new_y = drop_pos
                    move = (old_x,old_y),(new_x,new_y)
                    if islegal(move,selected_card):
                        board[old_y][old_x] = " "
                        board[new_y][new_x] = piece
                        if turn == "R":
                            turn = "B"
                        else:
                            turn = "R"
                        print_turn(turn)
                        if cardpos == "R1":
                            middleCard, redCards[0] = redCards[0], middleCard
                        elif cardpos == "R2":
                            middleCard, redCards[1] = redCards[1], middleCard
                        elif cardpos == "B1":
                            middleCard, blueCards[0] = blueCards[0], middleCard
                        elif cardpos == "B2":
                            middleCard, blueCards[1] = blueCards[1], middleCard
                        selected_card = None
                        cardpos = None

                selected_piece = None
                drop_pos = None

        screen.fill(pygame.Color('grey'))
        screen.blit(board_surf, BOARD_POS)
        draw_pieces(screen, board)
        draw_cards(screen,redCards, blueCards, middleCard)
        draw_selector(screen, piece, x, y)
        draw_selected_card(screen, cardpos)
        drop_pos = draw_drag(screen, board, selected_piece)
        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()