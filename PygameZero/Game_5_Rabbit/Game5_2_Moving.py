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
      def __init__(self, image_file, pos = (random.randint(0,WIDTH),0), speed = 1):
            super().__init__(image_file, pos)
            self.pos = pos
            self.speed = speed

      def reset_position(self):
            self.pos = (WIDTH, self.y)
            
      def moving(self):
            self.x = self.x - self.speed
            if (self.x) <= 0 :
                  self.reset_position()

class Player(Actor):
      def __init__(self, image_file, pos = (random.randint(0,WIDTH),0), speed = 1):
            super().__init__(image_file, pos)
            self.pos = pos
            self.speed = speed

rabbitSprite = Player('rabbit1',pos = (50, 420))

snailSprite = Animal('snail1',pos = (750, 430),speed = 2)
flySprite = Animal('fly1',pos = (750, 300),speed = 3)
carrotSprite = Animal('carrot',pos = (750, 200),speed = 5)

rabbitRun = ['rabbit1','rabbit2']  #rabbit3 is jumping
rabbitJump = ['rabbit3']
snailRun = ['snail1','snail2']  
flyRun = ['fly1','fly2']

def update():
      snailSprite.moving()
      flySprite.moving()
      carrotSprite.moving()
            
def draw():
      screen.blit('sky', (0,0))  #800, 450
      screen.blit('ground', (0,450)) #800, 150
      rabbitSprite.draw()
      snailSprite.draw()
      flySprite.draw()
      carrotSprite.draw()

image_counter_fast = 0
def animateimages_fast():
    global image_counter_fast
    rabbitSprite.image = rabbitRun[image_counter_fast % len(rabbitRun)]
    flySprite.image = flyRun[image_counter_fast % len(flyRun)]
    image_counter_fast += 1

image_counter_slow = 0
def animateimages_slow():
    global image_counter_slow
    snailSprite.image = snailRun[image_counter_slow % len(snailRun)]
    image_counter_slow += 1


clock.schedule_interval(animateimages_fast, 0.1)
clock.schedule_interval(animateimages_slow, 0.8)


pgzrun.go()