import tkinter as tk
import sound
import pygame
import pieceData
from pygame import mixer

def printBoardPieces(data):
    for piece in data:
        gameDisplay.blit(piece.image, (piece.rect))

def isOccupied(i,j):
    if (boardPosition.boardArray[i][j].piece =='e'):
        return False
    return True
def isOccupiedBy(i,j, color, piece):
    if (boardPosition.boardArray[i][j].piece =='e'):
        print ("Empty Space at (", i, ",",j , ")")
        return False
    if (boardPosition.boardArray[i][j].team == color):
        print (color, piece, "at (", i, ",", j, ")" )
        return True
    return False


def draw_move(clicked, sprites):
    move = possible_moves(clicked)
    print ("Clicked Piece:", clicked.piece)
    for n in move:

        if n[1] < 0 or n[0] < 0 or n[1] > 7 or n[0] > 7:
            continue
        #elif (al for al in sprites if al.x and al.y in n[0] and n[1]):
            #continue
        elif (isOccupied(n[0],n[1]) == True):
            isOccupiedBy(n[0],n[1],boardPosition.boardArray[n[0]][n[1]].team,boardPosition.boardArray[n[0]][n[1]].piece)
            continue
        else:
            if (clicked.team == 'w'):
                pygame.draw.circle(gameDisplay, (0, 205, 0), ((340+(n[1]*80)), (240+(n[0]*80))), 7)
            else:
                pygame.draw.circle(gameDisplay, (255, 8, 0), ((340+(n[1]*80)), (240+(n[0]*80))), 7)

#function takes in a value for the piece coordinate and gives possible moves
def possible_moves(pieceSelected):
    moves = [] #creating an empty list of tuples of coordinates for where a piece can move

    if pieceSelected.piece == 'N':
        moves += [(pieceSelected.x-1, pieceSelected.y-2), (pieceSelected.x-1, pieceSelected.y+2), (pieceSelected.x-2, pieceSelected.y+1), (pieceSelected.x-2, pieceSelected.y-1),
                  (pieceSelected.x+1, pieceSelected.y-2), (pieceSelected.x+1, pieceSelected.y+2), (pieceSelected.x+2, pieceSelected.y-1), (pieceSelected.x+2, pieceSelected.y+1)]

    elif pieceSelected.piece == 'B':
        down_left = [(pieceSelected.x-n, pieceSelected.y-n) for n in range(1, 8)]
        down_right = [(pieceSelected.x+n, pieceSelected.y-n) for n in range(1, 8)]
        up_right = [(pieceSelected.x+n, pieceSelected.y+n) for n in range(1, 8)]
        up_left = [(pieceSelected.x-n, pieceSelected.y+n) for n in range(1, 8)]
        moves += down_left + down_right + up_right + up_left

    elif pieceSelected.piece == 'R':
        left = [(pieceSelected.x-n, pieceSelected.y) for n in range(1, 8)]
        right = [(pieceSelected.x+n, pieceSelected.y) for n in range(1, 8)]
        up = [(pieceSelected.x, pieceSelected.y+n) for n in range(1, 8)]
        down = [(pieceSelected.x, pieceSelected.y-n) for n in range(1, 8)]
        moves += left + right + up + down

    elif pieceSelected.piece == 'Q':
        left = [(pieceSelected.x-n, pieceSelected.y) for n in range(1, 8)]
        right = [(pieceSelected.x+n, pieceSelected.y) for n in range(1, 8)]
        up = [(pieceSelected.x, pieceSelected.y+n) for n in range(1, 8)]
        down = [(pieceSelected.x, pieceSelected.y-n) for n in range(1, 8)]

        down_left = [(pieceSelected.x - n, pieceSelected.y - n) for n in range(1, 8)]
        down_right = [(pieceSelected.x + n, pieceSelected.y - n) for n in range(1, 8)]
        up_right = [(pieceSelected.x + n, pieceSelected.y + n) for n in range(1, 8)]
        up_left = [(pieceSelected.x - n, pieceSelected.y + n) for n in range(1, 8)]
        moves += down_left + down_right + up_right + up_left + left + right + up + down

    elif pieceSelected.piece == 'K':
        left = [(pieceSelected.x - 1, pieceSelected.y)]
        right = [(pieceSelected.x + 1, pieceSelected.y)]
        up = [(pieceSelected.x, pieceSelected.y + 1)]
        down = [(pieceSelected.x, pieceSelected.y - 1)]

        down_left = [(pieceSelected.x - 1, pieceSelected.y - 1)]
        down_right = [(pieceSelected.x + 1, pieceSelected.y - 1)]
        up_right = [(pieceSelected.x + 1, pieceSelected.y + 1)]
        up_left = [(pieceSelected.x - 1, pieceSelected.y + 1)]
        moves += down_left + down_right + up_right + up_left + left + right + up + down

    elif pieceSelected.piece == 'P':
        #rank 2 pawn
        if pieceSelected.team == 'b' and pieceSelected.x == 1:
            moves += [(pieceSelected.x + 2, pieceSelected.y), (pieceSelected.x + 1, pieceSelected.y)]
        elif pieceSelected.team == 'w' and pieceSelected.x == 6:
            moves += [(pieceSelected.x - 2, pieceSelected.y), (pieceSelected.x - 1, pieceSelected.y)]
        elif pieceSelected.team == 'b':
            moves += [(pieceSelected.x + 1, pieceSelected.y)]
        elif pieceSelected.team == 'w':
            moves += [(pieceSelected.x - 1, pieceSelected.y)]



    return moves

