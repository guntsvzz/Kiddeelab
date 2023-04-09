import pygame
import pgzrun
import random

TITLE = 'Game 3'
WIDTH = 800
HEIGHT = 600

class Fruit(Actor):
    def __init__(self, image_file, pos = (0,random.randint(0,590))):
        super().__init__(image_file, pos)
        self.pos = pos
        self.vy = 1
        self.speed = 5
        
    def reset(self):
        self.vy = random.choice([-1,1]) #random up-down
        self.pos = random.choice([0,WIDTH]), random.randint(0,590) #random left-right
        if self.x <= 0: #left
            self.speed = random.randint(5,10) #positive
        elif self.x >= WIDTH: #right
            self.speed = random.randint(-10,-5) #negative

    def moving(self):
        self.y += self.vy
        self.x += self.speed
        if self.x > WIDTH or self.x < 0 or self.y > HEIGHT or self.y < 0:
            self.reset()

class Center(Actor):
    def __init__(self, image_file):
        super().__init__(image_file)
        self.game_state = 'start'
        self.score = 0

appleSprite = Fruit('apple1')
bombSprite  = Fruit('bomb1')
crosshair = Center('crosshair')

def draw():
    screen.blit('background',(0,0)) #x,y
    appleSprite.draw()
    bombSprite.draw()
    crosshair.draw()
    #Format:  screen.draw.text(text, (x,y), color=(r,g,b), fontsize=20)
    screen.draw.text(f'Score : {crosshair.score}',(15,10),color=(255,255,255),fontsize=40)

def update():
    appleSprite.moving()
    bombSprite.moving()

def on_mouse_move(pos, rel, buttons):
    crosshair.x = pos[0]
    crosshair.y = pos[1]

def on_mouse_down(pos, button):
    if button == mouse.LEFT:
        print('shoot')
        if appleSprite.collidepoint(pos):
            print('Apple Shot')
            crosshair.score += 1 #variable from object
            appleSprite.reset()
        if bombSprite.collidepoint(pos):
            print('Bomb Shoot')
            crosshair.game_state = 'gameover' #variable
            bombSprite.reset()
pgzrun.go()
