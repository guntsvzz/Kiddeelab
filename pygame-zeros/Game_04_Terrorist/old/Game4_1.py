##To set screen to be in the middle
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (300,50) 
import pygame
import pgzrun
import random

TITLE = 'Game 4'
WIDTH = 800
HEIGHT = 600

#actor
##hostage
hostageSprite = Actor('hostage')
hostageSprite.pos = (random.randint(10, 790), random.randint(10, 590))

def update():
      pass
            
def draw():
      screen.blit('background', (0,0))
      hostageSprite.draw()
      screen.blit('wall', (0,400)) #W:800 H:250
      
pgzrun.go()
