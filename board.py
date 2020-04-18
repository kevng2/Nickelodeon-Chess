import tkinter as tk
import sound
import pygame
import pieceData

def printBoardPieces(data):
    for i in range(0, 8):
        for j in range(0, 8):
            if data.boardArray[i][j].piece != 'e':
                # Able to use a generic call because of inheritance
                gameDisplay.blit(data.boardArray[i][j].sprite, (squareSize * j + 300, squareSize * i + 200))

# initialize pygame
pygame.init()

# set window size
gameDisplay = pygame.display.set_mode((1000, 1000))

# window name
pygame.display.set_caption('Nickelodeon Chess')
gameExit = False

# blue background, we'll change as needed
gameDisplay.fill((51, 153, 255))

squareSize = 80
count = 0

# starting position of the pieces
boardPosition = pieceData.BoardPieceData()

# loop to print out board, 64 squares
for i in range(0, 8):
    for j in range(0, 8):
        if count % 2 == 0:
            # print orange square
            # rect(surface, color, rect), rect includes [int x, int y, width, height]
            pygame.draw.rect(gameDisplay, (204,102,0), [squareSize*j + 300, squareSize*i + 200, squareSize, squareSize])
        else:
            # print white squares
            pygame.draw.rect(gameDisplay, (255,255,255), [squareSize*j + 300, squareSize*i + 200, squareSize, squareSize])
        count += 1
    # -1 to for alternating rows
    count -= 1

printBoardPieces(boardPosition)

pygame.display.update()
sound.music()

# Loop to print out different events, just for testing
while not gameExit:
    for event in pygame.event.get():
        #print(event)
        if (event.type == pygame.QUIT):
            pygame.quit()
            quit()
