import pygame

class BoardPieceData(object):
    def __init__(self):
        # 2D List of starting board positions
        self.boardArray = [
            # Rank 8
           [Rook('b', 'R', 0, 0), Knight('b', 'N', 0, 1), Bishop('b', 'B', 0, 2), Queen('b', 'Q', 0, 3),
            King('b', 'K', 0, 4), Bishop('b', 'B', 0, 5), Knight('b', 'K', 0, 6), Rook('b', 'R', 0, 7)],

            # Rank 7
           [Pawn('b', 'P', 1, n) for n in range(8)],

           # Rank 6 - 3
           [Empty('e') for j in range(8)],
           [Empty('e') for j in range(8)],
           [Empty('e') for j in range(8)],
           [Empty('e') for j in range(8)],

           # Rank 2
           [Pawn('w', 'P', 6, n) for n in range(8)],

           # Rank 1
           [Rook('w', 'R', 7, 0), Knight('w', 'N', 7, 1), Bishop('w', 'B', 7, 2), Queen('w', 'Q', 7, 3),
            King('w', 'K', 7, 4), Bishop('w', 'B', 7, 5), Knight('w', 'K', 7, 6), Rook('w', 'R', 7, 7)]
        ]

#initializing chess pieces
#class piece, team is team color w or b, x is rows on board, y is columns
class Piece(pygame.sprite.Sprite):
    def __init__(self, team, piece, x, y):
        pygame.sprite.Sprite.__init__(self)

        #used for inheritance
        super().__init__()
        self.piece = piece
        self.team = team
        self.x = x
        self.y = y

class Bishop(Piece):
    def __init__(self, team, piece, x, y):
        pygame.sprite.Sprite.__init__(self)

        # super used for inheritance
        super().__init__(team, piece, x, y)

        # sprite is a visual object within pygame
        # load white or black piece depending on team
        if(team == 'w'):
            self.image = pygame.image.load("./images/bishop.png")
        else:
            self.image = pygame.image.load("./images/bishop_b.png")

        # get the rectangle around the image, Sprite class needs this defined to
        # move it later
        self.rect = pygame.Rect(300+(self.y*80), 200+(self.x*80), 80, 80)
        print(self.rect)


class Rook(Piece):
    def __init__(self, team, piece, x, y):
        super().__init__(team, piece, x, y)
        if(team == 'w'):
            self.image = pygame.image.load("./images/rook.png")
        else:
            self.image = pygame.image.load("./images/rook_b.png")

        self.rect = pygame.Rect(300 + (self.y * 80), 200 + (self.x * 80), 80, 80)


class King(Piece):
    def __init__(self, team, piece, x, y):
        super().__init__(team, piece, x, y)
        if(team == 'w'):
            self.image = pygame.image.load("./images/king.png")
        else:
            self.image = pygame.image.load("./images/king_b.png")

        self.rect = pygame.Rect(300 + (self.y * 80), 200 + (self.x * 80), 80, 80)


class Queen(Piece):
    def __init__(self, team, piece, x, y):
        super().__init__(team, piece, x, y)
        if(team == 'w'):
            self.image = pygame.image.load("./images/queen.png")
        else:
            self.image = pygame.image.load("./images/queen_b.png")
        self.rect = pygame.Rect(300 + (self.y * 80), 200 + (self.x * 80), 80, 80)


class Knight(Piece):
    def __init__(self, team, piece, x, y):
        super().__init__(team, piece, x, y)
        if(team == 'w'):
            self.image = pygame.image.load("./images/knight.png")
        else:
            self.image = pygame.image.load("./images/knight_b.png")
        self.rect = pygame.Rect(300 + (self.y * 80), 200 + (self.x * 80), 80, 80)

class Pawn(Piece):
    def __init__(self, team, piece, x, y):
        super().__init__(team, piece, x, y)
        if(team == 'w'):
            self.image = pygame.image.load("./images/pawn.png")
        else:
            self.image = pygame.image.load("./images/pawn_b.png")
        self.rect = pygame.Rect(300 + (self.y * 80), 200 + (self.x * 80), 80, 80)

# Empty Piece class, used to make printing the pieces easier
class Empty(Piece):
    def __init__(self, piece):
        super().__init__(None, None, None, None)
        self.piece = 'e' 
