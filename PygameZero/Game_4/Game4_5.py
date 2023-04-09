##To set screen to be in the middle
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (300,50) 
import pygame
import pgzrun
import random

TITLE = 'Game 4'
WIDTH = 800
HEIGHT = 600

#Timer and timeout
timeRise = [0.5, 1, 1.5, 2, 2.5]
timeOut = [0.5, 1, 1.5, 2, 2.5]
#actor
##hostage
hostageSprite = Actor('hostage')
hostageSprite.pos = (random.randint(10, 790), 550)
hostage_risetime = timeRise[random.randrange(0,5,1)]
hostage_timeout = timeOut[random.randrange(0,5,1)]

##terrors
#terror1
terror1Sprite = Actor('terror1')
terror1Sprite.pos = (random.randint(10, 790), 550)
terror1_risetime = timeRise[random.randrange(0,5,1)]
terror1_timeout = timeOut[random.randrange(0,5,1)]
#terror2
terror2Sprite = Actor('terror2')
terror2Sprite.pos = (random.randint(10, 790), 550)
terror2_risetime = timeRise[random.randrange(0,5,1)]
terror2_timeout = timeOut[random.randrange(0,5,1)]

#GunCenter
GunCenter = Actor('crosshair')

#game states
game_state = ''

#score
score = 0

def on_mouse_move(pos, rel, buttons):
    GunCenter.x = pos[0]
    GunCenter.y = pos[1]

def on_mouse_down(pos, button):
      global score
      global game_state
      if button == mouse.LEFT :
          sounds.bullet_pew.play()
          #hostage shot
          if hostageSprite.collidepoint(pos) :
                hostageshot = True
                print('Hostage shot')
                game_state = 'gameover'
                sounds.scream_hostage.play()
                gameSong()
          else :
                hostageshot = False
          #terror1 shot
          if terror1Sprite.collidepoint(pos) :
                terror1shot = True
                sounds.scream_terrorist.play()
                print('Terror1 shot')
                score = score + 1
                terror1Sprite.pos =(random.randint(10, 790), 550) 
          else :
                terror1shot = False
          #terror2 shot
          if terror2Sprite.collidepoint(pos) :
                terror2shot = True
                sounds.scream_terrorist.play()
                print('Terror2 shot')
                score = score + 2
                terror2Sprite.pos =(random.randint(10, 790), 550)
          else :
                terror2shot = False
          if score > 5 :
              game_state = 'win'
              gameSong()
                
def hostageMove():
    global hostage_risetime, hostage_timeout
    hostage_risetime = hostage_risetime - 1/60
    if hostage_risetime <= 0:
        hostageSprite.y = hostageSprite.y - 2
        if hostageSprite.y < 350 :
            hostageSprite.y = 350
            hostage_timeout = hostage_timeout - 1/60
            if hostage_timeout <=0:
                hostageSprite.y = 550
                hostageSprite.x = random.randint(0, 790)
                hostage_risetime = timeRise[random.randrange(0,5,1)]
                hostage_timeout = timeOut[random.randrange(0,5,1)]

def terror1Move():
    global terror1_risetime, terror1_timeout
    terror1_risetime = terror1_risetime - 1/60
    if terror1_risetime <= 0:
        terror1Sprite.y = terror1Sprite.y - 2
        if terror1Sprite.y < 350 :
            terror1Sprite.y = 350
            terror1_timeout = terror1_timeout - 1/60
            if terror1_timeout <=0:
                terror1Sprite.y = 550
                terror1Sprite.x = random.randint(0, 790)
                terror1_risetime = timeRise[random.randrange(0,5,1)]
                terror1_timeout = timeOut[random.randrange(0,5,1)]

def terror2Move():
    global terror2_risetime, terror2_timeout
    terror2_risetime = terror2_risetime - 1/60
    if terror2_risetime <= 0:
        terror2Sprite.y = terror2Sprite.y - 2
        if terror2Sprite.y < 350 :
            terror2Sprite.y = 350
            terror2_timeout = terror2_timeout - 1/60
            if terror2_timeout <=0:
                terror2Sprite.y = 550
                terror2Sprite.x = random.randint(0, 790)
                terror2_risetime = timeRise[random.randrange(0,5,1)]
                terror2_timeout = timeOut[random.randrange(0,5,1)]                                  
def update():
      global game_state 
      if game_state == 'play' : 
          hostageMove()
          terror1Move()
          terror2Move()
      
def draw():
      global score
      screen.blit('background', (0,0))
      def restart() :
            global game_state
            global score
            screen.draw.text('Re Start' , center=(400, 300), color=(255, 0, 0), fontsize=80)
            screen.draw.text('Press space bar to play' , center=(400, 350), color=(255, 0, 0), fontsize=50)
            if keyboard.space == True :
                  game_state = 'play'
                  score = 0
                  gameSong()
            
      if game_state == '' : #Main Screen
            screen.draw.text('Save Hostage' , center=(400, 200), color=(255, 255, 255), fontsize=100)
            restart()
      elif game_state == 'gameover' : 
            screen.draw.text('Game Over' , center=(400, 200), color=(255, 255, 255), fontsize=100)
            restart()
      elif game_state == 'win' : 
            screen.draw.text('You Win' , center=(400, 200), color=(255, 255, 255), fontsize=100)
            restart()
      elif  game_state == 'play' :       
            screen.draw.text('Score:' +str(score), (15, 10), color=(255, 255, 255), fontsize=40)
            hostageSprite.draw()
            terror1Sprite.draw()
            terror2Sprite.draw()
            GunCenter.draw()
      screen.blit('wall', (0,400)) #W:800 H:250

def gameSong():
      if game_state == 'win' :
            sounds.win.play()
            sounds.snarebeat.stop()
      elif game_state == 'gameover' :
            sounds.gameover.play()
            sounds.snarebeat.stop()
      elif game_state == 'play' :
             sounds.snarebeat.play(-1)
             sounds.gameover.stop()
             sounds.win.stop()        

pgzrun.go()
