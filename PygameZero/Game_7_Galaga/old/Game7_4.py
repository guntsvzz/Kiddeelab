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

#dynamic
meteorSpeed = 10
dynamiteSpeed = 10

#Group of enemy
enemies = []
bugXdirection = 1
bugMoveDown = False

#Bullets
bullets = []
bulletActive = False

#score
score = 0

#game state
gameState = 'start'

def on_key_down(key):
      global bulletActive 
      if key == keys.SPACE and bulletActive == False:
            bullets.append(Actor('laserred'))
            bullets[-1].pos = galagaSprite.pos
            bulletActive = True

def bulletMove():
      global bulletActive
      for bullet in bullets:
            if bullet.y <= 0:
                  bullets.remove(bullet)
                  bulletActive = False
            else :
                  bullet.y = bullet.y - 10
                        
def galagaMove():
      global gameState
      if keyboard.a == True :
            galagaSprite.x = galagaSprite.x - 10
      elif keyboard.d == True :
            galagaSprite.x = galagaSprite.x + 10

      if galagaSprite.x >= WIDTH :
            galagaSprite.x = WIDTH
      if galagaSprite.x <= 0 :
            galagaSprite.x = 0

      if galagaSprite.colliderect(dynamiteSprite):
            gameState = 'gameover'
            dynamiteReset()
      elif galagaSprite.colliderect(meteorSprite):
            gameState = 'gameover'
            meteorReset()
      
def meteorMove():
      meteorSprite.y = meteorSprite.y + meteorSpeed
      if meteorSprite.y >= HEIGHT:
            meteorReset()
            
def meteorReset():
      global meteorSpeed
      meteorSprite.pos = (random.randint(0, WIDTH), 0)
      meteorSpeed = random.randint(7,12)

def dynamiteMove():
      dynamiteSprite.y = dynamiteSprite.y + dynamiteSpeed
      if dynamiteSprite.y >= HEIGHT:
            dynamiteReset()
            
def dynamiteReset():
      global dynamiteSpeed
      dynamiteSprite.pos = (random.randint(0, WIDTH), 0)
      dynamiteSpeed = random.randint(10,15)
      
def update():
      global gameState
      if gameState == 'play':
            galagaMove()
            meteorMove()
            dynamiteMove()
            enemyMove()
            bulletMove()
            if score >= 5:
                  gameState = 'win'

##Create a group of bug
def enemyCreate(): 
      for row in range(0,2,1):
            for column in range(0,5,1):
                  enemies.append(Actor('bug'))
                  #enemies.append(bugSprite)  --> not working
                  enemies[-1].x = (100 + 100*column)
                  enemies[-1].y = (50 + 80*row)

def enemyMove():
      global bugXdirection
      global bugMoveDown
      global gameState
      global bulletActive
      global score
      if (len(enemies)>0) and (enemies[-1].x >= WIDTH or enemies[0].x <= 0 ):
            bugXdirection = bugXdirection*-1  #toggle direction
            bugMoveDown = True
      for enemy in enemies:
            enemy.x = enemy.x + 5*bugXdirection
            if bugMoveDown == True:
                  enemy.y = enemy.y + 50

            if enemy.colliderect(galagaSprite):
                  gameState = 'gameover'

            for bullet in bullets : 
                  if enemy.colliderect(bullet):
                        enemies.remove(enemy)
                        bullets.remove(bullet)
                        bulletActive = False
                        score = score + 1
                        print('score :', score)

      bugMoveDown = False
      
def draw():
      screen.blit('galagabg', (0,0))
      def restart():
            global gameState
            global score
            global bulletActive
            global bugMoveDown
            screen.draw.text('Press s to play', center = (WIDTH/2, 500), color = 'white', fontsize = 70)
            if keyboard.s == True:
                  gameState = 'play'
                  score = 0
                  bulletActive = False
                  bugMoveDown = False
                  enemies.clear()
                  bullets.clear()
                  enemyCreate()
                  
      if gameState == 'start':
            screen.draw.text('Galaga', center = (WIDTH/2, 80), color = 'white', fontsize = 100)
            restart()
      elif gameState == 'win':
            screen.draw.text('You Win', center = (WIDTH/2, 80), color = 'white', fontsize = 100)
            for enemy in enemies :
                  enemies.remove(enemy)
            restart()
      elif gameState == 'gameover':
            screen.draw.text('You Loose', center = (WIDTH/2, 80), color = 'white', fontsize = 100)
            for enemy in enemies :
                  enemies.remove(enemy)
            restart()
      elif gameState == 'play': 
            galagaSprite.draw()
            meteorSprite.draw()
            dynamiteSprite.draw()
            for enemy in enemies:
                  enemy.draw()
            for bullet in bullets:
                  bullet.draw()
      
pgzrun.go()
