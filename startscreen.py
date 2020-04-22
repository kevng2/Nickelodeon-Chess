import tkinter as tk
import sound
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

sign(600, 340, "Chess", white)

class button():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)

        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)

        if self.text != '':
            font = pygame.font.Font('some-time-later.ttf', 80)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False

#sign(600,550, "Start", orange)
#sign(600, 700, "Settings", orange)
start = button((orange),450,500,250,150, "Start")

pygame.display.update()
sound.music()
SONG_END = pygame.USEREVENT + 1
mixer.music.set_endevent(SONG_END)

while not gameExit:
    start.draw(gameDisplay, (0,0,0))
    pygame.display.update()
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == SONG_END:
            sound.music()
        '''if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            print(pos)
            clicked_sprites = [s for s in spriteList if s.rect.collidepoint(pos)]
            print(clicked_sprites)'''
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start.isOver(pos):
                print('clicked start')
                exec(open('board.py').read())
        if event.type == pygame.MOUSEMOTION:
            if start.isOver(pos):
                start.color = (white)
            else:
                start.color = (orange)
        if (event.type == pygame.QUIT):
            pygame.quit()
            quit()
