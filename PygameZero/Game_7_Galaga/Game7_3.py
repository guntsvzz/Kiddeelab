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


def on_key_down(key):
      global bulletActive 
      if key == keys.SPACE and bulletActive == False:
            bullets.append(Actor('laserred'))
            bullets[-1].pos = galagaSprite.pos
            bulletActive = True

def bulletMove():
      global bulletActive
      global score 
      for bullet in bullets:
            if bullet.y <= 0:
                  bullets.remove(bullet)
                  bulletActive = False
            else :
                  bullet.y = bullet.y - 10

            for enemy in enemies : 
                  if enemy.colliderect(bullet):
                        enemies.remove(enemy)
                        bullets.remove(bullet)
                        bulletActive = False
                        score = score + 1
                        print('score :', score)
                        
def galagaMove():
      if keyboard.a == True :
            galagaSprite.x = galagaSprite.x - 10
      elif keyboard.d == True :
            galagaSprite.x = galagaSprite.x + 10

      if galagaSprite.x >= WIDTH :
            galagaSprite.x = WIDTH
      if galagaSprite.x <= 0 :
            galagaSprite.x = 0

      if galagaSprite.colliderect(dynamiteSprite):
            print('gameover1')
            dynamiteReset()
      elif galagaSprite.colliderect(meteorSprite):
            print('gameover2')
            meteorReset()
      
def meteorMove():
      meteorSprite.y = meteorSprite.y + meteorSpeed
      if meteorSprite.y >= HEIGHT:
            meteorReset()
            
def meteorReset():
      global meteorSpeed
      meteorSprite.pos = (random.randint(0, WIDTH), 0)
      meteorSpeed = random.randint(5,15)

def dynamiteMove():
      dynamiteSprite.y = dynamiteSprite.y + dynamiteSpeed
      if dynamiteSprite.y >= HEIGHT:
            dynamiteReset()
            
def dynamiteReset():
      global dynamiteSpeed
      dynamiteSprite.pos = (random.randint(0, WIDTH), 0)
      dynamiteSpeed = random.randint(10,20)
      
def update():
      galagaMove()
      meteorMove()
      dynamiteMove()
      enemyMove()
      bulletMove()

##Create a group of bug
def enemyCreate(): 
      for row in range(0,2,1):
            for column in range(0,5,1):
                  enemies.append(Actor('bug'))
                  #enemies.append(bugSprite)  --> not working
                  enemies[-1].x = (100 + 100*column)
                  enemies[-1].y = (80 + 80*row)
enemyCreate()  #call only once

def enemyMove():
      global bugXdirection
      global bugMoveDown
      if (len(enemies)>0) and (enemies[-1].x >= WIDTH or enemies[0].x <= 0 ):
            bugXdirection = bugXdirection*-1  #toggle direction
            bugMoveDown = True
      for enemy in enemies:
            enemy.x = enemy.x + 5*bugXdirection
            if bugMoveDown == True:
                  enemy.y = enemy.y + 50

            if enemy.colliderect(galagaSprite):
                  print('gameover3')
                  
      bugMoveDown = False
      
def draw():
      screen.blit('galagabg', (0,0))
      galagaSprite.draw()
      meteorSprite.draw()
      #bugSprite.draw()
      dynamiteSprite.draw()
      for enemy in enemies:
            enemy.draw()
      for bullet in bullets:
            bullet.draw()
      
pgzrun.go()
