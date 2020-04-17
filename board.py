import matplotlib.pyplot as plt
import tkinter as tk
import sound
import pygame

# initialize pygame
pygame.init()

# set window size
gameDisplay = pygame.display.set_mode((800, 800))

# window name
pygame.display.set_caption('Nickelodeon Chess')
gameExit = False

# orange background, we'll change as needed
gameDisplay.fill((51, 153, 255))

squareSize = 80
count = 0

image = pygame.image.load('./images/king.png')

# loop to print out board, 64 squares
for i in range(0, 8):
    for j in range(0, 8):
        if count % 2 == 0:
            # print black square
            pygame.draw.rect(gameDisplay, (204,102,0), [squareSize*j + 85, squareSize*i + 85, squareSize, squareSize])
        else:
            # print white squares
            pygame.draw.rect(gameDisplay, (255,255,255), [squareSize*j + 85, squareSize*i + 85, squareSize, squareSize])
        count += 1
    # -1 to for alternating rows
    count -= 1
gameDisplay.blit(image, (50,50))

pygame.display.update()
sound.music()

# Loop to print out different events, just for testing
while not gameExit:
    for event in pygame.event.get():
        print(event)
        if (event.type == pygame.QUIT):
            pygame.quit()
            quit()
