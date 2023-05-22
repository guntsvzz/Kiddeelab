##To set screen to be in the middle
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (300,50) 
import pygame
import pgzrun
import random

HEIGHT = 600
WIDTH = 750
TITLE = 'Game 7'

#actors
galagaSprite = Actor('galaga')
galagaSprite.pos = (WIDTH/2, 550)
meteorSprite = Actor('meteor')
meteorSprite.pos = (50, 50)
bugSprite = Actor('bug')
bugSprite.pos = (WIDTH/2,100)
dynamiteSprite = Actor('dynamite')
dynamiteSprite.pos = (600, 50)

def update():
      pass

def draw():
      screen.blit('galagabg', (0,0))
      galagaSprite.draw()
      meteorSprite.draw()
      bugSprite.draw()
      dynamiteSprite.draw()
      
pgzrun.go()

