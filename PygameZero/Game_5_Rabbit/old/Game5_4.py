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
flySprite.pos = (750, 360)
flyRun = ['fly1','fly2']
##carrot
carrotSprite = Actor('carrot')
carrotSprite.pos = (750, 300)

#dynamic
snail_speed = 4
fly_speed = 6
carrot_speed = 3

#Jumping
rabbitSprite.vy = 0
GRAVITY = 0.5
Jump_VELOCITY = -14
rabbitSprite.jumpcount = True

#score and life
score = 0
life = 10

#game state
game_state = ''

def rabbitJump():
      if rabbitSprite.y >= 420:  #On ground
            rabbitSprite.vy = 0
            rabbitSprite.y = 420
            rabbitSprite.jumpcount = True
      else :
            rabbitSprite.jumpcount = False
      if keyboard.up and rabbitSprite.jumpcount == True:
            rabbitSprite.vy = Jump_VELOCITY
            rabbitSprite.y = rabbitSprite.y + rabbitSprite.vy
      else:
            rabbitSprite.vy = rabbitSprite.vy + GRAVITY
            rabbitSprite.y = rabbitSprite.y + rabbitSprite.vy

def ScoreandLife():
      global score
      global life
      global game_state
      if rabbitSprite.colliderect(carrotSprite):
            reset_carrot()
            score = score + 1
            print(score)
      elif rabbitSprite.colliderect(flySprite):
            reset_fly()
            life = life - 1
            print(life)
      elif rabbitSprite.colliderect(snailSprite):
            reset_snail()
            life = life - 2
            print(life)

      if score >= 5 :
            game_state = 'win'
      if life <= 0 :
            game_state = 'gameover'
      
                 
def reset_carrot():
      carrotSprite.pos = (WIDTH, 300)
      
def carrotMove():
      carrotSprite.x = carrotSprite.x - carrot_speed
      if (carrotSprite.x) <= 0 :
            reset_carrot()

def reset_fly():
      flySprite.pos = (WIDTH, 360)
      
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
      global game_state
      if game_state == 'play': 
            snailMove()
            flyMove()
            carrotMove()
            rabbitJump()
            ScoreandLife()
            
def draw():
      screen.blit('sky', (0,0))  #800, 450
      screen.blit('ground', (0,450)) #800, 150
      def restart() :
            global game_state
            global score
            global life
            screen.draw.text('Re Start' , center=(400, 300), color=(255, 0, 0), fontsize=80)
            screen.draw.text('Press space bar to play' , center=(400, 350), color=(255, 0, 0), fontsize=50)
            if keyboard.space == True :
                  game_state = 'play'
                  score = 0
                  life = 10
                  reset_fly()
                  reset_snail()
                  reset_carrot()
      if game_state == '' : #Main Screen
            screen.draw.text('Run Rabbit Run' , center=(400, 200), color=(255, 255, 255), fontsize=100)
            restart()
      elif game_state == 'gameover' : 
            screen.draw.text('Game Over' , center=(400, 200), color=(255, 255, 255), fontsize=100)
            restart()
      elif game_state == 'win' : 
            screen.draw.text('You Win' , center=(400, 200), color=(255, 255, 255), fontsize=100)
            restart()
      elif  game_state == 'play' :
            rabbitSprite.draw()
            snailSprite.draw()
            flySprite.draw()
            carrotSprite.draw()
            screen.draw.text('Score: ' + str(score), (15, 10), color=(0, 0, 255), fontsize=30)
            screen.draw.text('Life: ' + str(life), (700, 15), color=(255, 0, 0), fontsize=30)
    
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
