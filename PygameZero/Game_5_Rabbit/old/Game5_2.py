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
rabbitRun = ['rabbit1','rabbit2']  #rabbit3 is jumping
rabbitJump = ['rabbit3']
##snail
snailSprite = Actor('snail1')
snailSprite.pos = (750, 430)
snailRun = ['snail1','snail2']  
##fly
flySprite = Actor('fly1')
flySprite.pos = (750, 300)
flyRun = ['fly1','fly2']
##carrot
carrotSprite = Actor('carrot')
carrotSprite.pos = (750, 200)

#dynamic
snail_speed = 2
fly_speed = 5
carrot_speed = 3

def reset_carrot():
      carrotSprite.pos = (WIDTH, 200)
      
def carrotMove():
      carrotSprite.x = carrotSprite.x - carrot_speed
      if (carrotSprite.x) <= 0 :
            reset_carrot()

def reset_fly():
      flySprite.pos = (WIDTH, 300)
      
def flyMove():
      flySprite.x = flySprite.x - fly_speed
      if (flySprite.x) <= 0 :
            reset_fly()

def reset_snail():
      snailSprite.pos = (WIDTH, 430)
      
def snailMove():
      snailSprite.x = snailSprite.x - snail_speed
      if (snailSprite.x) <= 0 :
            reset_snail()

def update():
      snailMove()
      flyMove()
      carrotMove()
            
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
