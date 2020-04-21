import tkinter as tk
import sound
import font
import pygame
from pygame import mixer

pygame.init()

white = (255, 255, 255)
blue = (51, 153, 255)
orange = (245, 124, 19)

gameDisplay = pygame.display.set_mode((1200, 1000))

pygame.display.set_caption('Nickelodeon Chess')
gameExit = False

gameDisplay.fill(blue)

logo = pygame.image.load("NickelodeonLogo.png")
logo = pygame.transform.scale(logo, (640,484))
gameDisplay.blit(logo, (300, 0))

def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def sign(w, h, sign, color):
    startsign = pygame.font.Font('some-time-later.ttf', 80)
    TextSurf, TextRect = text_objects(sign, startsign, color)
    TextRect.center = (w, h)
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

sign(600, 320, "Chess", white)

sign(600,550, "Start", orange)
sign(600, 700, "Settings", orange)

pygame.display.update()
sound.music()
SONG_END = pygame.USEREVENT + 1
mixer.music.set_endevent(SONG_END)

while not gameExit:
    for event in pygame.event.get():
        if event.type == SONG_END:
            sound.music()
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            print(pos)
            clicked_sprites = [s for s in spriteList if s.rect.collidepoint(pos)]
            print(clicked_sprites)
        if (event.type == pygame.QUIT):
            pygame.quit()
            quit()
