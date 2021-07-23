# Saicharan Vemuri (FiveArcher76571)
# Started July 22, 2021
# PyGame Sandbox
# Requires PyGame module
# Made using the tutorial at https://coderslegacy.com/python/python-pygame-tutorial/

import pygame, sys
from pygame import rect
from pygame.locals import *
 
# Initialize program
pygame.init()
 
# Assign FPS a value
FPS = 30
RefRate = pygame.time.Clock()
 
# Setting up color objects
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
# Setup a 300x300 pixel display with caption
DISPLAYSURF = pygame.display.set_mode((300,300))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("lollllll face")
 
# Creating Lines and Shapes
#pygame.draw.line(DISPLAYSURF, BLUE, (150,130), (130,170))
#pygame.draw.line(DISPLAYSURF, BLUE, (150,130), (170,170))
#pygame.draw.line(DISPLAYSURF, GREEN, (130,170), (170,170))
pygame.draw.polygon(DISPLAYSURF, BLUE, [(150, 130), (130, 170), (170, 170)], width=1)
pygame.draw.circle(DISPLAYSURF, BLACK, (100,50), 30, width=4)
pygame.draw.circle(DISPLAYSURF, BLACK, (125, 50), 5)
pygame.draw.circle(DISPLAYSURF, BLACK, (200,50), 30, width=4)
pygame.draw.circle(DISPLAYSURF, BLACK, (225, 50), 5)
#pygame.draw.rect(DISPLAYSURF, RED, (100, 200, 100, 50), 2)
pygame.draw.arc(DISPLAYSURF, RED, (100, 175, 100, 50), 3.14, 6.28, width=5)
pygame.draw.rect(DISPLAYSURF, BLACK, (110, 260, 80, 5))
 
# Beginning Game Loop
while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
   
    RefRate.tick(FPS)