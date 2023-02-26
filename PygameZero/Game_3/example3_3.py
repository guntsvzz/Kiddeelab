import pygame
import pgzrun
import random

TITLE = 'Game 3'
WIDTH = 800
HEIGHT = 600

def Sprite(name, x, y, score = 1):
    actor = Actor(name)
    actor.pos = (x,y) #fix
    actor.vy = 1
    actor.speed = 5
    actor.score = score
    return actor

appleSprite = Sprite('apple1', 0, random.randint(0,590))
bombSprite  = Sprite('bomb1',  0, random.randint(0,590))
crosshair = Actor('crosshair')

def draw():
    screen.blit('background',(0,0)) #x,y
    appleSprite.draw()
    bombSprite.draw()
    crosshair.draw()

def reset(name_sprite):
    name_sprite.vy = random.choice([-1,1]) #random up-down
    name_sprite.pos = random.choice([0,WIDTH]), random.randint(0,590) #random left-right
    if name_sprite.x <= 0: #left
        name_sprite.speed = random.randint(5,10) #positive
    elif name_sprite.x >= WIDTH: #right
        name_sprite.speed = random.randint(-10,-5) #negative

def moving(name_sprite):
    name_sprite.y += name_sprite.vy
    name_sprite.x += name_sprite.speed
    if name_sprite.x > WIDTH or name_sprite.x < 0 or name_sprite.y > HEIGHT or name_sprite.y < 0:
        reset(name_sprite)

def update():
    moving(appleSprite)
    moving(bombSprite)

def on_mouse_move(pos, rel, buttons):
    crosshair.x = pos[0]
    crosshair.y = pos[1]


pgzrun.go()
