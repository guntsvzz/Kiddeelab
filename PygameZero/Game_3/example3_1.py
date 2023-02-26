import pygame
import pgzrun
import random

TITLE = 'Game 3'
WIDTH = 800
HEIGHT = 600

def Sprite(name,x,y):
    actor = Actor(name)
    actor.pos = (x,y)
    actor.vy = 1
    actor.speed = 5
    return actor

appleSprite = Sprite('apple1', 0, random.randint(0,590))
bombSprite  = Sprite('bomb1',  0, random.randint(0,590))

def draw():
    screen.blit('background',(0,0)) #x,y
    appleSprite.draw()
    bombSprite.draw()

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

pgzrun.go()
