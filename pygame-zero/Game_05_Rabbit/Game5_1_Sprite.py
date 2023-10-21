##To set screen to be in the middle
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (300,50) 
import pygame
import pgzrun
import random

TITLE = 'Game 5'
WIDTH = 800
HEIGHT = 600

class Animal(Actor):
    def __init__(self, image_file, pos = (random.randint(0,WIDTH),0)):
        super().__init__(image_file, pos)
        self.pos = pos

class Player(Actor):
      def __init__(self, image_file, pos = (random.randint(0,WIDTH),0), speed = 1):
            super().__init__(image_file, pos)
            self.pos = pos
            self.speed = speed

rabbitSprite = Player('rabbit1',pos = (50, 420))
snailSprite = Animal('snail1',pos = (750, 430))
flySprite = Animal('fly1',pos = (750, 300))
carrotSprite = Animal('carrot',pos = (750, 200))

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