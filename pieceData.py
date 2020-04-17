class BoardPieceData(object):
    rank8 = ["r", "kn", "b", "q", "k", "b", "kn", "r"]
    rank7 = ["p","p","p","p","p","p","p","p"]
    rank6 = ["e","e","e","e","e","e","e","e"]
    rank5 = ["e","e","e","e","e","e","e","e"]
    rank4 = ["e","e","e","e","e","e","e","e"]
    rank3 = ["e","e","e","e","e","e","e","e"]
    rank2 = ["p","p","p","p","p","p","p","p"]
    rank1 = ["r", "kn", "b", "q", "k", "b", "kn", "r"]

boardData = BoardPieceData()

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