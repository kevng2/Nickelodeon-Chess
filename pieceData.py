import pygame

class BoardPieceData(object):
<<<<<<< HEAD
    rank8 = ["r", "kn", "b", "q", "k", "b", "kn", "r"]
    rank7 = ["p","p","p","p","p","p","p","p"]
    rank6 = ["e","e","e","e","e","e","e","e"] 
    rank5 = ["e","e","e","e","e","e","e","e"]
    rank4 = ["e","e","e","e","e","e","e","e"] 
    rank3 = ["e","e","e","e","e","e","e","e"]
    rank2 = ["p","p","p","p","p","p","p","p"]
    rank1 = ["r", "kn", "b", "q", "k", "b", "kn", "r"]
=======
    def __init__(self):
        #initiliazing empty array
        self.boardArray = [[(Rook('b', 0, 0)), (Knight('b', 0, 1)), (Bishop('b', 0, 2)), (Queen('b', 0, 3)),
                           (King('b', 0, 4)), (Bishop('b', 0, 5)), (Knight('b', 0, 6)), (Rook('b', 0, 7))],
                          [Pawn('b', 1, n) for n in range(8)], [['e']*4 for i in range(8)],
                          [Pawn('w', 6, n) for n in range(8)], [(Rook('w', 7, 0)), (Knight('w', 7, 1)), (Bishop('w', 7, 2)), (Queen('w', 7, 3)),
                           (King('w', 7, 4)), (Bishop('w', 7, 5)), (Knight('w', 7, 6)), (Rook('w', 7, 7))]]




#initializing chess pieces

#class piece, team is team color w or b, x is rows on board, y is columns


class Piece(pygame.sprite.Sprite):
    def __init__(self, team, x, y):
        #used for inheritance
        super().__init__()
        self.team = team
        self.x = x
        self.y = y


class Bishop(Piece):
    def __init__(self, team, x, y):
        #super used for inheritance
        super().__init__(team, x, y)
        #sprite is a visual object within pygame
        self.sprite = pygame.image.load("./images/bishop.png")


class Rook(Piece):
    def __init__(self, team, x, y):
        #super used for inheritance
        super().__init__(team, x, y)
        #sprite is a visual object within pygame
        self.sprite = pygame.image.load("./images/rook.png")


class King(Piece):
    def __init__(self, team, x, y):
        #super used for inheritance
        super().__init__(team, x, y)
        #sprite is a visual object within pygame
        self.sprite = pygame.image.load("./images/king.png")


class Queen(Piece):
    def __init__(self, team, x, y):
        #super used for inheritance
        super().__init__(team, x, y)
        #sprite is a visual object within pygame
        self.sprite = pygame.image.load("./images/queen.png")


class Knight(Piece):
    def __init__(self, team, x, y):
        #super used for inheritance
        super().__init__(team, x, y)
        #sprite is a visual object within pygame
        self.sprite = pygame.image.load("./images/knight.png")


class Pawn(Piece):
    def __init__(self, team, x, y):
        #super used for inheritance
        super().__init__(team, x, y)
        #sprite is a visual object within pygame
        self.sprite = pygame.image.load("./images/pawn.png")
>>>>>>> f50f1219fdb7129c33553c3efa4fb340383d4ece