def drawBoard():
    count = 0

    # loop to print out board, 64 squares
    for i in range(0, 8):
        TextSurf, TextRect = text_objects(str(8-i), font)
        TextRect.center = (275, squareSize*i +240)
        gameDisplay.blit(TextSurf, TextRect)

        pygame.display.update()
        for j in range(0, 8):
            if count % 2 == 0:
                # print orange square
                # rect(surface, color, rect), rect includes [int x, int y, width, height]
                pygame.draw.rect(gameDisplay, BRIGHTORANGE, [squareSize*j + 300, squareSize*i + 200, squareSize, squareSize])
            else:
                # print white squares
                pygame.draw.rect(gameDisplay, ORANGE, [squareSize*j + 300, squareSize*i + 200, squareSize, squareSize])
            count += 1
        # -1 to for alternating rows
        count -= 1

def getRectPoints(dest):
    # if the click is out of the bounds of the board
    if dest[0] < 300 or dest[0] > 940 or dest[1] < 200 or dest[1] > 840:
        return (dest[0], dest[1])

    # Coordinates of where the white and orange squares were drawn
    cornerPointsX = [860, 780, 700, 620, 540, 460, 380, 300]
    cornerPointsY = [760, 680, 600, 520, 440, 360, 280, 200]

    xPoint = dest[0]
    yPoint = dest[1]

    # loop through each value in the list to find which
    # square the click was in
    for x in cornerPointsX:
        if xPoint > x:
            xPoint = x
            break

    for y in cornerPointsY:
        if yPoint > y:
            yPoint = y
            break

    return (xPoint, yPoint)

# initialize pygame
pygame.init()

# set window size
gameDisplay = pygame.display.set_mode((1200, 1000))

#creating a surface
#board = pygame.Surface((640, 640))

# window name
pygame.display.set_caption('Nickelodeon Chess')
gameExit = False

BLUE = (51, 153, 255)
WHITE = (255, 255, 255)
ORANGE = (204,102,0)
BRIGHTORANGE = (255, 195, 77)

# blue background, we'll change as needed
gameDisplay.fill(BLUE)

#board dimensions
width = 640
height = 640

# Nickelodeon Logo
logo = pygame.image.load("NickelodeonLogo.png")
logo = pygame.transform.scale(logo,(320,242) )
gameDisplay.blit(logo, (470,-22))

squareSize = 80
count = 0

# starting position of the pieces
boardPosition = pieceData.BoardPieceData()


def text_objects(text, font):
    textSurface = font.render(text, True, WHITE)
    return textSurface, textSurface.get_rect()

font = pygame.font.Font('some-time-later.ttf', 40)
alpha = ['A', 'B', 'C', 'D', 'E', 'F','G', 'H']

drawBoard()

for k in range(0,8):
    TextSurf, TextRect = text_objects(alpha[k], font)
    TextRect.center = (squareSize*k + 340,squareSize*7 +310)
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

#printBoardPieces(boardPosition)

pygame.display.update()

# music
sound.music()
SONG_END = pygame.USEREVENT + 1
mixer.music.set_endevent(SONG_END)

# list of sprites available
spriteList = pygame.sprite.Group()

#added all sprites to board
for i in range(8):
    for j in range(8):
        if (boardPosition.boardArray[i][j].piece=='e'):
            continue
        else:
            spriteList.add(boardPosition.boardArray[i][j])

print(spriteList)

printBoardPieces(spriteList)

# Will check if one of the sprites was selcted
pieceClicked = False

# Will hold the image to redraw it on the board once the user
# selected another square
pieceSelected = None

# Loop to print out different events, just for testing
while not gameExit:
    for event in pygame.event.get():
        if event.type == SONG_END:
            sound.music()

        if event.type == pygame.MOUSEBUTTONUP:

            # Gets the x,y coordinates of the mouse
            pos = pygame.mouse.get_pos()

            # stores the sprite that user clicked
            clicked_sprite = [s for s in spriteList if s.rect.collidepoint(pos)]


            # will draw the image at the specified square
            if pieceClicked == True:
                # Clear the board
                gameDisplay.fill(BLUE)

                # Redraw board
                drawBoard()
                # get the x, y points for which square the sprite belongs in
                pos = getRectPoints(pos)

                # the the Object's rectangle data to the position
                pieceSelected.rect = pygame.Rect(pos[0], pos[1], 80, 80)
                pieceSelected.y = int((pieceSelected.rect[0]-300) / 80)
                pieceSelected.x = int((pieceSelected.rect[1]-200) / 80)

                # Redraw pieces
                printBoardPieces(spriteList)

                pieceClicked = False

            # Store the clicked sprite for the next run of the loop
            # to redraw
            if clicked_sprite:
                pieceClicked = True
                pieceSelected = clicked_sprite[0]
                draw_move(pieceSelected, spriteList)


        if (event.type == pygame.QUIT):
            pygame.quit()
            quit()
    pygame.display.update()
