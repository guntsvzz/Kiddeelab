import pygame
import pgzrun
import random

TITLE = "Game1 Monkey"
WIDTH, HEIGHT = 800, 600
#Class Actor
monkeyimage = ['monkey1','monkey2']
#object = class()
monkeySprite = Actor('monkey1') #object
#object.variables
monkeySprite.pos = (WIDTH/2,HEIGHT/2) #tuple #pos = position
#object.method()
bananaSprite = Actor('banana')
bananaSprite.pos = (random.randint(0,WIDTH),0)
spiderSprite = Actor('spider')
spiderSprite.pos = (random.randint(0,WIDTH),0)

def draw():
    # format screen.blit(image,tuple_position)
    # screen.fill((255,255,0)) #Red Green Blue
    screen.blit('background',(0,0))
    screen.blit('ground',(0,0))
    monkeySprite.draw()
    bananaSprite.draw()
    spiderSprite.draw()

def movement(player):
    if keyboard.w or keyboard.up: #full
        player.y = player.y - 5 #full
        monkey_limit(player)
    if keyboard.a or keyboard.left: #short
        player.x -= 5 #short
        monkey_limit(player)
    if keyboard.s or keyboard.down: #short
        player.y += 5 #short
        monkey_limit(player)
    if keyboard.d or keyboard.right: #short
        player.x += 5 #short
        monkey_limit(player)

def monkey_limit(player):
    if player.x >= WIDTH:
        player.x = WIDTH
    if player.x <= 0:
        player.x = 0
    if player.y >= HEIGHT:
        player.y = HEIGHT
    if player.y <= 0:
        player.y = 0

def update():
    movement(monkeySprite)

pgzrun.go()