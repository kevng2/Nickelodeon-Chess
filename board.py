import tkinter as tk
import sound
import pygame
import pieceData
from pygame import mixer

def printBoardPieces(data):
    for i in range(0, 8):
        for j in range(0, 8):
            if data.boardArray[i][j].piece != 'e':
                # Able to use a generic call because of inheritance
                gameDisplay.blit(data.boardArray[i][j].image, (squareSize * j + 300, squareSize * i + 200))


# initialize pygame
pygame.init()

# set window size
gameDisplay = pygame.display.set_mode((1200, 1000))

#creating a surface
#board = pygame.Surface((640, 640))

# window name
pygame.display.set_caption('Nickelodeon Chess')
gameExit = False

# blue background, we'll change as needed
gameDisplay.fill((51, 153, 255))

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
    textSurface = font.render(text, True, (255,255,255))
    return textSurface, textSurface.get_rect()

font = pygame.font.Font('some-time-later.ttf', 40)

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
            pygame.draw.rect(gameDisplay, (255,255,255), [squareSize*j + 300, squareSize*i + 200, squareSize, squareSize])
        else:
            # print white squares
            pygame.draw.rect(gameDisplay, (204,102,0), [squareSize*j + 300, squareSize*i + 200, squareSize, squareSize])
        count += 1
    # -1 to for alternating rows
    count -= 1

alpha = ['A', 'B', 'C', 'D', 'E', 'F','G', 'H']

for k in range(0,8):
    TextSurf, TextRect = text_objects(alpha[k], font)
    TextRect.center = (squareSize*k + 340,squareSize*7 +310)
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()
    
printBoardPieces(boardPosition)

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

isClicked = True 

# Loop to print out different events, just for testing
while not gameExit:
    for event in pygame.event.get():
        if event.type == SONG_END:
            sound.music()
        if event.type == pygame.MOUSEBUTTONUP:
            isClicked = not isClicked
            pos = pygame.mouse.get_pos()
            clicked_sprite = [s for s in spriteList if s.rect.collidepoint(pos)]
            print(clicked_sprite)
        if (event.type == pygame.QUIT):
            pygame.quit()
            quit()
    pygame.display.update()

