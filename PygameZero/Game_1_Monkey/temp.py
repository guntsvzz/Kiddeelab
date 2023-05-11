import pygame
import pgzrun
import random
TITLE = "Game1 Monkey"
WIDTH, HEIGHT = 800, 600
actors = []
#Class Actor
monkeyimage = ['monkey1','monkey2']
#object = class()
monkeySprite = Actor('monkey1') #object
#object.variables
monkeySprite.pos = (WIDTH/2,HEIGHT/2) #tuple #pos = position
actors.append(monkeySprite)

def draw():
    # format screen.blit(image,tuple_position)
    # screen.fill((255,255,0)) #Red Green Blue
    screen.blit('background',(0,0))
    screen.blit('ground',(0,0))
    for s in actors:
        s.draw()

def update(): #1/60 second
    if keyboard.space:
        # actors.remove(monkeySprite)
        del monkeySprite

pgzrun.go()