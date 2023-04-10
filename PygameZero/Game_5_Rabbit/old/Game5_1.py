##To set screen to be in the middle
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (300,50) 
import pygame
import pgzrun
import random

TITLE = 'Game 5'
WIDTH = 800
HEIGHT = 600

#actor
##rabbit
rabbitSprite = Actor('rabbit1')
rabbitSprite.pos = (50, 420)
##snail
snailSprite = Actor('snail1')
snailSprite.pos = (750, 430)
##fly
flySprite = Actor('fly1')
flySprite.pos = (750, 300)
##carrot
carrotSprite = Actor('carrot')
carrotSprite.pos = (750, 200)

def update():
      pass
            
def draw():
      screen.blit('sky', (0,0))  #800, 450
      screen.blit('ground', (0,450)) #800, 150
      rabbitSprite.draw()
      snailSprite.draw()
      flySprite.draw()
      carrotSprite.draw()
      
pgzrun.go()
