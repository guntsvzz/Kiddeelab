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
      def __init__(self, image_file, type_, pos = (random.randint(0,WIDTH),0), speed = 1):
            super().__init__(image_file, pos)
            self.pos = pos
            self.speed = speed
            self.type = type_

      def reset_position(self):
            self.pos = (WIDTH, self.y)
            
      def moving(self):
            self.x = self.x - self.speed
            if (self.x) <= 0 :
                  self.reset_position()

class Player(Actor):

      GRAVITY = 0.5
      Jump_VELOCITY = -16

      def __init__(self, image_file, pos = (random.randint(0,WIDTH),0), speed = 1):
            super().__init__(image_file, pos)
            self.pos = pos
            self.speed = speed
            self.hp = 5
            self.vy = 0
            self.jumpcount = True
            self.score = 0
            self.game_state = 'main'

      def gameSong(self):
            if self.game_state == 'win' :
                  music.play('win')
            elif self.game_state == 'gameover' :
                  music.play('failgame')
            elif self.game_state == 'play' :
                  music.play('rungame')   

      def jump(self):
            ####On ground
            if self.y >= 420:  
                  self.vy = 0
                  self.y = 420
                  self.jumpcount = True
            else :
                  self.jumpcount = False
            #### Double Jumping
            if keyboard.up and self.jumpcount == True:
                  self.vy = Player.Jump_VELOCITY
                  self.y = self.y + self.vy
            else:
                  self.vy = self.vy + Player.GRAVITY
                  self.y = self.y + self.vy

      def collision(self, animal):
            if self.colliderect(animal) and animal.type == 'carrot':
                  self.score += 1
                  animal.reset_position()
            elif self.colliderect(animal) and animal.type == 'fly':
                  self.hp -= 1
                  animal.reset_position()
            elif self.colliderect(animal)  and animal.type == 'snail':
                  self.hp -= 2
                  animal.reset_position()


            if self.score >= 5 :
                  self.game_state = 'win'
            if self.hp <= 0 :
                  self.game_state = 'gameover'

rabbitSprite = Player('rabbit1',pos = (50, 420))

snailSprite = Animal('snail1', type_ = 'snail', pos = (750, 430),speed = 2)
flySprite = Animal('fly1', type_ = 'fly', pos = (750, 300),speed = 3)
carrotSprite = Animal('carrot', type_ = 'carrot', pos = (750, 200),speed = 5)

rabbitRun = ['rabbit1','rabbit2']  #rabbit3 is jumping
rabbitJump = ['rabbit3']
snailRun = ['snail1','snail2']  
flyRun = ['fly1','fly2']

def update():
      ####Moving
      snailSprite.moving()
      flySprite.moving()
      carrotSprite.moving()
      ####Collision
      rabbitSprite.collision(snailSprite)
      rabbitSprite.collision(flySprite)
      rabbitSprite.collision(carrotSprite)
      ####Jump
      rabbitSprite.jump()

def draw():
      def restart():
            screen.draw.text('Press space to restart',center = (WIDTH/2, HEIGHT/2+50), color = (255,0,0), fontsize = 40)
            if keyboard.space:
                  rabbitSprite.game_state = 'play'
                  rabbitSprite.score = 0
                  rabbitSprite.gameSong()
                  snailSprite.reset_position()
                  flySprite.reset_position()
                  carrotSprite.reset_position()

                  print(f'Game Status : {rabbitSprite.game_state}')

      screen.blit('sky', (0,0))  #800, 450
      screen.blit('ground', (0,450)) #800, 150
      if rabbitSprite.game_state == 'main':
            screen.draw.text('Run Rabbit Run' , center=(400, 200), color=(255, 255, 255), fontsize=100)
            restart()
      elif rabbitSprite.game_state == 'gameover':
            screen.draw.text('Game Over' , center=(400, 200), color=(255, 255, 255), fontsize=100)
            restart()
      elif rabbitSprite.game_state == 'win':
            screen.draw.text('You Win' , center=(400, 200), color=(255, 255, 255), fontsize=100)
            restart()

      elif rabbitSprite.game_state == 'play':
            rabbitSprite.draw()
            snailSprite.draw()
            flySprite.draw()
            carrotSprite.draw()
            screen.draw.text('Score: ' + str(rabbitSprite.score), (15, 10), color=(0, 0, 255), fontsize=30)
            screen.draw.text('Life: ' + str(rabbitSprite.hp), (700, 15), color=(255, 0, 0), fontsize=30)
      
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