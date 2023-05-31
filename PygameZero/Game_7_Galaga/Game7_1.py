import os
os.environ['SDL_VIDEO_WINDOW_POS'] = '%d, %d' % (200,50)
import pygame
import pgzrun
import random

#resolution is in pixels
WIDTH = 750
HEIGHT = 600
TITLE = 'Galaga'

bullets =[]
bugXdirection = 1
bugMoveDown = False
score = 0

class Player(Actor):
    #properties/ variable
    def __init__(self, image_file, pos):
        super().__init__(image_file, pos)
    #function/ method
    def galagaMoving(self):
        #setting moving
        if keyboard.a:
            self.x -= 10
        elif keyboard.d:
            self.x += 10
        #setting boundary
        if self.x < 0:
            self.x = 0
        elif self.x > WIDTH:
            self.x = WIDTH

class Item(Actor):
    #properties/ variable
    def __init__(self, image_file, pos):
        super().__init__(image_file, pos)
        self.speed = 10

    def move(self):
        self.y += self.speed
        if self.y >= HEIGHT:
            self.reset()

    def reset(self):
        self.pos = (random.randint(0, WIDTH), 50)
        self.speed = random.randint(10,15)

class Enemy(Actor):
    #properties/ variable
    def __init__(self, image_file):
        super().__init__(image_file)

class Bullet(Actor):
    #properties/ variable
    def __init__(self, image_file):
        super().__init__(image_file)

galagaSprite = Player('galaga', pos = (WIDTH/2, 550))
dynamiteSprite = Item('dynamite', pos = (WIDTH/2, 50))
meteorSprite = Item('meteor', pos = (WIDTH/2, 150))

enemies = []
def createEnemy():
    for row in range(0,2,1):
        for column in range(0,5,1):
            enemies.append(Enemy('bug'))
            enemies[-1].x = 10 + 80*column #[-1] refer to the last item
            enemies[-1].y = 50 + 60*row

createEnemy() #calling to create 10 bugs

def on_key_down(key):
    if key == key.SPACE:
        bullets.append(Bullet('laserred'))
        bullets[-1].pos = galagaSprite.pos

def draw():
    screen.blit('galagabg', (0,0))
    galagaSprite.draw()
    dynamiteSprite.draw()
    meteorSprite.draw()
    for enemy in enemies:
        enemy.draw()
    for bullet in bullets:
        bullet.draw()

def enemyMoving():
    global bugMoveDown, bugXdirection
    if enemies[-1].x > WIDTH or enemies[0].x < 0:
        bugMoveDown = True
        bugXdirection *= -1

    for enemy in enemies:
        enemy.x += 5*bugXdirection
        if bugMoveDown == True:
            enemy.y += 50
    bugMoveDown = False

def bulletMoving():
    global score 
    for bullet in bullets:
        if bullet.y <= 0:
            bullets.remove(bullet) #specific value
        else:
            bullet.y -= 10
        
        #collision enemy
        for enemy in enemies:
            if enemy.colliderect(bullet):
                bullets.remove(bullet)
                enemies.remove(enemy) 
                score += 1

def update():
    galagaSprite.galagaMoving()
    dynamiteSprite.move()
    meteorSprite.move()
    bulletMoving()
    enemyMoving()

pgzrun.go()